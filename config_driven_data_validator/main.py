import json
import pandas as pd
from validator.validation_rules import QualityChecker

def load_data():
    data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [25, None, 40, 17, 65],
    "salary": [50000, 60000, None, 30000, -120000],
    "country": ["US", "IND", "CA", "MX", None]
}

    df = pd.DataFrame(data)
    return df


def load_config(path):
    with open (path,"r") as f:
        return json.load(f)


def main():
    config_data = load_config("config/sample_config.json")
    df = load_data()
    checker = QualityChecker(df, config_data)
    results = checker.run_rules()

    print("Summary:", results["summary"])
    if results["summary"]["high_severity_failures"] > 0:
        print("Pipeline FAILED due to high severity issues.")
    else:
        print("Pipeline PASSED.")

if __name__ == "__main__":
    main()