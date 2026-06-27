import os
from src.train import train_model
from src.predict import predict_promotion

def test_model_file_exists():
    train_model()
    assert os.path.exists("model/model.pkl")

def test_employee_promoted():
    train_model()
    result = predict_promotion(7)
    assert result == "Promoted"