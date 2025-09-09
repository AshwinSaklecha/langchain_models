from langchain_openai import OpenAI
# this OpenAI is a class
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("what is the capital of India")
print(result)

# Dont use this code, as this is not the recommended way. This code is just for demonstration.