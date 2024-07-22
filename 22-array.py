# Array in python 
# Python has not in built array type but you can get array from numpY python library and you can use them all araay features in python

# Instead you can use LIST type for array

# import array for use array in python
import array

#creating array of Interger => Please note when you define array you also need to mension type of array.
# => You can mension type of array in quote using some type specified keywords
# 'b': signed char (integer)
# 'B': unsigned char (integer)
# 'h': signed short (integer)
# 'H': unsigned short (integer)
# 'i': signed int (integer)
# 'I': unsigned int (integer)
# 'l': signed long (integer)
# 'L': unsigned long (integer)
# 'f': float
# 'd': double

myArray = array.array('i',[1,2,3,4,5])
print(myArray)


#Access array by using index
print(myArray[0])
print(myArray[1])

#Length of the array
print(len(myArray))

#Iterate all element in array using for loops
for i in myArray:
    print(i)

#operation on array
myArray.remove(1)

myArray.append(10)
myArray.insert(100)