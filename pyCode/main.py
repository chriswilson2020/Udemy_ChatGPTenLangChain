import os
import argparse

api_key = os.environ.get("OPENAI_API_KEY")

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")

args = parser.parse_args()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt
)

result = code_chain.invoke(
    {
        "language": args.language,
        "task": args.task
    }
)

print(result["text"])