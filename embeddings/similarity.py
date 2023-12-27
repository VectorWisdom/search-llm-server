import utils as utl

chunk_list_file = "../.data/embedding_chunks.json"
vectors_file="../.data/vectors.pkl"
# 'text-embedding-ada-002', 'all-MiniLM-L6-v2'
model="all-MiniLM-L6-v2"

sentence = "A smart sensor with a modern wireless protocol, that can sense the environment without consuming much power"

print(f"embed {model} start")
chunk_list = utl.load_json(chunk_list_file)
vectors = utl.get_embeddings(chunk_list,vectors_file,model,batch_size=200)
print(f" get_embeddings() returned {len(vectors)} vectors")

target = utl.get_one_embedding(sentence,model)

