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

print(list_states_capital[2]['state'])
print(list_states_capital[2]['capital'])

state3 = list_states_capital[2]['state']
capital3 = list_states_capital[2]['capital']

print('The capital of ', state3, 'is', capital3) #you need to add comma to differentiate the variable from the string and each string stretch should be quoated
# 

print(f'The capital of {state3}' is {capital3}) # the {} shows it is a variable and not string

for eachItem in list_states_capital:
    print(eachItem)
    print(f"The capital of {eachItem['state']} is {eachItem['capital']}")


# # for eachitem in list_states_capital:
# #     print(eachitem)
#     # print
# print(list_states_capital[2])

# print(list_states_capital[2]['state'])

# student1 = {
#     "name": "Chuks",
#     "lastname": "Chinwe",
#     "age": 26,
#     "phoneNumber": "08038099315",
#     "friends": [
#         {
#         "name": "Tobi",
#         "lastname": "Tosby",
#         "age": 24,
#         "phoneNumber": "08038099316",
#         "friends" : ['Malik', 'Joshua']

#         },
#         {

#         "name": "Timi",
#         "lastname": "Timsy",
#         "age": 25,
#         "phoneNumber": "08038099317",
#         "friends" : ['Tomi', 'Shaukan']
#         }
#     ]

# }

# print(student1['name'])
# print(student1['lastname'])
# print(student1['friends'][0])
# # print(student1['friends'][0][:1])
# print(student1['friends'][0]['name'])
# print(student1['friends'][0]['lastname'])
# print(student1['friends'][0]['friends'][1][0:3])
# print(student1['friends'][0]['friends'])

# for eachItem in student1['friends'][0]['friends']:
#     print(eachItem)
    
    









