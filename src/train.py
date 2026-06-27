import os
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_model():
    data = {
        "years_of_experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "promotion_status": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    }

    df = pd.DataFrame(data)

    X = df[["years_of_experience"]]
    y = df["promotion_status"]

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")

    print("Model trained and saved successfully.")

if __name__ == "__main__":
    train_model()