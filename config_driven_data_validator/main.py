import json
import pandas as pd
import validator.engine as e

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
    output = e.run_validation(df, config_data)

    print("Summary:")
    print(output["summary"])

    print("\nDetailed Results:")
    for r in output["results"]:
        print(r)

    # Production enforcement
    e.enforced_pipeline(output["summary"], config_data)


if __name__ == "__main__":
    main()