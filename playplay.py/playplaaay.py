'''
Create a list of at least 5 states and capital.
From user option 1-4
1. Read - display all stats and capital
2. Create - User can add a state and it capital
3. Update - User can edit a particular state and capital
4. Delete - User can delete a particular state and capital
'''
    
state1 = { 'State': 'Oyo', 'Capital': 'Ibadan'}
state2 = { 'State': 'Lagos', 'Capital': 'Ikeja'}
state3 = { 'State': 'Ogun', 'Capital': 'Abeokuta'}
state4 = { 'State': 'Osun', 'Capital': 'Osogbo'}
state5 = { 'State': 'Ekiti', 'Capital': 'Ado-Ekiti'}

stateCapital_list = [state1, state2, state3, state4, state5]
if user_input == 1:
    print('')

def read():
    for states in stateCapital_list:
        print(states)
read()

def create():
    New_state = input('State: ')
    New_capital = input('Capital: ')
    statenCapital = print(f'{New_state}, {New_capital}')
    stateCapital_list.append(statenCapital)
create()

def delete():
     deleteState = input('state to be deleted: ')
     deleteCapital = input('capital to be deleted: ')
     for states in stateCapital_list:
          if deleteState == s
     

def stateCapital():
    print('''
    Enter 1 to view list of states and capital
    Enter 2 to add a state and capital
    Enter 3 to edit a state of you choice
    Enter 4 to delete a particular state and it capital
    ''')
    

    user_input = input('Enter your option: ')
    if user_input.isnumeric:
            UserInput = int(user_input)
            if UserInput == '1':
                read()
                
            elif UserInput == '2':
                create()
                
            elif UserInput == '3':
                edit()
                
            elif UserInput == '4':
                delete()
                
            elif UserInput == '5':
                pass
            else:
                print('please choose between 1-4')
                stateCapital()
            
    else:
        print('you have entered invalid option')
    
            
stateCapital()
    

        
        
