# Day 16 of learning 100 days python with code with harry
#Today topics : Match case statement/Switch case statement

def runMatchFunction():
    num = int(input('ENter a number beetween 1 to 3: '))
    match num:
        case 1:
            print('Case-1 Executed')
        case 2:
            print('Case 2 is executed')
        case 3:
            print('Case-3 is executed')
        
        
runMatchFunction()