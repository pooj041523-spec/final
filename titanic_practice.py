import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("train.csv")
survival_counts =df["Survived"].value_counts()
survival_counts.plot(kind="bar")
plt.title("survivors vs non-survivors")
plt.xlabel("survival status")
plt.ylabel("number of passengers")
plt.xticks(ticks=[0,1],labels=["not survived","survived"],rotation=0)
plt.show()