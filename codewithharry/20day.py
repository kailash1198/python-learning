# Day 20 of learning 100 days python with code with harry
#Today topics : function

def userDataCreation(userName, password, age, rank):
    studentData = {
                   "Name: " : userName,
                   "Password: ": password,
                   "Age:": age,
                   "Rank:": rank
                   }
    
    for i, value in studentData.items():
        print(i, value)
        
        
userDataCreation('Kailash', '12345', '26', '10')


# studentData = {
#                    "Name: " : 'Kailash',
#                    "Password: ": '123',
#                    "Age:": '10',
#                    "Rank:": '40'
#                    }

# # print(studentData)
# for key, value in studentData.items():
#     print(key, value)
    