import pandas as pd

titanic = pd.read_csv(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Training Session\Day11\Titanic\titanic.csv")

# Compare the average of age of passengers based on "Survived"
print(titanic.groupby("Survived")["Age"].agg(["mean"]).reset_index())

# Calculate survival rate by gender
gender_survival = titanic.groupby("Sex")["Survived"].agg(["mean"]).reset_index()
gender_survival["mean"] = gender_survival["mean"] * 100
print(gender_survival)

# Add column to df
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]
print(titanic)

# Calculate family survival rate and merge to df
family_survival = titanic.groupby("FamilySize")["Survived"].mean().reset_index()
family_survival.columns = ["FamilySize", "FamilySurvivalRate"]
titanic = titanic.merge(family_survival, on="FamilySize", how="left")
print(titanic)
