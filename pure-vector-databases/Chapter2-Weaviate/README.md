# Weaviate Semantic Search Demos

This chapter demonstrates how to use **Weaviate** for semantic search, both in local (self-hosted) and cloud environments.

---

## 📂 Project Structure

```warp-runnable-command
Chapter2-Weaviate/
│
├── scripts/
│   ├── docker-run.sh                       # Start Weaviate in Docker
│   ├── self_hosted_telecom_demo.py         # Telecom Call Summary Semantic Search (local demo)
│   └── cloud_jeopardy_semantic_search_demo.py # Jeopardy! Q&A search (cloud demo)
│
└── README.md                               # This file
```

---

## 🚀 Quick Start

### 1️⃣ Run Weaviate in Docker

```warp-runnable-command
docker run -p 8081:8080 -p 50051:50051 cr.weaviate.io/semitechnologies/weaviate:1.31.5
```

Once started, confirm readiness:

```warp-runnable-command
curl -i http://localhost:8081/v1/.well-known/live
```

Expected response:

```warp-runnable-command
HTTP/1.1 200 OK
Date: Sat, 12 Jul 2025 14:40:54 GMT
Content-Length: 0
```

Once started, confirm readiness using [http://localhost:8081/v1](http://localhost:8081/v1) URL:

---

### 2️⃣ Install Python Client

Weaviate’s Python client works with Python  **3.8+** . Install from PyPI:

```warp-runnable-command
pip install -U weaviate-client
```

---

### 3️⃣ Run Telecom Call Summary Search (Local Demo)

```warp-runnable-command
python scripts/self_hosted_telecom_demo.py
```

**Expected Output**

```
➡️ Connecting to Milvus Standalone...
➡️ Preview of inserted data:
 • id=0, subj=history, text='Artificial intelligence was founded as an academic discipline in 1956.'
 • id=1, subj=history, text='Alan Turing was the first person to conduct substantial research in AI.'
 • id=2, subj=history, text='Born in Maida Vale, London, Turing was raised in southern England.'
 • id=3, subj=science, text='Marie Curie pioneered research in radioactivity and won two Nobel Prizes.'
 • id=4, subj=history, text='The first computer programmer was Ada Lovelace in the 19th century.'
➡️ User query: "research in AI"
✅ Simulated query vector sample:
 [-0.48106721173394495, 0.46393661985486356, 0.15912996953044112, 0.4388697499234273, -0.8990788600806903] ...
✅ Search results:
🎉 Script completed.

```

This script connects to your **local Docker Weaviate instance** and demonstrates telecom call summary semantic search.

---

### 4️⃣ Run Jeopardy! Q&A Search (Cloud Demo)

```warp-runnable-command
python scripts/cloud_jeopardy_semantic_search_demo.py
```

**Expected Output**

```
🔌 Connected
📥 Inserting 10 items
✅ Inserted all items

📄 Full dataset:
 1. Q: This organ removes excess glucose from the blood & stores it as glycogen | A: Liver | Cat: SCIENCE
 2. Q: This large mammal is known for its long trunk used for drinking and grabbing food | A: Elephant | Cat: ANIMALS
 3. Q: It's the only living mammal in the order Proboscidea | A: Elephant | Cat: ANIMALS
 4. Q: The gavial looks very much like a crocodile except for this bodily feature | A: the nose or snout | Cat: ANIMALS
 5. Q: In 1953 Watson & Crick built a model of the molecular structure of this, the gene‑carrying substance | A: DNA | Cat: SCIENCE
 6. Q: This element has the atomic number 79 and is a precious yellow metal | A: Gold | Cat: SCIENCE
 7. Q: This planet is known as the Red Planet | A: Mars | Cat: SCIENCE
 8. Q: He painted the Mona Lisa | A: Leonardo da Vinci | Cat: ART
 9. Q: The capital city of Japan | A: Tokyo | Cat: GEOGRAPHY
 10. Q: The author of 'Romeo and Juliet' | A: William Shakespeare | Cat: LITERATURE

🔍 Query: animal with long trunk
→ Elephant (Q: This large mammal is known for its long trunk used for drinking and grabbing food) dist=0.4234

🔍 Query: organ that stores glycogen
→ Liver (Q: This organ removes excess glucose from the blood & stores it as glycogen) dist=0.4063
🔒 Closed
```

This script connects to a **cloud-hosted Weaviate instance** and demonstrates Jeopardy-style semantic Q&A search.

---

## 📑 References

* Weaviate Database Documentation:[https://docs.weaviate.io/weaviate](https://docs.weaviate.io/weaviate)
* Weaviate Cloud Documentation: [https://docs.weaviate.io/cloud](https://docs.weaviate.io/cloud)
* Concepts and Architecture: [https://docs.weaviate.io/weaviate/concepts](https://docs.weaviate.io/weaviate/concepts)
* Model Integrations:[https://docs.weaviate.io/weaviate/model-providers](https://docs.weaviate.io/weaviate/model-providers)
* API Reference:[https://docs.weaviate.io/weaviate/config-refs](https://docs.weaviate.io/weaviate/config-refs)
* Installation Guides:[https://docs.weaviate.io/deploy/installation-guides](https://docs.weaviate.io/deploy/installation-guides)
