
# Student Performance Prediction API 🎓

A Machine Learning–powered REST API built using **FastAPI** that predicts student performance based on input features. This project showcases a complete ML pipeline — from data processing and model training to API deployment.

---

## 🚀 Features

- Predict student performance using a trained ML model  
- FastAPI-based RESTful API  
- Interactive Swagger UI (`/docs`)  
- Model training via Jupyter Notebook  
- Modular project structure  
- Ready for cloud deployment  
- Unit testing support  

---

## 🧰 Tech Stack

- Python  
- FastAPI  
- Scikit-Learn  
- Uvicorn  
- Jupyter  
- Pytest  

---

## 📁 Project Structure

student-performance-api/
├── app/                # Main FastAPI application
├── model/              # Trained ML model
├── notebooks/          # Jupyter notebooks for training
├── templates/          # HTML templates (if used)
├── tests/              # Unit test cases
├── requirements.txt   # Project dependencies
├── Dockerfile          # Docker configuration
└── README.md           # Project documentation
└── README.md

---

## ✅ Prerequisites

- Python 3.8+
- pip

---

## 🛠️ Installation

git clone https://github.com/AdarshKosare/student-performance-api.git  
cd student-performance-api  
python -m venv env  
env\Scripts\activate  
pip install -r requirements.txt  

---

## 🚄 Running the API

uvicorn app.main:app --reload  

Open: http://127.0.0.1:8000/docs

---

## 📊 API Example

Input:
{
  "study_hours": 10
  "previous_score": 80
  "sleep_hours": 8
  "practiced_sample_paper_count": 15
  "extracurricular_activities": Yes
}

Output:
{
  "predicted_score": 83.2
}

---

## 📝 Model Training

notebooks/train_model.ipynb

---

## 🤝 Contribution

Fork → Branch → Commit → Pull Request

---

## 📄 License

MIT License

---

## 👤 Author

Adarsh Kosare  
GitHub: https://github.com/AdarshKosare
