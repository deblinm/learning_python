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

    rule_config = config_data["rules"]["age"]
    min_age = rule_config["min"]
    max_age = rule_config["max"]
    severity = rule_config["severity"]

    if "age" not in df.columns:
        return [{
            "rule": "age_range",
            "status": "fail",
            "message": "Column 'age' is missing",
            "severity": severity
        }]

    age_calc = df [(df["age"] > max_age) |
                   (df["age"] < min_age) |
                   (df["age"].isnull())]
    results = [{
        "rule": "age_range",
                    "status": "fail",
                    "message": f"Row {idx}, invalid age '{inval_age}'",
                    "severity": f"{severity}"}
        for idx,cust_id, inval_age in zip(age_calc.index,
                                          age_calc.get("cust_id", ["N/A"] * len(age_calc)),
                                          age_calc["age"])
    ]

    return results

def check_salary_range(df,config_data):
    results = []

    rule_config = config_data["rules"]["salary"]
    min_sal = rule_config["min"]
    severity = rule_config["severity"]

    if "salary" not in df.columns:
        return [{
            "rule": "salary_range",
            "status": "fail",
            "message": "Column 'salary' is missing",
            "severity": severity
        }]

    invalid_sal =df [(df["salary"].isnull()) | ( df["salary"] < min_sal)]

    results = [{
        "rule": "salary_range",
        "status": "fail",
        "message": f"Row {idx}, customer_id '{cust_id}' invalid salary '{salary}'",
        "severity": f"{severity}"}
        for idx, cust_id, salary in zip(invalid_sal.index,
                                        invalid_sal.get("cust_id", ["N/A"] * len(invalid_sal)),
                                        invalid_sal["salary"])
    ]
    return results


def check_country_allowed(df,config_data):
    rule_config = config_data["rules"]["country"]
    severity = rule_config["severity"]
    allowed_countries = config_data.get('allowed_countries', [])

    if "country" not in df.columns:
        return [{
            "rule": "country_allowed",
            "status": "fail",
            "message": "Column 'country' is missing",
            "severity": severity
        }]

    if not allowed_countries:
        return [{
            "rule": "country_allowed",
            "status": "fail",
            "message": "Allowed countries list is missing in config",
            "severity": severity
        }]

    invalid_countries = df[(~df["country"].isin(allowed_countries))
                           | (df["country"].isnull())]

    results = [{
        "rule": "country_allowed",
        "status": "fail",
        "message": f"Row {idx}, customer_id '{cust_id}' has invalid country '{ctry}'",
        "severity": f"{severity}"}
        for idx, cust_id, ctry in zip(invalid_countries.index,
                                        invalid_countries.get("cust_id", ["N/A"] * len(invalid_countries)),
                                        invalid_countries["country"])
    ]
    return results


