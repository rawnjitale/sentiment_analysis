# Sentiment Analysis API with FastAPI

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green)](https://fastapi.tiangolo.com)
[![Transformers](https://img.shields.io/badge/Transformers-4.0+-orange)](https://huggingface.co/transformers)

A production-ready sentiment analysis API with web interface, built with FastAPI and Hugging Face Transformers.

## Features

- 🚀 FastAPI backend with async support
- 🤗 Hugging Face Transformers for sentiment analysis
- 🌐 Web interface and REST API endpoints
- ✅ Comprehensive test coverage with pytest
- 🔄 Automatic model loading with lifespan events
- 📊 Confidence scores with predictions

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Steps
- Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-api.git
   cd sentiment-analysis-api
- Create an virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

- Install dependencies:
   ```bash
    pip install -r requirements.txt
- (Optional) Hugging face model in .env file as MODEL_NAME
- Runnig an Application 
    ```bash
    python3 main.py or python main.py (Depending upon your usecase) 

- Open server at ```http://127.0.0.1:8000/```
- Thank you for reading.
