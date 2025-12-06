import joblib

def load_models():
    linear = joblib.load("model/linear_model.pkl")
    lasso = joblib.load("model/lasso_model.pkl")
    ridge = joblib.load("model/ridge_model.pkl")
    return linear, lasso, ridge
