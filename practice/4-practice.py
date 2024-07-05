def printNum(startNum, endNum):
    while startNum<endNum:
        print(startNum)
        startNum=startNum+1



def sumNum(inputNum):
    total=0
    while inputNum>0:
        total=total+inputNum
        inputNum=inputNum-1
    return total



printNum(10, 20)
printNum(100, 110)

totalNum = sumNum(200)
print(totalNum)