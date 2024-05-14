# CRUD operation with python

# Create
# Read
# Update
# Delete

# task

# create a list collection with atleat 4 student names calles studentlist
# using input, add a new student called Samuel
# delete the student in the middle item


# newstudent = input("name: ")

# studentlist.append(newstudent)
# print(studentlist) 
    

# listlength = len(studentlist)
# print(listlength)

# median = listlength//2
# print(median)
# print(studentlist.pop(median))
# print(studentlist)

# for students in studentlist:
#     print(students)

#Task
# create a list of dictionaries with the following properties: name, lastname, age, phone number, friends list of two friends

Studentprofile = [
    {
"name": "Chuks",
"lastname": "Chinwe",
"age": 26,
"phoneNumber": "08038099315",
"friends": ["Tobi", "Timi"]
},
{
"name": "Chuks",
"lastname": "Chinwe",
"age": 26,
"phoneNumber": "08038099316",
"friends": ["Joshua", "Timi"]
}
]

print(Studentprofile)

Newstudent = {
"name": "Stanley",
"lastname": "Chukwuma",
"age": 46,
"phoneNumber": "08038099319",
"friends": ["Feranmi", "Timi"]
}

Studentprofile.append(Newstudent)
print(Studentprofile)

for students in Studentprofile:
    print(students)

# # Function is block of codes that performs specific operation(s)
# # it only executes when it is invoked/called
# studentlist = ["Sayo", "Timileyin", "Tobi", "Malik"]

# def greet() :
#     for students in studentlist:
#         print("hello "+ students )

# greet()

def addAge():
    newage = 0
    for students in Studentprofile:
        print(students)
        newage += students["age"]
    print(newage)
addAge()
# assignment:

# ussing input make a currency converter dollars tonaira and naira to dollars
# do u want to convert dols to naira or vice versa

# CRUD operation on dictionary
# write a function that adds to thelist of dictionaries

weight = input("weightin kg ")
if weight.isnumeric:
    weight_kg = int(weight)
    Studentprofile["weight"] = weight_kg
    for students in Studentprofile:
        print(Studentprofile[weight])
else:
    print("invalid input")
