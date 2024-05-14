# list = ["Vel", 20, True, False, ["bacteria", "Fungi"]]
# print(list[4])
# print(list[4][1])
# print(list[4][-1])
# print(list[4][-1])
# list2 = list[4]
# print(list2[:-2])
# print(list[4][-1][:-2])

# for eachItem in list:
#     print(eachItem)
# listb = []
# for eachItem in list:
#     listb.append(eachItem)
#     print(listb)

#     #TUPLE
# fruit = ("apple", "banana", "tomato")
# print(fruit)

# # fruit4 = input("enter a fruit name: ")
# # print(fruit4)

# newfruits = []
# for eachItem in fruit:
#     newfruits.append(eachItem)
# print(newfruits)
# # newfruits.append(fruit4)
# print(newfruits)

# fruit=tuple(newfruits)
# print(fruit)
# print(type(fruit))


studentslist = ["Sayo", "Tobi", "Timileyin", "Malik", "Isaac"]


studentage = [16, 45, 74, 63, 25]

#match eachstiudentto student age


# for x in studentage:
#     studentslist.append(x)
# print(studentslist)

# for eachItem in studentslist:
#     studentage.append(eachItem)
# print(studentslist)

# for eachItem in studentslist:
#     for eachItem in studentage:
# #         print(eachItem)


# for student, age in zip(studentslist, studentage):
#     print(f"{student} is {age} years old")

    #student and age represent the in the lists and are variable
    #f allow to use the variable in the print string

for i in studentslist:
    print(i)

    studentslist_pos = studentslist.index(i)
    print( studentage[studentslist_pos])


for i in studentslist:
    studentslist_pos = studentslist.index(i)
    age = studentage[studentslist_pos]
    print( f"{i} is {age} years old")

for score in scorelist:
    scorelist_pos = scorelist.index(score)
    mark = grade[scorelist_pos]
    print( f"{score} is {mark}") 



  