import pandas as pd
import json

def validate_data(df,config_data):
    results = []


    # Check required columns
    required_columns = config_data.get("required_columns")
    for val in required_columns:
        if val not in df.columns:
            rule = {"rule": "required_columns",
                    "status": "fail",
                    "message": f"Missing '{val}'",
                    "severity": "critical"}
            results.append(rule)


    # # Check age range
    #
    severity = config_data["rules"]["age"]["severity"]
    age_range = df[(df["age"] < config_data["rules"]["age"]["min"]) | (df["age"] > config_data["rules"]["age"]["max"]) | (df["age"].isnull())]
    if not age_range.empty:
         for index,row in age_range.iterrows():
             invalid_age= row["age"]
             rule = {"rule":"age_range",
                     "status":"fail",
                     "message":f"Out of age range '{invalid_age}'",
                     "severity": f"{severity}"}
             results.append(rule)
    # Check salary
    severity = config_data["rules"]["salary"]["severity"]
    salary_range = config_data["rules"]["salary"]["min"]
    invalid_salary = df[(df["salary"] < salary_range) | (df["salary"].isnull()) ]
    if not invalid_salary.empty:
        for index,row in invalid_salary.iterrows():
            invalid_sal = row["salary"]
            rule = {"rule": "check_salary",
                    "status": "fail",
                    "message": f"Out of salary range '{invalid_sal}'",
                    "severity": f"{severity}"}
            results.append(rule)
    # Check allowed countries
    severity = config_data["rules"]["country"]["severity"]
    required_countries = config_data["allowed_countries"]
    invalid_countries = df[~df["country"].isin(required_countries)]
    if not invalid_countries.empty:
        for index,row in invalid_countries.iterrows():
            invalid_cntry = row["country"]
            rule = {"rule": "country_allowed",
                    "status": "fail",
                    "message": f"Row {index+1} has invalid country '{invalid_cntry}'",
                    "severity": f"{severity}"}
            results.append(rule)
    return results


data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [25, None, 40, 17, 65],
    "salary": [50000, 60000, None, 30000, -120000],
    "country": ["US", "IND", "CA", "MX", None]
}

with open('my_config.json', 'r') as f:
    config_data = json.load(f)

df = pd.DataFrame(data)
validator = validate_data(df,config_data)
print(validator)


for result in validator:
    if result["status"] == "fail" and result["severity"] == "critical":
        if config_data["env"] == "prod":
            raise Exception(f"Critical validation failed: {result['message']}")
    elif result["status"] == "fail":
        print(f"Warning: {result['message']}")