# import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', temperature=0.5, max_completion_tokens=5)
result = model.invoke("tell me uniqe word write just a single word")
print(result.content)