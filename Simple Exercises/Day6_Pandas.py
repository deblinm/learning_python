import pandas as pd

data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [25, None, 40, 17, 65],
    "salary": [50000, 60000, None, 30000, -120000],
    "country": ["US", "US", "CA", "US", None]
}

df = pd.DataFrame(data)
print(df)
print(df.info())

print(df.isnull().sum())


invalid_age = df[(df["age"] < 18) | (df["age"] > 60 )]
print(invalid_age)


required_columns = ["customer_id", "age", "salary","address"]

missing = [col for col in required_columns if col not in df.columns]
print("Missing columns:", missing)

# find rows where salary is null or <= 0

no_salary = df[(df["salary"].isnull()) | (df["salary"] <= 0)]
print(no_salary)


allowed_countries = ["US", "CA"]

# find rows where country is not allowed or null
invalid_country = df[~df["country"].isin(allowed_countries) | df["country"].isnull()]
print (f"invalid country : {invalid_country}")


def validate_age(df):
    return df[(df["age"] < 18) | (df["age"] > 60)]


invalid_age_group = validate_age(df)
print(invalid_age_group)