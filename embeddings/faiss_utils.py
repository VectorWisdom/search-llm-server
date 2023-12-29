import utils as utl
import numpy as np
import faiss

def build_index(index_file,vectors_file,model):
    global vectors
    global faiss_index
    embeddings = utl.load_pickle(vectors_file)
    vectors = embeddings[model]
    np_vectors = np.array(list(vectors.values()))
    dimension = np_vectors.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(np_vectors)
    faiss.write_index(faiss_index,index_file)
    return

def load_index(index_file,vectors_file,model):
    global vectors
    global faiss_index
    faiss_index = faiss.read_index(index_file)
    embeddings = utl.load_pickle(vectors_file)
    vectors = embeddings[model]
    return

def search(vector,top_k = 5):
    top_k = 5
    np_query_vector = np.array(vector).reshape(1,-1)
    distances, indices = faiss_index.search(np_query_vector, top_k)
    hashes_list = list(vectors.keys())
    hashes = [hashes_list[index] for index in indices[0] ]
    results = []
    for i in range(top_k):
        results.append({
            "hash":hashes[i],
            "distance":distances[0][i]
        })
    return results


vectors = {}
faiss_index = None
