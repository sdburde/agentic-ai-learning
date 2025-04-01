A hands-on learning resource for agentic AI using LangChain, LangGraph, Pydantic, and RAG systems.

# Agentic AI Learning

![GitHub last commit](https://img.shields.io/github/last-commit/sdburde/agentic-ai-learning)
![GitHub repo size](https://img.shields.io/github/repo-size/sdburde/agentic-ai-learning)

Welcome to **Agentic AI Learning**! This repository is a comprehensive learning resource and experimentation playground for building agentic AI systems using tools like **LangChain**, **LangGraph**, **Pydantic**, and various vector stores and embeddings. It includes Jupyter notebooks, Python scripts, and sample data to explore concepts such as data ingestion, text splitting, embeddings, vector stores, chatbots, RAG (Retrieval-Augmented Generation), and workflows.

The goal of this project is to document my journey in mastering agentic AI and to serve as a reference for others interested in these technologies.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

---

## Project Structure

The repository is organized into topical directories, each containing notebooks, scripts, and sample files for hands-on learning. Below is an overview of the structure:

```
agentic-ai-learning/
├── 1-Langchain/                # Introduction to LangChain basics
│   ├── 1.1-gettingstarted.ipynb
│   ├── 1.1-gettingstarted_practice.ipynb
│   ├── RAG.ipynb
│   └── speech.txt
├── 2-LangchainConti/           # Advanced LangChain topics
│   ├── 2.1-DataIngestion/      # Data ingestion techniques
│   ├── 2.2-DataTransformer/    # Text splitting methods
│   ├── 2.3-Embeddings/         # Embedding models (Ollama, Hugging Face, etc.)
│   └── 2.4-VectorStore/        # Vector store implementations (FAISS, Chroma)
├── 3-Chatbots/                 # Chatbot development
├── 4-langgraph/                # Introduction to LangGraph
├── 5-langgraph_agents/         # LangGraph with agents and chains
├── 6-Debugging/                # Debugging tools and scripts
├── 7-Pydantic/                 # Pydantic for data validation
├── 7-Workflows/                # Workflows and human-in-the-loop systems
├── 8-RAGS/                     # Retrieval-Augmented Generation (RAG) explorations
├── AI-LLM-Chatbot/             # (Excluded from Git - placeholder directory)
├── campusx_langchain/          # LangChain tutorials from CampusX
├── yt_video_summerizer/        # YouTube video summarizer project
├── README.md                   # This file
└── requirement.txt             # Dependencies
```

For a detailed file listing, run `tree` in the repository root (see [full structure](#full-directory-structure) below).

---

## Key Features

- **LangChain Basics**: Getting started with LangChain, including RAG implementations.
- **Data Processing**: Ingestion, transformation, and splitting of text data (e.g., recursive splitters, HTML splitters).
- **Embeddings**: Experiments with various embedding models (Ollama, Hugging Face).
- **Vector Stores**: Implementations with FAISS and Chroma for efficient retrieval.
- **Chatbots**: Building conversational agents with tools and memory.
- **LangGraph**: Graph-based workflows and agentic systems.
- **Pydantic**: Structured data validation and workflows.
- **RAG**: Adaptive and agentic RAG systems for enhanced retrieval.
- **YouTube Summarizer**: A mini-project to summarize YouTube videos.

---

## Prerequisites

- **Python 3.8+**
- **Jupyter Notebook** (for running `.ipynb` files)
- **Git** (for cloning and contributing)
- Access to API keys for models (e.g., OpenAI, Hugging Face) - store these securely in a `.env` file.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github-sdburde:sdburde/agentic-ai-learning.git
   cd agentic-ai-learning
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirement.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your API keys (e.g., `OPENAI_API_KEY=your-key-here`).
   - Use `python-dotenv` to load these in your scripts/notebooks.

5. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

---

## Usage

- Navigate to a directory (e.g., `1-Langchain/`) and open a notebook (e.g., `1.1-gettingstarted.ipynb`) to explore the code and concepts.
- Run scripts (e.g., `yt_video_summerizer/st.py`) directly with `python script_name.py`.
- Modify sample files (e.g., `speech.txt`, `syllabus.pdf`) to experiment with your own data.

Example:
```bash
cd 8-RAGS
jupyter notebook 1-AgenticRAG.ipynb
```

---

## Contributing

Contributions are welcome! If you’d like to add a feature, fix a bug, or improve documentation:

1. Fork the repository.
2. Create a branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to your fork: `git push origin feature-name`.
5. Open a pull request.

---
