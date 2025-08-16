#!/usr/bin/env python3
"""
03_semantic_retrieval.py - Semantic retrieval with bi-encoder + FAISS
Three-Stage Semantic Search Pipeline

Prerequisites: 
- Run 01_setup_and_data.py first
- Run 02_bm25_baseline.py
- Requires GPU for optimal performance
"""


import os
from pathlib import Path

def get_project_root():
    """Get project root directory (works from anywhere in the project)"""
    current_file = Path(__file__).resolve()
    
    # If running from scripts/ directory, go up one level
    if current_file.parent.name == 'scripts':
        return current_file.parent.parent
    # If running from project root
    else:
        return current_file.parent

# Set project directory dynamically
PROJECT_DIR = str(get_project_root())
print(f"📁 Project directory: {PROJECT_DIR}")

# Create directories if they don't exist
os.makedirs(f"{PROJECT_DIR}/data", exist_ok=True)
os.makedirs(f"{PROJECT_DIR}/reports", exist_ok=True)
os.makedirs(f"{PROJECT_DIR}/runs", exist_ok=True)
os.makedirs(f"{PROJECT_DIR}/indices", exist_ok=True)
os.makedirs(f"{PROJECT_DIR}/cfg", exist_ok=True)


import pandas as pd
import numpy as np
import torch

def main():
    """Main execution function for Phase 3"""
    print("🚀 Phase 3: Semantic Retrieval Implementation")
    
    # Check GPU availability
    print(f"🔥 GPU Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"🎯 GPU Device: {torch.cuda.get_device_name(0)}")
    
    # Check if data exists
    if not os.path.exists(f"{PROJECT_DIR}/data/queries.csv"):
        print("❌ Data files not found!")
        print("💡 Please run the previous phases first")
        return 1
    
    # Load dataset
    queries_df = pd.read_csv(f"{PROJECT_DIR}/data/queries.csv")
    corpus_df = pd.read_csv(f"{PROJECT_DIR}/data/corpus.csv")
    
    print(f"📂 Loaded {len(queries_df)} queries and {len(corpus_df)} products")
    
    print("🧠 Semantic retrieval implementation would run here...")
    print("💡 For full implementation, please run: notebooks/03_semantic_retrieval.ipynb")
    print("📁 Results should be saved to: runs/bi_encoder_ann.trec")
    
    print("✅ Phase 3 template completed!")
    print("🚀 Ready for Phase 4: Cross-Encoder Reranking")
    
    return 0

if __name__ == "__main__":
    exit(main())
