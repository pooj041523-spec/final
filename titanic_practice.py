import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("train.csv")
#Inspect the dataset (head(),info(),describe())
print("First 5 rows of the dataset")
print(df.head())
print("\nDataset info: ")
print(df.info())
print("\nstatistical summary :")
print(df.describe())
#clean the dataset
df['Age'].fillna(df['Age'].mean(),inplace=True)
df.drop(columns=['Cabin','Ticket','Name'],inplace=True)
print("\nDataset after cleaning:")
print(df.head())
#Analysis with pandas
survival_counts = df['Survived'].value_counts()
print("\n Number of passengers survived vs not survived:")
print(survival_counts)
#average age grouped by gender
average_age_gender = df.groupby('Sex')["Age"].mean()
print("\nAverage age grouped by gender:")
print(average_age_gender)
#simple bar chart using matplotlib
plt.figure(figsize=(6,4))
survival_counts.plot(kind="bar",color=['red','green'])
plt.title("survivors vs non-survivors")
plt.xlabel("survival (0 = no,1 = yes)")
plt.ylabel("number of passengers")
plt.xticks(rotation=0)
plt.show()