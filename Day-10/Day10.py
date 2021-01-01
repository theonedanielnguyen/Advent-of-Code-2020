from collections import defaultdict

dataSet = []
with open("C:/Users/Daniel/Desktop/AdventOfCode/Day-10/input.txt") as x:
    for line in x:
        line = line[:-1]
        dataSet.append(int(line))
#---------------------------------------------#
dataSet.append(0)
dataSet.append(max(dataSet)+3)
sortedData = sorted(dataSet)
oneCount = 0
threeCount = 1

for i in range(len(sortedData)):
    diff = sortedData[i]-sortedData[i-1]
    if i == 0:
        diff = sortedData[i]
    if diff==1:
        oneCount+=1
    elif diff==3:
        threeCount+=1

print(oneCount*threeCount)

potentials = defaultdict(int)
potentials[0] = 1

for i in sortedData:
    for ii in range(1,4):
        nextNum = i+ii
        if nextNum in sortedData:
            potentials[nextNum] += potentials[i]

print(potentials[max(dataSet)])