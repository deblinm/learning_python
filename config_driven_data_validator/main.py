import json
import pandas as pd
import validator.engine as e


data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [25, None, 40, 17, 65],
    "salary": [50000, 60000, None, 30000, -120000],
    "country": ["US", "IND", "CA", "MX", None]
}

df = pd.DataFrame(data)

with open("config/sample_config.json","r") as conf:
    config = json.load(conf)

output = e.run_validation(df, config)

print("Summary:")
print(output["summary"])

print("\nDetailed Results:")
for r in output["results"]:
    print(r)


# Production enforcement
e.enforced_pipeline(output["summary"], config)