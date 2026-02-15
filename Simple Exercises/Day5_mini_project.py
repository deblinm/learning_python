CONFIG = {
    "threshold": 0.8,
    "max_attempts": 3,
    "improvement_step": 0.03
}

models = {
    "fraud_model": 0.76,
    "risk_model": 0.81,
    "churn_model": 0.78
}

def all_models_pass(models, threshold):
    return all(score >= threshold for score in models.values())

attempt = 1

while not all_models_pass(models, CONFIG["threshold"]) and attempt <= CONFIG["max_attempts"]:
    print(f"\nAttempt {attempt}")

    for model, score in models.items():
        if score < CONFIG["threshold"]:
            print(f"Retraining {model} (accuracy={score})")
            models[model] = round(score + CONFIG["improvement_step"], 3)

    attempt += 1

print("\nFinal Model Scores:")
for model, score in models.items():
    print(f"{model}: {score}")

if all_models_pass(models, CONFIG["threshold"]):
    print("\n✅ Deploy all models")
else:
    print("\n❌ Deployment blocked")
