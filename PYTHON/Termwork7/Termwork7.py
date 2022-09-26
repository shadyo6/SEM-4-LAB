import numpy as np
import csv

data=np.loadtxt("in.txt",usecols=range(1,5),delimiter=",")
print("Marks data: \n ",data)

avg=np.array([])
for mks in data:
    avg=np.append(avg,round(np.mean(mks),2))

print("Averages are: ")
for avgMks in avg:
    print(avgMks)

with open("in.txt") as inF:
    with open("out.txt","w") as outF:
        reader=csv.reader(inF)
        i = 0
        for line in reader:
            outF.write(line[5] + ' ' + str(avg[i]) + ' \n ')
            i=i+1
print(" class Topper has scored average mks : ", np.max(avg))
