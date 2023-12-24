import os
from openai import OpenAI
from dotenv import load_dotenv


def get_embedding(text,model="text-embedding-ada-002"):
    response = client.embeddings.create(
    model=model,
    input=text,
    encoding_format="float"
    )
    return response.data[0].embedding

def get_embedding_list(text_list,model="text-embedding-ada-002"):
    if(len(text_list) == 0):
        return []
    response = client.embeddings.create(
    model=model,
    input=text_list,
    encoding_format="float"
    )
    embedding_list = [entry.embedding for entry in response.data]
    return embedding_list

def test():
    response = client.embeddings.create(
    model="text-embedding-ada-002",
    input="The food was delicious and the waiter...",
    encoding_format="float"
    )

    print(f"{len(response.data[0].embedding)} floats, used {response.usage.total_tokens} tokens")
    return


def create_client():
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client

client = create_client()
