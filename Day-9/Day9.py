dataSet = []
with open("C:/Users/Daniel/Desktop/AdventOfCode/Day-9/input.txt") as x:
    for line in x:
        line = line[:-1]
        dataSet.append(int(line))
#-------------------------------------------------#

# def checkSum(target, checkSet):
#     sortedSet = sorted(checkSet)
#     front = 0
#     end = len(sortedSet)-1
#     while front<end:
#         if (sortedSet[front]+sortedSet[end] == target):
#             return True
#         elif (sortedSet[front]+sortedSet[end]<target):
#             front += 1
#         else:
#             end -= 1
#     return False

# for i in range(25,len(dataSet)):
#     selectSet = dataSet[i-25:i]
#     if (checkSum(dataSet[i], selectSet) == True):
#         continue
#     else:
#         print("Location index is: "+str(i))
#         print("Value is: "+str(dataSet[i]))
#         exit()

#Target index = 563
def checkSum(target, numberSet):
    sIndex = 0
    eIndex = 1
    while sIndex<eIndex:
        if (sum(numberSet[sIndex:eIndex]) == target):
            print(str(dataSet[sIndex])+" : "+str(dataSet[eIndex-1]))
            newSet = sorted(numberSet[sIndex:eIndex])
            print(max(newSet)+min(newSet))
            print("Sum : "+str(newSet[0]+newSet[len(newSet)-1]))
            return
        elif (sum(numberSet[sIndex:eIndex]) < target):
            eIndex += 1
        else:
            sIndex += 1
checkSum(88311122, dataSet)