# Chapter 3 - Milvus + Zilliz Cloud Demo

This repository demonstrates how to use **Milvus** for vector similarity search,
both in a **self-hosted setup (Docker)** and in **Zilliz Cloud (managed Milvus)**.

## 📂 Project Structure

```
Chapter3-Milvus/
├── README.md
├── requirements.txt
└── scripts/
    ├── milvus-selfhosted-demo.py
    └── zillizcloud-demo.py
```

---

## **Install Milvus in Docker**

Run the following commands:

```
pip install -U pymilvus
```

Download Milvus standalone script

```
curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh
```

Start Milvus. This script runs Docker containers (Milvus standalone + dependencies).

```
bash standalone_embed.sh start
```

If you encounter a **Docker mount permission error** like:

```
docker: Error response from daemon: error while creating mount source path ... permission denied.
```

✅  **Fix (macOS Docker Desktop users)** :

Switch file-sharing to **gRPC-FUSE**

* Open **Docker Desktop → Settings → General**
* Enable **Use gRPC-FUSE for file sharing**
* Apply and **Restart Docker**

Then run:

```
mkdir -p ~/milvus/volumes
chmod -R 777 ~/milvus/volumes
bash standalone_embed.sh start
```

If successful, you should see:

Wait for Milvus Starting...
Start successfully.

📌  **Default configuration after startup** :

* **Milvus Server** : `localhost:19530`
* **Embedded etcd** : port `2379`
* **Data volume** : `~/milvus/volumes`
* **WebUI** : [http://127.0.0.1:9091/webui/](http://127.0.0.1:9091/webui/)

---

## 🚀 Self-hosted Demo

Run the Python demo:

```bash
python milvus-selfhosted-demo.py
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

This script will:

- Create a collection with embeddings
- Insert sample data
- Run similarity search queries

---

## ☁️ Zilliz Cloud Setup

1. Sign up at [https://zilliz.com/cloud](https://zilliz.com/cloud)
2. Create a free cluster
3. Copy the **API key** and **endpoint**
4. Update the values in `zillizcloud-demo.py`

Run the demo:

```bash
python zillizcloud-demo.py
```

**Expected Output**

```
✅ Inserted 8 recipes:
• ID 1: Spaghetti Pomodoro with tomato, basil, garlic
• ID 2: Tomato Basil Soup rich and creamy
• ID 3: Garlic Bread with butter and herbs
• ID 4: Pesto Pasta with basil, pine nuts, parmesan
• ID 5: Margherita Pizza with tomato, basil, mozzarella
• ID 6: Chicken Alfredo pasta with parmesan and cream
• ID 7: Caprese Salad with tomato, basil, mozzarella
• ID 8: Garlic Shrimp Linguine with parsley and lemon
Collection indexed & loaded
🔍 Query: basil tomato chicken pasta
🔢 Vector sample: [np.float64(-0.0153), np.float64(0.0454), np.float64(0.0268), np.float64(-0.0317), np.float64(-0.0508)]

📊 Top 3 Search Results:
• ID 4, Title: Pesto Pasta with basil, pine nuts, parmesan, Distance: 0.7422

```

This script will:

- Use the default embedding function
- Insert and query vectors
- Demonstrate semantic search

---

## 🗂 References

- Milvus open-source database: [https://milvus.io/docs/overview.md](https://milvus.io/docs/overview.md)
- Zilliz Cloud(fully managed Milvus cloud): [https://docs.zilliz.com/docs/home](https://docs.zilliz.com/docs/home)
- Integrations: [https://milvus.io/docs/integrations_overview.md](https://milvus.io/docs/integrations_overview.md)
