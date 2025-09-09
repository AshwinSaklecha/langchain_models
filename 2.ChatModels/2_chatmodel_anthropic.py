from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=10)
# temperature tells how creative the model is, and its value ranges from 0 to 2

result = model.invoke("what is the capital of india")

# print(result)
print(result.content)