# **Semantic AI search with Vector Databases**

**Companion GitHub repository and code for the book**

*Author: Amol Bhoite* — First Edition (2025) — ISBN: 978-93-343-5251-1

---

## What this repo is?

This GitHub repository contains the **companion code, labs, datasets, diagrams and deployment recipes** for the book  *Semantic AI Search with Vector Databases* . The book explains vector embeddings, ANN indexes, RAG architectures and production patterns — and this repo lets you run the hands‑on examples, reproduce the case studies, and experiment with multiple vector engines.

**Scan the QR / barcode in the printed/eBook to open the repository** , or visit the companion link embedded in the book: `https://github.com/bhoitea/ai-vector-databases`.

---

## About the Book — high level

*Semantic AI Search with Vector Databases* is a practical, example-driven guide to building semantic search, RAG (Retrieval-Augmented Generation) systems and AI-native data infrastructure. The book walks from fundamentals (what vectors and embeddings are) through internals (indexing, distance metrics, compression) to ecosystem deep-dives and full production case studies. It is written to be accessible for beginners while also providing depth for engineers, and architects.

**Who this is for** : Engineers, architects, DBAs, DevOps, solution architects, ML/AI practitioners, and decision-makers evaluating vector-powered systems.

---

## What you will find in this repository

This repo mirrors the structure of the book and includes:

* **Chapter folders** with code labs and example scripts (embedding loaders, ingestion scripts, index builders, query examples).
* **Docker / docker-compose** files to bring up local deployments of vector engines used in the book (Milvus, Qdrant, Weaviate, Redis + Redis‑Vector, etc.).
* **Sample datasets** and pre-computed embeddings for quicker experimentation.
* **Notebooks** and small demos (Python) demonstrating end-to-end RAG flows and LLM orchestration.
* **Architecture diagrams** and runbooks for production deployments (sharding, replication, monitoring).
* **Tests & small benchmarks** used in the chapters for reproducible performance experiments.
* **README files per chapter** that explain how to run each lab, prerequisites, and expected output.

The PDF/eBook explicitly points readers to "All code examples, datasets, and labs" at the companion repository.

---

## Repo Layout

```warp-runnable-command
ai-vector-databases/                       # root of this companion repo
├── pure-vector-databases/                 # Pinecone, Weaviate, Milvus, Qdrant, Chroma, ...
│   ├── Chapter1-Pinecone/
│   ├── Chapter2-Weaviate/
│   ├── Chapter3-Milvus/
│   ├── Chapter4-Qdrant/
│   ├── Chapter5-Chroma/
├── vector-stores/                         # pgvector (Postgres/Yugabyte), Redis, SQLite VSS, 
│   ├── Chapter1-PostgreSQL_pgvector/
│   ├── Chapter2-YugabyteDB_pgvector/
│   └── Chapter4-Redis_Vector/
└── README.md                              # this file
```

---

## What the book covers

The book is structured across multiple parts — foundations, internals, ecosystem deep dives, RAG architecture, case studies, and advanced topics. Representative chapter headings include (excerpted from the book's table of contents):

* The AI Era and the Rise of Unstructured Data
* What Is a Vector? How Embeddings Work
* Anatomy of a Vector Database — inside the engine room
* Similarity metrics, Indexing algorithms (HNSW, IVF, PQ), Compression & Scaling
* Vector Stores vs. Pure Vector Databases — deep dives: pgvector, YugabyteDB, Milvus, Qdrant, Chroma, Pinecone, Weaviate, FAISS, Marqo, Vespa, Vald, etc.
* RAG architectures, tuning, anti-patterns, and industry case studies (legal, healthcare).

---

## Important book metadata

* **Title:** Semantic AI Search with Vector Databases
* **Author:** Amol Bhoite
* **Edition:** First Edition, Version 1.0 (2025)
* **ISBN:** 978-93-343-5251-1
* **Contact:** https://www.linkedin.com/in/amolbhoite/

---

## How the barcode / QR works

The eBook and printed book include a scannable link that takes you to the companion GitHub repository (visible in the PDF as "Scan to open GitHub Repository"). If you don't have a scanner:

* Use your phone camera (iOS/Android) on the QR — modern camera apps detect QR codes automatically.
* Install a QR reader app or use an online QR decoder (upload a screenshot) if your camera doesn't detect it.
* If scanning fails, the raw link printed next to the code is `https://github.com/bhoitea/ai-vector-databases`.

---

## Why this repo exists

* **Run the exact code from the book** — no retyping. All ingestion scripts, index builders, and query examples are included so you can learn by doing.
* **Compare engines** — the book shows trade-offs across pure vector DBs and vector stores; the repo contains reproducible experiments and small benchmarks.
* **Production guidance** — runbooks, diagrams and notes on sharding, failover, and monitoring help turn prototypes into production.

---

**Enjoy building semantic, meaning-driven systems — one vector at a time.**
