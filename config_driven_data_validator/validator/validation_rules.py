import  pandas as pd

class QualityChecker:
    def __init__(self,df,config):
        self.df = df.copy()
        self.config = config
        self.result=[]

    def run_rules(self):
        rules = self.config.get("rules", {})

        for rule_name , rule_config in rules.items():
            rule_type = rule_config.get("type")

            if rule_type == "range":
                self.check_range(rule_name,rule_config)
            elif rule_type == "min":
                self.check_min(rule_name, rule_config)
            elif rule_type == "allowed_list":
                self.check_allowed_list(rule_name, rule_config)

        summary = {
            "total_rows": len(self.df),
            "total_failures": len(self.result),
            "high_severity_failures": len(
                [r for r in self.result if r["severity"] == "high"]
            )
        }
        return {
            "summary": summary,
            "failures": self.result
        }



    def check_range(self,rule_name,rule_config):
        column = rule_config["column"]
        severity = rule_config["severity"]
        min_val = rule_config["min"]
        max_val = rule_config["max"]
        self.df[column] = pd.to_numeric(self.df[column], errors="coerce")

        invalid_rows = self.df[((self.df[column].isnull()) |
                        (self.df[column] < min_val) |
                        (self.df[column] > max_val))]

        for idx, val in zip(invalid_rows.index, invalid_rows[column]):
            self.result.append({
                "rule": rule_name,
                "column": column,
                "row": idx,
                "value": val,
                "status": "fail",
                "severity": severity,
                "message": f"{column} value '{val}' is outside range {min_val}-{max_val}"
            })


    def check_min(self, rule_name, rule_config):
        column = rule_config["column"]
        severity = rule_config["severity"]
        min_val = rule_config["min"]
        invalid_rows = self.df[(self.df[column].isnull() |
                        (self.df[column] < min_val))]

        for idx, val in zip(invalid_rows.index, invalid_rows[column]):
            self.result.append({
                "rule": rule_name,
                "column": column,
                "row": idx,
                "value": val,
                "status": "fail",
                "severity": severity,
                "message": f"{column} value '{val}' is below min value allowed {min_val}"
            })



    def check_allowed_list(self,rule_name, rule_config):
        column = rule_config["column"]
        severity = rule_config["severity"]
        allowed_key = rule_config.get("allowed_key")
        allowed_values = self.config.get(allowed_key, [])

        invalid_rows = self.df[(self.df[column].isnull() |
                        ~ self.df[column].isin(allowed_values))]

        for idx, val in zip(invalid_rows.index, invalid_rows[column]):
            self.result.append({
                "rule": rule_name,
                "column": column,
                "row": idx,
                "value": val,
                "status": "fail",
                "severity": severity,
                "message": f"{column} value '{val}' is not in allowed values  {allowed_values}"
            })



