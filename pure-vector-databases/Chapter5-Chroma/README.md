# ChromaDB Demo

This repository demonstrates how to use **ChromaDB** in two ways:

1. **Self-Hosted (Local / Persistent)** using the Python client.
2. **ChromaDB Cloud** using HttpClient with API keys.

---

## 📂 Repo Structure

---

chromadb-demo/
├── README.md
└── scripts/
    ├── chromadb_local_demo.py
    └── chromadb_cloud_demo.py
---------------------------------

## 🚀 Installation & Setup

First, install ChromaDB:

```bash
pip install chromadb
```

---

## 🖥️ Self-Hosted ChromaDB Demo

In this example, we use the Python client to create a collection, insert documents, and perform a semantic search with ChromaDB.

Run the local demo script:

```bash
python scripts/chromadb_local_demo.py
```

This will:

- Create a collection called `movie_reviews`.
- Insert sample movie reviews with genres & ratings.
- Prompt you for a search query and return top semantic matches.

**Expected Output**

```
✅ Added movie reviews to ChromaDB collection
Collection contains 8 documents
Enter your search query: funny romantic movie
🔍 Searching for: "funny romantic movie"
🎯 Top matching reviews:Similarity: 0.477 | Genre: comedy | Rating: 7.8
"A heartwarming romantic comedy that will make you laugh and cry at the same time."Similarity: 0.017 | Genre: sci-fi | Rating: 8.7
"Brilliant sci-fi thriller with mind-bending plot twists and excellent acting."Similarity: -0.051 | Genre: animation | Rating: 8.2
"Family-friendly animated film with beautiful animation and memorable characters."
```

---

## ☁️ ChromaDB Cloud Demo

1. Sign up at [ChromaDB Cloud](https://cloud.trychroma.com).
2. Create a database instance
3. Create an API key and get your endpoint/tenant details.
4. Update `scripts/chromadb_cloud_demo.py` with your API key and connection info.

Run with:

```bash
python scripts/chromadb_cloud_demo.py
```

**Expected Output**

```
🗑️ Deleted existing 'cloud_demo_collection'
✅ Collection 'cloud_demo_collection' now contains 8 items.
🔍 Top 3 results for query: 'wireless headphones'
- electronics | Price: $300 | In Stock: True | Similarity: 0.756
  "Wireless headphones with long battery & premium audio"
- electronics | Price: $200 | In Stock: True | Similarity: 0.214
  "Smart fitness tracker with heart rate monitoring and GPS"
- electronics | Price: $150 | In Stock: True | Similarity: 0.137
  "Smart home security camera with night vision and mobile alerts"

```

This will:

- Create a collection `cloud_demo_collection`.
- Insert sample product descriptions with metadata.
- Perform semantic search on product data (e.g., *wireless headphones*).

## Official Docs & Resources

* Open-source database: :[https://qdrant.tech/documentation/](https://qdrant.tech/documentation/)
* Cloud documentation: [https://qdrant.tech/documentation/cloud-intro/](https://qdrant.tech/documentation/cloud-intro/)
* Github:[https://github.com/qdrant/qdrant](https://github.com/qdrant/qdrant)
* Qdrant Cloud:[https://cloud.qdrant.io/](https://cloud.qdrant.io/)
* Practical Examples: [https://qdrant.tech/articles/practicle-examples/](https://qdrant.tech/articles/practicle-examples/)**
