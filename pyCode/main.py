import os

api_key = os.environ.get("OPENAI_API_KEY")

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

result = llm.invoke("Write a very very short poem")
print(result.content)
