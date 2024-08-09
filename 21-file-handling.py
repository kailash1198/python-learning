# File handling 
"""
1. Creating
2. Reading
3. Updating
4. Deleting

"""

# Open(file name, mode) - mode:r(read),w(write),a(append),x(create)
createFile = open('myfile.txt', 'r')
createFile.close()

readFile = open('myfile.txt', 'r ')
print(readFile.read())
readFile.close()

# createFile = open('user_information.xlsx', 'x')

# readContent = open('user_information.xlsx', 'r')
# print(readContent)

