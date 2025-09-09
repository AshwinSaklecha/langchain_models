from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Why Magnus Carlsen is the best Chess Player?")
print(result.content)

# So this model will be downloaded in C: drive, and after installation you will also get the answer.
# Here I am not gonna run this code, as my machine is not that powerful to handle this.
