import  pandas as pd

def run_rules(df , config):
    results = []
    for rule_name , rule_config in config["rules"].items():
        rule_type = rule_config["type"].strip()
        column = rule_config["column"]
        severity = rule_config["severity"]


        # Missing column check
        if column not in df.columns:
            results.append({
                "rule": rule_type,
                "status": "fail",
                "message": f"Column '{column}' is missing",
                "severity": severity
            })
            continue

        # ---------- AGE RULE ----------
        if rule_type == "age_range":
            min_age = rule_config["min"]
            max_age = rule_config["max"]
            df[column] = pd.to_numeric(df[column], errors='coerce')
            invalid_rows =  ((df[column].isnull()) |
                             (df[column] > max_age) |
                             (df[column] < min_age))


        # ---------- SALARY RULE ----------
        elif  rule_type == "min_sal":
            min_sal = rule_config["min"]
            invalid_rows = (df[column].isnull() |
                            (df[column] < min_sal))

        # ---------- COUNTRY RULE ----------
        elif rule_type == "allowed_country":
            allowed_key = rule_config.get("allowed_key")
            allowed_values = config.get(allowed_key, [])

            invalid_rows = (df[column].isnull() |
                            ~ df[column].isin(allowed_values) )

        else:
            continue

        invalid_rec = df[invalid_rows]

        for index, val in zip (invalid_rec.index, invalid_rec[column]):
            results.append(
                {
                    "rule": rule_name,
                    "status": "fail",
                    "message": f"Row {index}, invalid value '{val}' in column '{column}'",
                    "severity": severity
                }
            )

    return results
