dataSet = []
with open("C:/Users/Daniel/Desktop/AdventOfCode/Day-8/input.txt") as x:
    for line in x:
        line = line[:-1]
        dataSet.append([line[:3], line[4:]])

print(dataSet)