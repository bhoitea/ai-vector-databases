# Pinecone Demo

This repository demonstrates how to:

* Connect to Pinecone with an API key
* Create and delete indexes
* Upsert vectors with metadata
* Perform similarity search
* Apply metadata filters for hybrid queries
* Understand cosine similarity scores

---

## 📂 Project Structure

```
Chapter1-Pinecone/
│
├── scripts/
│   └── pinecone_demo.py    
│
└── README.md         
```

---

## 🚀 Quick Start

### 1️⃣ Install dependencies

```
pip install pinecone
```

---

### 2️⃣ Set your API key

Update `pinecone_demo.py` with your Pinecone API key:

```
pc = Pinecone(api_key="pcsk_3g5ZMv_ZEf5gFp1bLeGF*******", environment="us-east-1-aws")**
```

---

### 3️⃣ Run the demo

```
python3 scripts/pinecone_demo.py
```

**Expected Output**

```
🗑️ Deleted existing index 'docs-example'.
✅ Created new index 'docs-example'.
✅ Upserted 3 vectors into namespace 'example-namespace'.

⏳ Waiting for vectors to be indexed...
⏳ Attempt 1: 0/3 indexed. Retrying in 2s...
⏳ Attempt 2: 0/3 indexed. Retrying in 2s...
⏳ Attempt 3: 0/3 indexed. Retrying in 2s...

🔍 Query text: I'm in the mood for a funny movie about family adventures.
🔍 Query vector preview: [0.11, 0.11, 0.11, 0.11, 0.11] ...

📋 Results for your query:
- ID: B | Score: 1.0000
  Genre: comedy, Year: 2021.0
  Description: Show me a light comedy featuring family road‑trip adventures.

- ID: A | Score: 1.0000
  Genre: comedy, Year: 2020.0
  Description: I want a heartwarming comedy about a stand‑up comedian.

🧾 All inserted vectors:
- A: genre=comedy, year=2020
  text: I want a heartwarming comedy about a stand‑up comedian.
- B: genre=comedy, year=2021
  text: Show me a light comedy featuring family road‑trip adventures.
- C: genre=thriller, year=2022
  text: Recommend a suspense thriller with lots of plot twists.

```

This will:

* Create a Pinecone index
* Insert 3 sample vectors (A, B, C) with metadata
* Query with a vector and metadata filter
* Return similarity results

---

## References

* Pinecone Database: https://docs.pinecone.io/guides/get-started/overview
* Pinecone Assistant:[https://docs.pinecone.io/guides/assistant/overview](https://docs.pinecone.io/guides/assistant/overview)
* Notebooks – Example Jupyter notebooks demoing Pinecone with OpenAI, LangChain, and others. [ https://docs.pinecone.io/examples/notebooks](https://docs.pinecone.io/examples/notebooks)
* SDK Reference –SDKs (Python, Node.js, etc.) and API usage. [https://docs.pinecone.io/reference/pinecone-sdks](https://docs.pinecone.io/reference/pinecone-sdks)**
