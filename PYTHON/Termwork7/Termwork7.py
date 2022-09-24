if __name__ == '__main__':
    myFile = open("Termwork7.txt")
    allLines = myFile.read().splitlines()
    avgMarks = 0
    maxAvg = 0
    for line in allLines:
        (name,m1,m2,m3,m4,usn)=map(str,line.split(","))
        avgMarks = (int(m1)+int(m2)+int(m3))/3
        print(usn, "\t",m1,"\t",m2,"\t",m3,"\t",name)
        print()
        if(avgMarks > maxAvg):
            maxAvg = avgMarks
print("Max class %5.2f" %maxAvg)