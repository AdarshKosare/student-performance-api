from pydantic import BaseModel

class PredictionRequest(BaseModel):
    # Define your input features here
    study_hours: int
    previous_score: int
    sleep_hours: float
    practiced_sample_paper_count: int
    extracurricular_activities: bool
    # ...
