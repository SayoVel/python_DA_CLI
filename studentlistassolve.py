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
stateList = []
for state_capital in stateCapital_list:
    state = f'{state_capital["State"]} : {stte_capital["Capital"]}'
    stateList.append(state)
stateList.sort()
def read():
    num = 1
    for eachState in stateCapital_List:
        print(f'{num}. {eachState}')
        num += 1
if user_input =='2':
    print('Add a state and capital\n') #\nis for new line
    getState = input('Enterstate: