#!/usr/bin/env python3
"""
02_bm25_baseline.py - BM25 baseline implementation
Three-Stage Semantic Search Pipeline

Prerequisites: Run 01_setup_and_data.py first
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
from rank_bm25 import BM25Okapi
import ir_measures
from ir_measures import *
import time
import yaml

def main():
    """Main execution function for Phase 2"""
    print("🚀 Phase 2: BM25 Baseline Implementation")
    
    # Check if data exists
    if not os.path.exists(f"{PROJECT_DIR}/data/queries.csv"):
        print("❌ Data files not found!")
        print("💡 Please run: python scripts/01_setup_and_data.py first")
        print("📔 Or run the notebook: notebooks/01_setup_and_data.ipynb")
        return 1
    
    # Load dataset
    queries_df = pd.read_csv(f"{PROJECT_DIR}/data/queries.csv")
    corpus_df = pd.read_csv(f"{PROJECT_DIR}/data/corpus.csv")
    
    print(f"📂 Loaded {len(queries_df)} queries and {len(corpus_df)} products")
    
    # Load configuration
    with open(f"{PROJECT_DIR}/cfg/retrieval.yaml", 'r') as f:
        config = yaml.safe_load(f)
    
    print("🔍 BM25 implementation would run here...")
    print("💡 For full BM25 implementation, please run: notebooks/02_bm25_baseline.ipynb")
    print("📁 Results should be saved to: runs/bm25.trec")
    
    print("✅ Phase 2 template completed!")
    print("🚀 Ready for Phase 3: Semantic Retrieval")
    
    return 0

if __name__ == "__main__":
    exit(main())
