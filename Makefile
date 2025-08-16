# Makefile for Three-Stage Semantic Search Pipeline

.PHONY: help install setup-data bm25 semantic cross-encoder demo clean test

help:
	@echo "Three-Stage Semantic Search Pipeline"
	@echo "====================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install        - Install all dependencies"
	@echo "  make setup-data     - Run Phase 1: Data preparation"
	@echo "  make bm25          - Run Phase 2: BM25 baseline"
	@echo "  make semantic      - Run Phase 3: Semantic retrieval (requires GPU)"
	@echo "  make cross-encoder - Run Phase 4: Cross-encoder reranking (requires GPU)"
	@echo "  make demo          - Run Phase 5: Interactive demo"
	@echo "  make pipeline      - Run complete pipeline (Phases 1-4)"
	@echo "  make clean         - Clean generated files"

install:
	pip install -r requirements.txt
	@echo "✅ Dependencies installed"

setup-data:
	@echo "🔧 Running Phase 1: Data preparation..."
	python scripts/01_setup_and_data.py
	@echo "✅ Phase 1 completed"

bm25:
	@echo "🔍 Running Phase 2: BM25 baseline..."
	python scripts/02_bm25_baseline.py
	@echo "✅ Phase 2 completed"

semantic:
	@echo "🧠 Running Phase 3: Semantic retrieval..."
	python scripts/03_semantic_retrieval.py
	@echo "✅ Phase 3 completed"

cross-encoder:
	@echo "🎯 Running Phase 4: Cross-encoder reranking..."
	python scripts/04_cross_encoder_reranking.py
	@echo "✅ Phase 4 completed"

demo:
	@echo "🎮 Running Phase 5: Interactive demo..."
	streamlit run app/app.py
	@echo "✅ Demo started"

pipeline: setup-data bm25 semantic cross-encoder
	@echo "🚀 Complete pipeline execution finished!"

clean:
	@echo "🧹 Cleaning generated files..."
	rm -rf runs/*.trec reports/*.json reports/*.png indices/*
	@echo "✅ Cleanup completed"
