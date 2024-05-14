# def convert():
#     temperature = input('enter temperature')
#     if temperature.isdigit():
#         fahrenheit = float(temperature)
#         celcius = 54°F − 32) × 5/9

#     if means_of_measurement is celcius:
 




# Function are blocks of codes that are reuseable
#parameters maybe a  requirements for a function to work.
#argument is a value of a parameters


# def temperature_converter(input_value):
#     print(
#         '''
#     Enter 'F' to convert Fahrenheit to Celcius.
#     Enter 'C' to convert Celcius to Fahrenheit.

#     '''
#         )
#     check = input('Enter your option: ')

#     if check.lower() == 'f':
#         print('You chose to convert Fahrenheit to Celcius')
#           c = (int(input_value) - 32) * 5/9
#         print(f'Fahrenheit {input_value} = {c} Celcius')
#     elif check.lower() == 'c':
#         print('you chose to convert from celcius to Fahrenheit')
#         f = (int(input_value) * 9/5) + 32
#         print(f'Celcius value {input_value} = {f} Fahrenheit')
#     else:
#         print('You have inputted a wrong value')

# temperature_converter(47.2)



# have a list of student profile of atleast five student profile
# task
# using the list write 4 functions to
# 1: read the list
# 2. add new item (profile to the list)
# 3. edit a particualr item in the list
# 4. delete a particular itme in the list


student_profile = [
    {
        'firstname': 'Timi',
        'lastname': 'Timsy',
        'age': '25',
        'phone_number': '09039099315',
        'friend': 'Timini'
    },
    
    {
        'firstname': 'Tosin',
        'lastname': 'Tosy',
        'age': '26',
        'phone_number': '09037099315',
        'friend': 'Tosini'
    },
    {

        'firstname': 'Tomi',
        'lastname': 'Tomsy',
        'age': '27',
        'phone_number': '09036099315',
        'friend': 'Tomini'
    },
    {

        'firstname': 'Tunmi',
        'lastname': 'Tumsy',
        'age': '29',
        'phone_number': '09035099315',
        'friend': 'Tumini'
    },
    {

        'firstname': 'Tola',
        'lastname': 'Tolsy',
        'age': 28, #integer
        'phone_number': '09034099315',
        'friend': 'Tolini'

    }
    
]
def read():
    for students in student_profile:
        print(students)
# read()


    
def add():
    new_firstname = input('firstname: ')
    new_lastname = input('lastname: ')
    new_age = input('age: ')
    new_phone_number = input('phone_number: ')
    new_friend = input('friend: ')

    New_student = {
        'firstname': new_firstname,
        'lastname': new_lastname,
        'age': new_age,
        'phone_number': new_phone_number,
        'friend': new_friend

    }
    student_profile.append(New_student)
    read()
# add()


def edit():
    edit_firstname = input('firstname to be edited: ')
    edit_lastname = input('lastname to be edited: ')
    for students in student_profile:
        if edit_firstname == students['firstname'] and edit_lastname == students['lastname']:
            print(students)
            print(students['firstname'])
            print(students['lastname'])
            print(students['age'])
            print(students['phone_number'])
            print(students['friend'])
            Q1 = input('enter yes to edit firstname')
            if Q1.lower() == 'yes': 
                input_new_firstname = input('enter firstname: ')
            Q2 = input('enter yes to edit lastname: ')
            if Q2.lower() == 'yes':
                input_new_lastname = input('enter lastname: ')

            
# edit()

#         '''
#     enter 'firstname' to edit name
#     enter 'lastname' to edit lastname
#     enter 'age' to edit age
#     enter 'phone_number' to editphone number
#     enter 'friend' to edit friend
#     '''
#     )
#     verify = input('enter your option ')
#     for students in student_profile:
      
#         if verify == students['firstname']:
#             print(students)
#             students['firstname'] = input

def delete():
    delete_firstname = input('firstname to be deleted: ')
    delete_lastname = input('lastname to be deleted: ')
    for students in student_profile:
        if delete_firstname == students['firstname'] and delete_lastname == students['lastname']:
            print(students)
            student_index = student_profile.index(students)
            print(student_index)
            student_profile.pop(student_index)
            read()


# delete()

# create a recursive function that performs the crud operation using the student student_profile

# ie create a function that calls the other functions on the click of a particular value

def encompass():
    print('''
          Click 1 to view all student profiles
          click 2 to add a new profile
          click 3 to edit a profile
          click 4 to delete an item
          click 5 to exit
          ''')

    option = input('enter your option: ')
    if option.isdigit():
        choice = int(option)
        if option == '1':
            read()
            encompass()
        elif option == '2':
            add()
            encompass()
        elif option == '3':
            edit()
            encompass()
        elif option == '4':
            delete()
            encompass()
        elif option == '5':
            pass
        else:
            print('please choose between 1-4')
            encompass()
            
    else:
        print('you have entered invalid option')
encompass()

