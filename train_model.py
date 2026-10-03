import pandas as pd
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

print("Dataset loaded successfully!")
print(data)

# Simple quality prediction logic
def predict_quality(loc, bugs, complexity, coverage, duplication):

    score = 100

    # Bugs
    score -= bugs * 1.2

    # Complexity
    score -= complexity * 1.5

    # Test coverage
    score += (coverage - 70) * 0.5

    # Duplication
    score -= duplication * 1.0

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    if score >= 75:
        quality = "High"
    elif score >= 50:
        quality = "Medium"
    else:
        quality = "Low"

    return round(score, 2), quality


# Test prediction
score, quality = predict_quality(
    2500,   # LOC
    12,     # Bugs
    11,     # Complexity
    80,     # Test Coverage
    6       # Duplication
)

print("\nAI Software Quality Prediction")
print("--------------------------------")
print("Quality Score :", score)
print("Quality       :", quality)