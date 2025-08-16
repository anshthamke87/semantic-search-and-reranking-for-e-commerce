# Three-Stage Semantic Search Pipeline for E-commerce

## 🎯 Project Overview

This project implements a **production-ready three-stage retrieval pipeline** for e-commerce product search, demonstrating the progression from traditional lexical matching to modern semantic understanding and fine-grained reranking.

## 🏗️ Architecture

```
Query → BM25 Baseline → Semantic Retrieval → Cross-Encoder Reranking → Final Results
        (Lexical)      (Bi-encoder + FAISS)    (Fine-grained scoring)
```

## 📊 Performance Results

| Stage | nDCG@10 | Improvement | Latency |
|-------|---------|-------------|---------|
| **BM25 Baseline** | 0.0025 | - | ~26ms |
| **+ Semantic Retrieval** | 0.0031 | **+24.9%** | ~7ms |
| **+ Cross-Encoder** | 0.0034 | **+9.1%** | ~25ms |
| **Total Improvement** | | **+36.3%** | |



## 🚀 Quick Start

### Option 1: Using Python Scripts (Recommended for automation)
```bash
# Clone the repository
git clone https://github.com/anshthamke87/semantic-search-and-reranking-for-e-commerce.git
cd semantic-search-and-reranking-for-e-commerce

# Install dependencies
pip install -r requirements.txt

# Run individual phases
python scripts/01_setup_and_data.py      # Data preparation
python scripts/02_bm25_baseline.py       # BM25 baseline (CPU)
python scripts/03_semantic_retrieval.py  # Semantic retrieval (GPU recommended)
python scripts/04_cross_encoder_reranking.py  # Cross-encoder reranking (GPU recommended)

# Or run complete pipeline
make pipeline

# Start demo
streamlit run app/app.py
```

### Option 2: Using Jupyter Notebooks (Recommended for learning)
```bash
# Open in Google Colab or Jupyter
notebooks/01_setup_and_data.ipynb
notebooks/02_bm25_baseline.ipynb
notebooks/03_semantic_retrieval.ipynb
notebooks/04_cross_encoder_reranking.ipynb
notebooks/05_demo_and_documentation.ipynb
```

### Option 3: Using Docker
```bash
# Build and run
docker build -t semantic-search-pipeline .
docker run -p 8000:8000 semantic-search-pipeline
```

## 📁 Project Structure

The repository works with **relative paths** and can be run from any location:
- Scripts automatically detect project root directory
- All paths are relative to project root
- Works in Google Colab, local Jupyter, or command line


## 🔧 Technical Implementation

### Stage 1: BM25 Baseline
- **Algorithm:** BM25Okapi with default parameters
- **Implementation:** `rank-bm25` library
- **Purpose:** Establish lexical matching baseline

### Stage 2: Semantic Retrieval
- **Model:** `all-MiniLM-L6-v2` bi-encoder
- **Index:** FAISS HNSW (M=32, efConstruction=200, efSearch=64)
- **Purpose:** Capture semantic similarity and query intent

### Stage 3: Cross-Encoder Reranking
- **Model:** `ms-marco-MiniLM-L-6-v2` cross-encoder
- **Depth:** Top-50 candidates reranked
- **Purpose:** Fine-grained relevance scoring

## 📁 Project Structure

```
semantic-search/
├── notebooks/
│   ├── 01_setup_and_data.ipynb
│   ├── 02_bm25_baseline.ipynb
│   ├── 03_semantic_retrieval.ipynb
│   ├── 04_cross_encoder_reranking.ipynb
│   └── 05_demo_and_documentation.ipynb
├── data/
│   ├── queries.csv (800 queries)
│   ├── corpus.csv (20000 products)
│   └── qrels.csv (32062 judgments)
├── runs/
│   ├── bm25.trec
│   ├── bi_encoder_ann.trec
│   └── cross_encoder_rerank.trec
├── reports/
│   ├── bm25_baseline_metrics.json
│   ├── semantic_retrieval_metrics.json
│   ├── cross_encoder_metrics.json
│   └── comprehensive_analysis.html
└── indices/
    ├── faiss_hnsw/
    └── corpus_embeddings.npy
```

## 🚀 Reproduction Instructions

### Environment Setup
```bash
# Use Google Colab with T4 GPU
pip install sentence-transformers faiss-gpu ir_measures rank-bm25
```

### Running the Pipeline
1. **Phase 1:** Data preparation and baseline establishment
2. **Phase 2:** BM25 baseline implementation (CPU runtime)
3. **Phase 3:** Semantic retrieval with bi-encoder + FAISS (GPU runtime)
4. **Phase 4:** Cross-encoder reranking (GPU runtime)
5. **Phase 5:** Demo and documentation

### Key Configuration
```yaml
bm25:
  top_k: 500

bi_encoder:
  model_name: "all-MiniLM-L6-v2"
  batch_size: 64
  top_k: 100

faiss:
  M: 32
  efConstruction: 200
  efSearch: 64

cross_encoder:
  model_name: "cross-encoder/ms-marco-MiniLM-L-6-v2"
  batch_size: 32
  top_k: 50
```

## 🎯 Key Achievements

✅ **36.3% improvement** in nDCG@10 over BM25 baseline  
✅ **Production-ready latency** (sub-30ms per query)  
✅ **100% query coverage** across all stages  
✅ **Memory efficient** implementation (~60MB total)  
✅ **GPU optimized** for encoding and reranking  
✅ **Comprehensive evaluation** with standard IR metrics  

## 📊 Ablation Study

Each stage contributes meaningful improvements:
- **BM25 → Semantic:** +24.9% (semantic understanding)
- **Semantic → Cross-Encoder:** +9.1% (fine-grained relevance)
- **Total Pipeline:** +36.3% (compound improvements)

## 📈 Evaluation Metrics

- **Primary:** nDCG@10, nDCG@20
- **Secondary:** MAP, MRR, P@10, Recall@100
- **Framework:** ir_measures (standard IR evaluation)
- **Dataset:** Synthetic e-commerce with realistic relevance distribution

## 🔗 References

- BM25: Robertson & Zaragoza (2009)
- Sentence-BERT: Reimers & Gurevych (2019)
- FAISS: Johnson et al. (2017)
- MS MARCO: Nguyen et al. (2016)

## 👨‍💻 Author

Ansh Thamke - Implementation of three-stage semantic search pipeline for e-commerce applications.
