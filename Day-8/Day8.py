dataSet = []
with open("C:/Users/Daniel/Desktop/AdventOfCode/Day-8/input.txt") as x:
    for line in x:
        line = line[:-1]
        dataSet.append([line[:3], line[4:]])

indexTracker = []
runner = 0
acc = 0

# def game(runner, acc, indexTracker):
#     if runner in indexTracker:
#         print(acc)
#         return
#     else:
#         indexTracker.append(runner)
#         if (dataSet[runner][0] == "nop"):
#             runner += 1
#         else:
#             math = dataSet[runner][1][0]
#             count = str(dataSet[runner][1][1:-1])
#             if (dataSet[runner][0] == "acc"):
#                 acc = eval(str(acc)+math+count)
#                 runner += 1
#             elif (dataSet[runner][0] == "jmp"):
#                 runner = eval(str(runner)+math+count)
#     return game(runner, acc, indexTracker)

# def game(runner, acc, indexTracker):
#     if runner in indexTracker:
#         print(acc)
#         return
#     else:
#         indexTracker.append(runner)
#         if (dataSet[runner][0] == "nop"):
#             runner += 1
#         else:
#             math = dataSet[runner][1][0]
#             count = int(dataSet[runner][1][1:])
#             if (dataSet[runner][0] == "acc"):
#                 if (math == "+"):
#                     acc += count
#                     runner += 1
#                 if (math == "-"):
#                     acc -= count
#                     runner += 1
#             elif (dataSet[runner][0] == "jmp"):
#                 if (math == "+"):
#                     runner += count
#                 if (math == "-"):
#                     runner -= count
#     return game(runner, acc, indexTracker)

# game(runner, acc, indexTracker)

def game(runner, acc, indexTracker):
    if (runner == len(dataSet)-1):
        print(acc)
        quit()
    elif runner in indexTracker:
        return False
    else:
        indexTracker.append(runner)
        if (dataSet[runner][0] == "nop"):
            runner += 1
        else:
            math = int(dataSet[runner][1])
            if (dataSet[runner][0] == "acc"):
                    acc += math
                    runner += 1
            elif (dataSet[runner][0] == "jmp"):
                    runner += math
    return game(runner, acc, indexTracker)

def fixer(program):
    index = 0
    while (index < len(program)):
        accumulator = 0
        indexTracker = []
        runner = 0
        if program[index][0] == "acc":
            index+=1
            continue
        else:
            if program[index][0] == "nop":
                program[index][0] = "jmp"
            elif program[index][0] == "jmp":
                program[index][0] = "nop"
            
            if (game(runner, accumulator, indexTracker) == False):
                if program[index][0] == "nop":
                    program[index][0] = "jmp"
                elif program[index][0] == "jmp":
                    program[index][0] = "nop"
            else:
                quit()
        index += 1

fixer(dataSet)