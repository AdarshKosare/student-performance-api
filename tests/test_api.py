from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction():
    response = client.post("/predict",
      json={
         "study_hours": 7,
         "previous_score": 70,
         "sleep_hours": 7,
         "practiced_sample_paper_count": 2,
         "extracurricular_activities": 1
      }
    )
    assert response.status_code == 200
