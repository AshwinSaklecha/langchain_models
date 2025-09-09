from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "Madrid is the capital of Spain"
documents = [
    "Berlin is capital of germany", 
    "Tokyo is capital of japan",
    "Rome is the capital of Italy"
]

# vector = embedding.embed_query(text)
vector = embedding.embed_documents(documents)

print(str(vector))

# I am not able to run this because, I guess I also need to install some transformers library too