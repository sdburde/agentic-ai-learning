import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import youtube_dl
import re

# Load environment variables
load_dotenv()

# Initialize Groq client
groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model_name="Gemma2-9b-it", groq_api_key=groq_api_key, temperature=0.3)

# Custom CSS for better appearance
st.markdown("""
<style>
    .stApp {
        max-width: 900px;
        padding: 2rem;
    }
    .summary-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-top: 1rem;
        color: rgba(0, 0, 0, 1);  /* White text for contrast */
    }
</style>
""", unsafe_allow_html=True)

def extract_video_id(url):
    """Extract video ID from various YouTube URL formats"""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def get_auto_generated_transcript(video_id):
    """Fetch auto-generated transcript using youtube_dl"""
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitleformat': 'vtt',
        'quiet': True,
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            
            if 'automatic_captions' not in info or 'en' not in info['automatic_captions']:
                return None, None
            
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
            subtitle_file = f"{info['title']} [{video_id}].en.vtt"
            
            try:
                with open(subtitle_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    transcript_lines = [
                        line.strip() for line in lines 
                        if line.strip() and 
                        not line.startswith('WEBVTT') and 
                        not line.startswith('Kind:') and 
                        not line.startswith('Language:') and 
                        not re.match(r'\d\d:\d\d:\d\d', line)
                    ]
                    full_text = ' '.join(transcript_lines)
                    return full_text, None  # No timestamps available in this format
            except FileNotFoundError:
                return None, None
                
    except Exception as e:
        st.error(f"Error fetching auto-generated transcript: {str(e)}")
        return None, None

def extract_transcript_details(youtube_video_url):
    """Improved transcript extraction with multiple fallbacks"""
    video_id = extract_video_id(youtube_video_url)
    
    # Try official transcript first
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        full_text = "\n".join(
            f"[{chunk['start']:.0f}s] {chunk['text']}" 
            for chunk in transcript_data
        )
        st.info("Using official transcript")
        return full_text, video_id
    
    except (TranscriptsDisabled, NoTranscriptFound):
        st.warning("Official transcript not available, trying auto-generated...")
        
        # Try auto-generated transcript as fallback
        auto_transcript, _ = get_auto_generated_transcript(video_id)
        if auto_transcript:
            st.info("Using auto-generated transcript (no timestamps available)")
            return auto_transcript, video_id
        
        st.error("This video doesn't have English captions available.")
        return None, None
    
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None, None

def generate_groq_summary(transcript_text):
    """Generate summary using Groq's Gemma model with truncation"""
    # Truncate transcript to avoid context length issues (approx. 800-1000 words)
    MAX_CHARS = 4000
    if len(transcript_text) > MAX_CHARS:
        transcript_text = transcript_text[:MAX_CHARS] + "\n[Transcript truncated due to length]"
        st.warning("Transcript was truncated to fit model limits. Summary covers first ~1000 words.")

    prompt = PromptTemplate.from_template(
        """You are a YouTube video summarizer. Create a detailed summary with:
        - Key points as bullet points
        - Timestamps for important sections (if in transcript)
        - Main takeaways
        - Keep it under 500 words
        
        Transcript:
        {text}
        
        Concise Summary:"""
    )
    
    chain = prompt | model
    
    try:
        response = chain.invoke({"text": transcript_text})
        return response.content
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return None

# Streamlit UI
st.title("🎥 YouTube Video Summarizer")
st.markdown("Get concise summaries of YouTube videos with timestamps and key points")

youtube_link = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

# if youtube_link:
#     try:
#         video_id = extract_video_id(youtube_link)
#         st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
#     except:
#         st.warning("Couldn't load video thumbnail")
if youtube_link:
    try:
        # Handle different YouTube URL formats
        if "youtu.be/" in youtube_link:
            video_id = youtube_link.split("youtu.be/")[1].split("?")[0]
        else:
            video_id = youtube_link.split("v=")[1].split("&")[0]
            
        st.image(
            f"http://img.youtube.com/vi/{video_id}/0.jpg", 
            use_container_width=True,
            caption="Video Thumbnail"
        )
    except Exception as e:
        st.warning(f"Couldn't load video thumbnail: {str(e)}")

if st.button("Generate Summary", type="primary"):
    if not youtube_link:
        st.warning("Please enter a YouTube URL")
    else:
        with st.spinner("Fetching transcript and generating summary..."):
            transcript_text, video_id = extract_transcript_details(youtube_link)
            
            if transcript_text:
                with st.expander("View Full Transcript", expanded=False):
                    st.text_area("Transcript", transcript_text, height=200)
                
                summary = generate_groq_summary(transcript_text)
                
                if summary:
                    st.markdown("## 📝 Summary")
                    st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
                    
                    # Download buttons
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="Download Summary",
                            data=summary,
                            file_name=f"summary_{video_id}.txt",
                            mime="text/plain"
                        )
                    with col2:
                        st.download_button(
                            label="Download Transcript",
                            data=transcript_text,
                            file_name=f"transcript_{video_id}.txt",
                            mime="text/plain"
                        )