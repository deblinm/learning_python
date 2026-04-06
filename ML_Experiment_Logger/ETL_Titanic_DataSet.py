import pandas as pd

def run_pipeline():
        df = pd.read_csv("C:\\Users\\debli\\python_practice\\SourceData\\Titanic-Dataset.csv")

        df2 = df.drop(columns=['PassengerId','Name','Cabin','Ticket'])
        df2['Age'] = df2['Age'].fillna(df2['Age'].median())
        df2['Embarked'] = df2['Embarked'].fillna(df2['Embarked'].mode()[0])

        mapping_sex = {'male': 0, 'female': 1}
        df2['Sex'] = df2['Sex'].map(mapping_sex)
        df2 = pd.get_dummies(df2, columns=['Embarked'], dtype=int)

        df2.to_csv("C:\\Users\\debli\\python_practice\\TargetData\\Titanic-Dataset_Pandas_Version.csv", index=False)
        return df2


modified_df = run_pipeline()
print(f"Pipeline complete! Clean dataset shape: {modified_df.shape}. \n You can check the output file"
          f" in C:\\Users\\debli\\python_practice\\TargetData\\Titanic-Dataset_Pandas_Version.csv")

