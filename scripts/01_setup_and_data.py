#!/usr/bin/env python3
"""
01_setup_and_data.py - Data preparation and baseline establishment
Three-Stage Semantic Search Pipeline

Usage:
    python scripts/01_setup_and_data.py    # Run from project root
    python 01_setup_and_data.py            # Run from scripts/ directory
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
import random
import yaml
from tqdm import tqdm

def main():
    """Main execution function for Phase 1"""
    print("🚀 Phase 1: Setup and Data Preparation")
    
    # Set random seed for reproducibility
    RANDOM_SEED = 42
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    
    print(f"📁 Working directory: {PROJECT_DIR}")
    
    # Dataset configuration
    dataset_config = {
        'name': 'amazon_esci_synthetic',
        'target_queries': 800,
        'target_products': 20000,
        'random_seed': RANDOM_SEED,
        'min_judgments_per_query': 5,
        'max_judgments_per_query': 100
    }
    
    # Save configuration
    with open(f"{PROJECT_DIR}/cfg/dataset.yaml", 'w') as f:
        yaml.dump(dataset_config, f)
    
    # Retrieval configuration  
    retrieval_config = {
        'bm25': {'top_k': 500},
        'bi_encoder': {
            'model_name': 'all-MiniLM-L6-v2',
            'batch_size': 64,
            'top_k': 100
        },
        'faiss': {
            'index_type': 'HNSW',
            'M': 32,
            'efConstruction': 200,
            'efSearch': 64
        },
        'cross_encoder': {
            'model_name': 'cross-encoder/ms-marco-MiniLM-L-6-v2',
            'batch_size': 32,
            'top_k': 50
        }
    }
    
    with open(f"{PROJECT_DIR}/cfg/retrieval.yaml", 'w') as f:
        yaml.dump(retrieval_config, f)
    
    print("✅ Phase 1 configuration completed!")
    print("💡 Note: This is a template script converted from Jupyter notebook")
    print("📔 For full data generation, please run the original notebook: notebooks/01_setup_and_data.ipynb")
    print("📁 Dataset files should be in: data/")
    
    return 0

if __name__ == "__main__":
    exit(main())
