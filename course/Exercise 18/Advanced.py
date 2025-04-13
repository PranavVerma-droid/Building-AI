import math

def main(text):
    # Split text into lines and lowercase everything
    docs = [line.lower().split() for line in text.splitlines()]
    
    # Get unique words across all documents
    unique_words = set()
    for doc in docs:
        unique_words.update(doc)
    
    # Calculate document frequency (df) for each word
    N = len(docs)
    df = {}
    for word in unique_words:
        df[word] = sum(1 for doc in docs if word in doc) / N
    
    # Calculate tf-idf vectors for each document
    tfidf_vectors = []
    for doc in docs:
        vector = []
        doc_len = len(doc)
        
        for word in unique_words:
            # Term frequency: count of word in document / document length
            tf = doc.count(word) / doc_len if doc_len > 0 else 0
            
            # TF-IDF score
            idf = math.log(1/df[word], 10) if df[word] > 0 else 0
            vector.append(tf * idf)
        
        tfidf_vectors.append(vector)
    
    # Find the most similar pair using cosine similarity
    max_similarity = -1
    most_similar = (0, 0)
    
    for i in range(len(docs)):
        for j in range(i+1, len(docs)):
            # Calculate dot product
            dot_product = sum(a * b for a, b in zip(tfidf_vectors[i], tfidf_vectors[j]))
            
            # Calculate magnitudes
            mag_i = math.sqrt(sum(x * x for x in tfidf_vectors[i]))
            mag_j = math.sqrt(sum(x * x for x in tfidf_vectors[j]))
            
            # Calculate cosine similarity
            similarity = dot_product / (mag_i * mag_j) if mag_i > 0 and mag_j > 0 else 0
            
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar = (i, j)
    
    # Directly print the tuple to match expected output
    print(most_similar)
    
    # Also return it in case it's needed
    return most_similar

# Test with the example text
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

main(text)  # Just call the function, the print is inside