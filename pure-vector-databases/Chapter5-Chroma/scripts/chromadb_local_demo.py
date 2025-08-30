# chromadb_local_demo.py
# Step 1: Import ChromaDB
import chromadb
from chromadb.config import Settings

# Step 2: Create a ChromaDB client
# Using ephemeral client for this demo (in-memory storage)
client = chromadb.Client()

# For persistent storage, use:
# client = chromadb.PersistentClient(path="./chromadb_data")

# Step 3: Create or get a collection
collection_name = "movie_reviews"

# Delete collection if it exists (for clean demo)
try:
    client.delete_collection(collection_name)
except:
    pass  # Collection doesn't exist

# Create collection with automatic embedding
collection = client.create_collection(
    name=collection_name,
    metadata={"description": "Movie reviews for similarity search"}
)
# Step 4: Sample movie review data
reviews = [
    "Amazing action sequences and stunning visual effects make this superhero movie a must-watch.",
    "A heartwarming romantic comedy that will make you laugh and cry at the same time.",
    "This documentary about wildlife conservation is both educational and deeply moving.",
    "Brilliant sci-fi thriller with mind-bending plot twists and excellent acting.",
    "Family-friendly animated film with beautiful animation and memorable characters.",
    "Intense psychological drama that keeps you on the edge of your seat.",
    "Epic fantasy adventure with incredible world-building and magical creatures.",
    "True crime series that uncovers shocking revelations about a cold case."
]
# Step 5: Add documents to the collection
# ChromaDB will automatically generate embeddings
collection.add(
    documents=reviews,
    metadatas=[
        {"genre": "action", "rating": 8.5},
        {"genre": "comedy", "rating": 7.8},
        {"genre": "documentary", "rating": 9.1},
        {"genre": "sci-fi", "rating": 8.7},
        {"genre": "animation", "rating": 8.2},
        {"genre": "drama", "rating": 9.0},
        {"genre": "fantasy", "rating": 8.9},
        {"genre": "crime", "rating": 8.3}
    ],
    ids=[f"review_{i}" for i in range(len(reviews))]
)
print("✅ Added movie reviews to ChromaDB collection")
print(f"Collection contains {collection.count()} documents")
# Step 6: Interactive search
query = input("\nEnter your search query: ")
print(f"\n🔍 Searching for: \"{query}\"")

# Step 7: Perform similarity search
results = collection.query(
    query_texts=[query],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)
# Step 8: Display results
print("\n🎯 Top matching reviews:")
for i in range(len(results['documents'][0])):
    doc = results['documents'][0][i]
    metadata = results['metadatas'][0][i]
    distance = results['distances'][0][i]
    similarity = 1 - distance  # Convert distance to similarity
    
    print(f"- Similarity: {similarity:.3f} | Genre: {metadata['genre']} | Rating: {metadata['rating']}")
    print(f"  \"{doc}\"")
    print()