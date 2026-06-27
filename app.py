from flask import Flask
from src.predict import predict_promotion

app = Flask(__name__)

@app.route("/")
def home():
    result = predict_promotion(7)
    return f"Employee Result: {result}"

if __name__ == "__main__":
    app.run(debug=True)