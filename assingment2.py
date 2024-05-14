# def convert():
#     amount = input(" enter amount in dollars: ")
#     if amount.isdigit():
#         dollars = int(amount)
#         naira = dollars*1100
#         print(naira)      
#     else:
#         print("invalid input")
# convert()

# create a list of state and capital

list_states_capital = [
   {
       'state' :'Bauchi',
       'capital' :'Bauchi'
   },
   {
       'state' :'Adamamwa',
       'capital' :'Yola'
   },
   {
       'state' :'Akwa-Ibom',
       'capital' :'Uyo'
   },
   {
       'state' : "Abia",
       'capital' :"Umuahia"
   },
   {
       'state' :'Anambra',
       'capital' :'Awka'
   },

   
       
]

# liststates = []#because we cannot sort dictitonaries we need to change it to a list hence the creatioin of the empty list
# def sort_list():
#     for eachState_capital in  list_states_capital:
#         liststates.append(eachState_capital['state']) #will include only the states

#         # print(liststates, 'Newlist')
#         # print('/n') #this only creates space in the output
# liststates.sort()
#         #print(liststates, "New list sorted")
# for eachItem in liststates:
#         #print(eachItem, "each sorted state")
#         for eachState_capital in list_states_capital:
#             if eachItem == eachState_capital['state']:
#                 print(eachState_capital)
#                 break        


def states_capital():
    info = '''
        press 1, to display list of states and capital
        press 2, to add a new state to the list
        press 3, to edit a particular state and it's capital
        press 4, to dlele aparticular state and it's capital
        press 5, to close the program
        '''
    
    print(info)
    option = input('Enter your choice: ')
    if option == '1':
        liststates = []#because we cannot sort dictitonaries we need to change it to a list hence the creatioin of the empty list
        for eachState_capital in  list_states_capital:
            liststates.append(eachState_capital['state']) #will include only the states

            # print(liststates, 'Newlist')
            # print('/n') #this only creates space in the output
        liststates.sort()
        #print(liststates, "New list sorted")
        for eachItem in liststates:
                #print(eachItem, "each sorted state")
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
        liststates = []#because we cannot sort dictitonaries we need to change it to a list hence the creatioin of the empty list
        for eachState_capital in  list_states_capital:
                liststates.append(eachState_capital['state']) #will include only the states

                # print(liststates, 'Newlist')
                # print('/n') #this only creates space in the output
        liststates.sort()
            #print(liststates, "New list sorted")
        for eachItem in liststates:
                    #print(eachItem, "each sorted state")
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




#         pass
#         elif option == '4':
#             liststates.remove('Anambra')

#             print(liststates)
# def sort_list()

        # pass
        # elif option == '4':
        # pass
        # elif option == '5':
        # pass
        # else:
        #  print('check your input')
        
#         use input to identy the state u want to change with the exact value u want to change in order to identify it. eg lagossss
# loop through your original list to find the match eg if state== lagossss
# if match found, use an input ot request for new state and capital

    

