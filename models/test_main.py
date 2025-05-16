import pytest
from fastapi.testclient import TestClient
from main import app
import os
from transformers import pipeline

@pytest.fixture(scope="module")
def test_client():
    # Setup test client with model loaded
    model_name = os.getenv("MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
    pipe = pipeline("sentiment-analysis", model=model_name)
    
    # Override the app's pipe for testing
    app.state.pipe = pipe
    
    with TestClient(app) as client:
        yield client

def test_homepage_get(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert "<form" in response.text


def test_analyze_post_api(test_client):
    test_cases = [
        ("I love this product!", "POSITIVE"),
        ("I hate this product!", "NEGATIVE"),
        ("Hey","NEUTRAL")
        
    ]
    
    for text, expected_sentiment in test_cases:
        response = test_client.post("/api/analyze", json={"text": text})
        assert response.status_code == 200
        json_data = response.json()
        assert "text" in json_data
        assert "sentiment" in json_data
        assert "confidence" in json_data
        if expected_sentiment=="POSITIVE":
            expected_sentiment="POS"
        elif expected_sentiment=="NEGATIVE":
            expected_sentiment="NEG"
        else:
            expected_sentiment="NEU"
        assert json_data["text"] == text
        assert json_data["sentiment"] == expected_sentiment
        

