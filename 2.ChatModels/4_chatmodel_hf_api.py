from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the CEO of Google")

print(result.content)

# Ok so first I changed the model from TinyLama to Mistral and also changed the env varible name to HUGGINGFACEHUB_API_TOKEN and then got this HUGGINGFACEHUB_API_TOKEN As of my last update, the CEO of Google is Sundar Pichai. He has been serving as the CEO since October 2015. However, I recommend checking the latest sources to confirm as executive roles can change over time.
