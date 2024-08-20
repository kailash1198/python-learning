import time

timestamp1=time.strftime('%H:%M:%S')
print(timestamp1)

currentHours =int(time.strftime('%H'))
print(currentHours)

if(currentHours==0):
    print('Good Night')
elif(currentHours==6):
    print('Good Morning')
else:
    print('Not good night')
