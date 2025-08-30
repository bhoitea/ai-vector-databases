python
ab-mbp-v9qpf:chromadb abhoite$ python3 chromadb_cloud_demo.py
import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
# ───────────────────────────────────────────────────────────────────────────────
# Step 1: Connect to Chroma Cloud using HTTP client.
# No local model execution occurs--calls go to remote Chroma service.
#───────────────────────────────────────────────────────────────────────────────
client = chromadb.HttpClient(
   ssl=True,
   host="api.trychroma.com",
   tenant="3ae890ac-9a1e-4e56-aff2-3d1181d85643",
   database="chromadb_demo",
   headers={"x-chroma-token": "ck-7mBYcbzCHPQZCENKHabPBSVhwnp17SJhzgoFuXhRRF48"}
)
# ───────────────────────────────────────────────────────────────────────────────
# Step 2: Create a semantic collection using Chroma's default embedding function
# DefaultEmbeddingFunction uses the HuggingFace all‑MiniLM‑L6‑v2 model via ONNX runtime. :contentReference[oaicite:0]{index=0}
# Metadata sets 'hnsw:space' to 'cosine' so that similarity is based on cosine distance. :contentReference[oaicite:1]{index=1}
#───────────────────────────────────────────────────────────────────────────────
try:
   client.delete_collection("cloud_demo_collection")
   print("🗑️ Deleted existing 'cloud_demo_collection'")
except:
   pass
collection = client.create_collection(
   name="cloud_demo_collection",
   embedding_function=DefaultEmbeddingFunction(),
   metadata={"hnsw:space": "cosine"}
)
# ───────────────────────────────────────────────────────────────────────────────
# Step 3: Add 8 product descriptions
# Documents will be automatically embedded using the embedding function. :contentReference[oaicite:2]{index=2}
# Metadata fields are flat (primitive types only); no lists or nested types. :contentReference[oaicite:3]{index=3}
#───────────────────────────────────────────────────────────────────────────────
documents = [
   "Wireless headphones with long battery & premium audio",
   "Organic cotton t‑shirt in multiple colors",
   "Smartphone with triple camera & 5G support",
   "Ergonomic office chair with lumbar support",
   "Smart fitness tracker with heart rate monitoring and GPS",
   "Premium coffee beans sourced from sustainable farms",
   "Waterproof hiking boots with excellent grip and durability",
   "Smart home security camera with night vision and mobile alerts"
]
metadatas = [
   {"category": "electronics", "price": 300, "in_stock": True},
   {"category": "clothing",    "price": 30,  "in_stock": True},
   {"category": "electronics", "price": 800, "in_stock": False},
   {"category": "furniture",   "price": 450, "in_stock": True},
   {"category": "electronics", "price": 200, "in_stock": True},
   {"category": "food",        "price": 25,  "in_stock": True},
   {"category": "footwear",    "price": 160, "in_stock": True},
   {"category": "electronics", "price": 150, "in_stock": True}
]
ids = [f"item{i}" for i in range(8)]
collection.add(ids=ids, documents=documents, metadatas=metadatas)
print(f"✅ Collection '{collection.name}' now contains {collection.count()} items.")
# ───────────────────────────────────────────────────────────────────────────────
# Step 4: Semantic search using natural language query
# query_texts triggers automatic embedding using the collection's embedding function. :contentReference[oaicite:4]{index=4}
# Filter by category electronics using single field filter ({ "$eq": ... }) which is valid syntax. :contentReference[oaicite:5]{index=5}
#───────────────────────────────────────────────────────────────────────────────
results = collection.query(
   query_texts=["wireless headphones"],
   n_results=3,
   where={"category": {"$eq": "electronics"}},
   include=["documents", "metadatas", "distances"]
)
# ───────────────────────────────────────────────────────────────────────────────
# Step 5: Print top‑3 results
# Since 'hnsw:space' is cosine, distances are cosine distances (1 - cosine similarity). Lower is more similar. :contentReference[oaicite:6]{index=6}
# Convert to similarity via (1 - distance).
#───────────────────────────────────────────────────────────────────────────────
print("\n🔍 Top 3 results for query: 'wireless headphones'\n")
for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
   similarity = 1 - dist
   print(f"- {meta['category']} | Price: ${meta['price']} | In Stock: {meta['in_stock']} | Similarity: {similarity:.3f}")
   print(f"  \"{doc}\"\n")