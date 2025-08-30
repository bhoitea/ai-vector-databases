# Qdrant Vector Search Demo

This repository demonstrates how to use **Qdrant** for semantic search with both **self-hosted** (Docker) and **Qdrant Cloud** setups.

---

## 📂 Project Structure

```
qdrant-vector-demo/
├── README.md
├── requirements.txt
├── .gitignore
└── scripts/
    ├── qdrantdemo.py        # Self-hosted Qdrant demo
    └── qdrantclouddemo.py   # Qdrant Cloud demo
```

---

## 🚀 Quick Start

### 1️⃣ Run Qdrant (Self-hosted)

```bash
docker pull qdrant/qdrant

docker run -d --name qdrant_local -p 6333:6333 -p 6334:6334 \
 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant

```

Check readiness:

```bash
curl -X GET "http://localhost:6333/healthz"
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Demo Scripts

### **Self-hosted Qdrant**

```bash
python3 scripts/qdrant-sefthosted-demo.py
```

**Expected Output**

```
Inserted ads:
- id=1: "Limited Time Offer: Grab It Before It's Gone!"
- id=2: "Discover the Secret to Ageless Beauty!"
- id=3: "Join Thousands Who Made the Smart Choice!"
- id=4: "Boost Your Skills: Top-Rated Courses Inside!"
- id=5: "Elevate Your Career: Exclusive Workshops!"
- id=6: "Unlock Your Special Discount: Click Now!"
- id=7: "Experience Luxury at a Fraction of the Cost!"
- id=8: "Turn Your Dreams into Reality: Learn How!"

Enter your search query: new offers

Searching for: "new offers"

Top matching ads:
- id=1, score=0.380: "Limited Time Offer: Grab It Before It's Gone!"
- id=6, score=0.327: "Unlock Your Special Discount: Click Now!"
- id=7, score=0.158: "Experience Luxury at a Fraction of the Cost!"
```

**Qdrant Cloud**

python3 scripts/qdrant-cloud-demo.py

```
✅ Inserted entertainment documents:
- id=64b3818e740440fd8b2d308d68566c05: "Romantic comedy movie about two unlikely lovers."
- id=3a86cdb800304ae68f3aba993ebd5bfa: "Action-packed superhero blockbuster with stunning visuals."
- id=3eb4cf73dc09461fb95d974641626768: "Documentary series exploring wildlife conservation in Africa."
- id=94df9542ab5746bfb9e44559f25e5de9: "Sci‑fi adventure set in a dystopian future city."
- id=d6c505d6d06c47b1a307208ceb93e2c9: "Animated feature film suitable for the whole family."
- id=ac1b848c2cf24bbd95ec32e145267608: "True‑crime podcast unraveling a mysterious cold case."
- id=0f0064a7516d474f818b5b0bbfce7046: "Live Broadway‑style musical with elaborate choreography."
- id=9ecd2d05cf24456fb20dd1888588d5a7: "Fantasy epic trilogy filled with magic and dragons."

Enter your entertainment search query: action movie

🔍 Searching for: "action movie"

🎯 Top matches:
- id=3a86cdb8-0030-4ae6-8f3a-ba993ebd5bfa, score=0.886: "Action-packed superhero blockbuster with stunning visuals."
- id=d6c505d6-d06c-47b1-a307-208ceb93e2c9, score=0.875: "Animated feature film suitable for the whole family."
- id=94df9542-ab57-46bf-b9e4-4559f25e5de9, score=0.834: "Sci‑fi adventure set in a dystopian future city."
```

---

## 🧑‍💻 Scripts Overview

### `scripts/qdrant-sefthosted-demo.py`

- Connects to **local Qdrant** (running in Docker).
- Creates a collection.
- Inserts sample ads dataset.
- Performs semantic similarity search with a user query.

### `scripts/qdrant-cloud-demo.py`

- Connects to **Qdrant Cloud** (requires API key & endpoint).
- Creates a collection.
- Inserts sample entertainment dataset.
- Performs semantic similarity search with a user query.

---

## 🔗 References

* Open-source database: :[https://qdrant.tech/documentation/](https://qdrant.tech/documentation/)
* Cloud documentation: [https://qdrant.tech/documentation/cloud-intro/](https://qdrant.tech/documentation/cloud-intro/)
* Github:[https://github.com/qdrant/qdrant](https://github.com/qdrant/qdrant)
* Qdrant Cloud:[https://cloud.qdrant.io/](https://cloud.qdrant.io/)
* Practical Examples: [https://qdrant.tech/articles/practicle-examples/](https://qdrant.tech/articles/practicle-examples/)**
