dataSet = []

with open("C:/Users/Daniel/Desktop/AdventOfCode/Day-11/input.txt") as x:
    for line in x:
        line = line[:-1]
        dataSet.append(line)
##-----------------------------------------------##

print(dataSet[0][-1])

def planeSeating(data):
    newData = []

    for i in range(len(data)):
        if i == 0:
            for pos in data[i]:

        elif i == len(data)-1:
            for pos in data[i]:

        else:
            for pos in data[i]:



    return planeSeating(data)