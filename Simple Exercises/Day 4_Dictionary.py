student = {
    "name": "Deblin",
    "age": 39,
    "role": "PL SQL Engineer"
}

del student["age"]
student["experience"]=16

print(student["name"])
print(student.get("age"))
print(student.get("role"))
print(student["experience"])


a, b = 10, 3

operations = {
    "total": lambda x, y: x + y,
    "difference": lambda x, y: x - y,
    "product": lambda x, y: x * y,
    "division": lambda x, y: x / y,
    "remainder": lambda x, y: x % y
}

for op_name, func in operations.items():
    result = func(a, b)
    print(f"{op_name.capitalize()}: {result}")


models = {
    "model_A": 0.82,
    "model_B": 0.76,
    "model_C": 0.91
}

# Loop through models and print "Deploy" if >=0.8 else "Reject"

for model,val in models.items():
    if val >= 0.8:
        print("Deploy")
    else:
        print("Reject")


config = {
    "prod": {"logging": True, "monitoring": True},
    "dev": {"logging": True, "monitoring": False}
}

# Loop through config and print settings for each environment
for env, settings in config.items():
    print(f"Environment: {env}")
    print(f"  Logging enabled: {settings['logging']}")
    print(f"  Monitoring enabled: {settings['monitoring']}")



models = {"model_X": 0.79, "model_Y": 0.83}
# loop with while until all models reach >= 0.8

threshold = 0.8
attempt = 1
max_attempts = 5

while not all ( score >= threshold for score in models.values()) and attempt < max_attempts:
    for model, score  in models.items():
        if score  <  threshold:
            models [model] = score  + 0.1
    attempt += 1


for model, score in models.items():
    print(f"{model}: {score}")


