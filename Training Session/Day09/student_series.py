import pandas as pd

student_dict={
    "Anu":67,
    "RRR":87,
    "Manu":77,
    "Hari":81
}
students=pd.Series(student_dict)
print(students)
print("3rd Student Score : ",students.iloc[2])
print("Score of RRR : ",students.loc["RRR"])

print("Students who score greater than 80 : ")
print(students[students>80])