accuracy = 0.82

# if accuracy >= 0.8 → "Model acceptable"
# else → "Model rejected"


if accuracy >= 0.8:
    print("Model acceptable")
else:
    print("Model rejected")

env = "prod"

# if env == "prod" → "Running in production"
# else → "Running in non-prod"

if env == "prod":
    print("Running in production")
else:
    print("Running in non-prod")

value = None

if value:
    print("Has value")
else:
    print("No value")
