def averageNumber(a,b,c):
    avgNumber = (a+b+c)/3
    return avgNumber

def addNumber(a):
    number = 0
    while a>=0:
        number = number+a
        a=a-1
    
    return number

# avgNumberResult = averageNumber(10,10,10)
# print(avgNumberResult)

numberAdd = addNumber(1200)
print(numberAdd)