import numpy as np

def search_similar_vectors(query, vectors, top_k=5):
    np_vectors = np.array(list(vectors.values()))
    np_query_vector = np.array(query).reshape(1, -1)
    # np.dot() cosine_similarity() for unified vectors
    similarities = [(hash_key, np.dot(np_query_vector, vec))
                    for hash_key, vec in zip(vectors.keys(), np_vectors)]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]

def compute_similarity_matrix(vectors):
    keys = list(vectors.keys())
    np_vectors = np.array(list(vectors.values()))
    similarity_matrix = np.zeros((len(np_vectors), len(np_vectors)))

    for i, vec1 in enumerate(np_vectors):
        for j, vec2 in enumerate(np_vectors):
            similarity_matrix[i, j] = np.dot(vec1, vec2)
    
    return keys, similarity_matrix
