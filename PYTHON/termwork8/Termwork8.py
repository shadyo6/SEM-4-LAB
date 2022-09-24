import pandas as pd
import numpy as np

myData = pd.read_csv("Termwork8.csv")
print(myData.to_string())
print(".....table columns......")
print("===============================")
for col in myData.columns:
	print(col+"\t\t",end="")

colName = input("Enter col name: ")
print(myData.loc[0:10,colName].unique())
print(myData.groupby(colName)[colName].count())
print("Total rows in DFrame: "+str(myData.shape[0]))