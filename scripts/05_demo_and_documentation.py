#!/usr/bin/env python3
"""
05_demo_and_documentation.py - Interactive demo and documentation
Three-Stage Semantic Search Pipeline

Usage: python scripts/05_demo_and_documentation.py
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
import json

def main():
    """Main execution function for Phase 5"""
    print("🚀 Phase 5: Demo and Documentation")
    
    # Check if results exist
    results_files = [
        f"{PROJECT_DIR}/reports/bm25_baseline_metrics.json",
        f"{PROJECT_DIR}/reports/semantic_retrieval_metrics.json", 
        f"{PROJECT_DIR}/reports/cross_encoder_metrics.json"
    ]
    
    missing_files = [f for f in results_files if not os.path.exists(f)]
    
    if missing_files:
        print("❌ Some result files not found:")
        for f in missing_files:
            print(f"   - {f}")
        print("💡 Please run all previous phases first")
        return 1
    
    print("📊 Loading performance results...")
    print("📈 Demo setup would run here...")
    print("💡 For interactive demo, run: streamlit run app/app.py")
    print("💡 For full documentation, run: notebooks/05_demo_and_documentation.ipynb")
    
    print("✅ Phase 5 template completed!")
    print("🎉 Project documentation ready!")
    
    return 0

if __name__ == "__main__":
    exit(main())
