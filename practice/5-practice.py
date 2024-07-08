# Python practice

# built in function  

def functionOne():
    print("This is function one")
    
def functionTwo(numOne, numTwo):
    totalNumber = numOne+numTwo
    print(totalNumber)
    
def functionThree(min, max):
    if min<max:
        print("Min : ",min)
    else:
        print("Max : ",max)
        
    
    
# function call by user 
functionOne()
functionTwo(10, 20)

functionThree(100, 200)
absoluteNumber = abs(100)
print(absoluteNumber)