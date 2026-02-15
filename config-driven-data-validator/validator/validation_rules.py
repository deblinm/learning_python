import  pandas as pd

def check_required_columns(df,config_data):
    results = []
    severity = config_data["rules"]["req_cols"]["severity"]
    required_columns = config_data.get('required_columns')
    for cols in required_columns:
        if cols not in df.columns:
            results.append({"rule": "required_columns",
                    "status": "fail",
                    "message": f"Missing '{cols}'",
                    "severity": f"{severity}"})
    return results

def check_age_range(df,config_data):
    results = []
    severity = config_data["rules"]["age"]["severity"]
    age_calc = df [(df["age"] > config_data["rules"]["age"]["max"]) | (df["age"] < config_data["rules"]["age"]["min"]) | (df["age"].isnull())]
    if not age_calc.empty:
        for index,row in age_calc.iterrows():
            invalid_age = row["age"]
            cust_id = row ["customer_id"]
            results.append({"rule": "age_range",
                    "status": "fail",
                    "message": f"Row {index}, customer_id={cust_id}, invalid age '{invalid_age}'",
                    "severity": f"{severity}"})
    return results

def check_salary_range(df,config_data):
    results = []
    severity = config_data["rules"]["salary"]["severity"]
    sal_min = config_data["rules"]["salary"]["min"]
    invalid_sal =df [(df["salary"].isnull()) | ( df["salary"] < sal_min)]
    if not invalid_sal.empty:
        for index,row in invalid_sal.iterrows():
            invalid_salary = row["salary"]
            cust_id = row["customer_id"]
            results.append({"rule": "salary_range",
                    "status": "fail",
                    "message": f"Row {index}, customer_id={cust_id},Invalid salary '{invalid_salary}'",
                    "severity": f"{severity}"})
    return results


def check_country_allowed(df,config_data):
    results = []
    severity = config_data["rules"]["country"]["severity"]
    allowed_countries = config_data.get('allowed_countries')
    invalid_countries = df [(~df["country"].isin(allowed_countries)) | (df["country"].isnull())]
    if not invalid_countries.empty:
        for index,row in invalid_countries.iterrows():
            invalid_country= row["country"]
            cust_id = row["customer_id"]
            results.append({"rule": "country_allowed",
                    "status": "fail",
                    "message": f"Row {index + 1},customer_id={cust_id}  has invalid country '{invalid_country}'",
                    "severity": f"{severity}"})
    return results


