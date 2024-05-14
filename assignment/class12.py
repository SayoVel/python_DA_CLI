student = "samuel"
student2 = "Ibadan"
print(student[0:3])
student3 = 'Parach'
student4 = 'Ibrahim'

student_list = [student, student2, student3, student4]

#for eachitem in student_list:
    #print(student_list[2][0:4])


#print(student_list[1:3])
#print(student_list[1][:2].upper)





for eachstudent in student_list:
    #print(eachstudent)
    # print(f'hello {eachstudent}')

    if eachstudent == "Ibadan":

        print(f'hello {eachstudent}, welcome to class, pay up')
    else:
        print(f'hello {eachstudent}, welcome to class')

        L:k state1
        

state1 = {'state': 'Oyo', 'Capital': 'Ibadan'}
state2 = {'state': 'Lagos', 'Capital': 'Ikeja'}
state3 = {'state': 'Ogun', 'Capital': 'Abeokuta'}
state4 = {'state': 'Osun', 'Capital': 'Osogbo'}
state5 = {'state': 'Ekiti', 'Capital': 'Ado Ekiti'}

statecapital_list = [state1, state2, state3, state4, state5]

def stateCapital():
    print('''
    Enter 1 to view list of states and capital
    Enter 2 to add a state and capital
    Enter 3 to edit a state of your choice
    Enter 4 to delete a particular state and its capital
    ''')

    user_input = input('Enter your option: ')

    if user_input == '1':
        print('view list of capiatal')
    elif user_input == '2':
        print('add a dtate capital')
    elif user_input == 3:
        print('edit state of your choice')
    elif user_input == 4:
        print('delete a particularstate and capital')
    else:
        print('invalid input')
    
    option = input('input your option')

    def read():
        for statecapital in statecapital_list:
            print(statecapital)
        if option.isdigit():
            choice = int(option)
            if option == 1:
    read()
     print(info)
    option = input('Enter your choice: ')
    if option == '1':
        liststates = []
        for eachState_capital in  list_states_capital:
            liststates.append(eachState_capital['state']) 

            
        liststates.sort()
        
        for eachItem in liststates:
                
            for eachState_capital in list_states_capital:
                if eachItem == eachState_capital['state']:
                        print(eachState_capital)
                        break
        # pass

    elif option == '2':
        new_state = input("new state: ")
        new_capital = input("new capital: ")
        New_item = {
             "state": new_state,
             "capital": new_capital
        }
    
        list_states_capital.append(New_item)
        print(list_states_capital)
        liststates = []
        for eachState_capital in  list_states_capital:
                liststates.append(eachState_capital['state']) 


                
        liststates.sort()
            
        for eachItem in liststates:
                
                for eachState_capital in list_states_capital:
                    if eachItem == eachState_capital['state']:
                            print(eachState_capital)
                            break 
                
    elif option == '3':          
        inputstate = input("the wrong state")
        for eachState_capital in list_states_capital:
            if inputstate == eachState_capital['state']:
                print(eachState_capital)
                eachState_capital['state'] = input('enter the correct state')
                eachState_capital['capital'] = input('enter the correct capital')
                print(eachState_capital['state'])
                
                print(list_states_capital)
states_capital()                            
        





