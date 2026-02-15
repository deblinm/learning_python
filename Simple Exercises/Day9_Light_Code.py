import pandas as pd

data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [25, None, 40, 17, 65],
    "salary": [50000, 60000, None, 30000, -120000],
    "country": ["US", "US", "CA", "US", None]
}

allowed_countries = ["US", "CA"]

df = pd.DataFrame(data)

def validate_schema (my_df):
    required_columns = ["customer_id", "age", "salary", "address"]
    missing_columns = [cols for cols in required_columns if cols not in my_df.columns]

    if missing_columns:
        return False
    else:
        return True


missing_cols = validate_schema(df)

if missing_cols:
    print("structure validated successfully")
else:
    print("structure could not be validated")