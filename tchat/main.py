import os 
api_key = os.environ.get("OPENAI_API_KEY")

from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain


chat = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[HumanMessagePromptTemplate.from_template("{content}")]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt
)

while True:
    content = input(">> ")
    result = chain.invoke({"content": content})
    print(result["text"])