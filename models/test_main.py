import pytest
from fastapi.testclient import TestClient

from main import app, pipe
from transformers import pipeline as hf_pipeline
import os

# Ensure model is loaded manually for test purposes
@pytest.fixture(scope="session", autouse=True)
def load_model_for_test():
    global pipe
    if pipe is None:
        model_name = os.getenv("MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
        pipe = hf_pipeline("sentiment-analysis", model=model_name)
    return pipe


client = TestClient(app)

def test_homepage_get():
    response = client.get("/")
    assert response.status_code == 200
    assert "<form" in response.text  # check if HTML form is rendered

def test_analyze_post_html():
    response = client.post("/", data={"text": "I love this product!"})
    assert response.status_code == 200
    assert "label" in response.text or "Positive" in response.text or "NEGATIVE" in response.text

def test_analyze_post_api():
    response = client.post("/api/analyze", json={"text": "I love this product!"})
    assert response.status_code == 200
    json_data = response.json()
    assert "sentiment" in json_data
    assert "confidence" in json_data
    assert json_data["sentiment"] in ["POSITIVE", "NEGATIVE"]
    assert 0.0 <= json_data["confidence"] <= 1.0

def test_invalid_model():
    from main import pipe
    if pipe is None:
        pytest.skip("Model is not loaded, skipping test.")
