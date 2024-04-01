import os 
api_key = os.environ.get("OPENAI_API_KEY")

from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory


chat = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo", verbose=True)
memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm=chat
    #chat_memory=FileChatMessageHistory("messages.json")
    )

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    #verbose=True
)

while True:
    content = input(">> ")

    if content == "exit()":
        print("Bye bye!")
        break

    result = chain.invoke({"content": content})
    print(result["text"])