from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Berlin is capital of germany", 
    "Tokyo is capital of japan",
    "Rome is the capital of Italy"
]

result = embedding.embed_query(documents)

print(str(result))

# this way we can create embeddings of multiple texts
