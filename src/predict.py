import joblib
import pandas as pd

def predict_promotion(years_of_experience):
    model = joblib.load("model/model.pkl")

    input_data = pd.DataFrame(
        [[years_of_experience]],
        columns=["years_of_experience"]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "Promoted"
    return "Not Promoted"