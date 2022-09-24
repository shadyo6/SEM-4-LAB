import numpy as np
import csv 

data=np.loadtxt("Termwork7.txt",usecols=range(1,4),delimiter=',')
print("Mks data:\n",data)

avg=np.array([])
for mks in data:
    avg=np.append(avg,round(np.mean(mks),2))

print("Averages are: ")
for avgMks in avg :
    print(avgMks)

with open("Termwork7.txt") as inF:
    with open("out.txt","w") as outF:
        reader=csv.reader(inF)
        i=0
        for line in reader:
            outF.write(line[4]+'  '+str(avg[i])+'\n')
print("Class Topper has scored average mks: ",np.max(avg))
