# day 8 of 100 days python learning challange with code with harry
#Calculator using python - solution

def sumFunc(a,b):
    c = a+b
    return c


print("**************Calculator*************")
print("\n")

print(" 1. Addition\n 2. SUbstraction\n 3. Multiplication\n 4. Division\n\n")

userOption = input('Enter your Option: ')

option = int(userOption)

if(option==1):
    print("*******Addition****")
    numOne = input("Enter number One : ")
    numTwo = input("Enter number Two : ")
    sumTotal = sumFunc(int(numOne), int(numTwo))
    print("Total : ", sumTotal)
elif(option==2):
    print("*********Substraction**********")
elif(option==3):
    print('*********Multiplication***********')
elif(option==4):
    print('*********Division***********')
else:
    print('Please enter valid option')