# #CASTING
# text = "123"
# text2 = int(text)

# print(text)
# print(type(text))
# print(text2)
# print(type(text2))


E = input("english score: ")

M = input("maths score: ")

if E.isdigit() and M.isnumeric():
    eng = int(E)
    math = int(M)
    if(0 < eng < 100) and (math < 100 and math > 0):
        if eng >= 50 and math >= 50:
            print("You are eligible for UI admission")
        elif eng >= 50 or math >=50:
            print ("you are eligible for OAU admission")
        else:
            print("no admission")  
    else:
        print("student score not within range")
     
else:
    print("score is not a number")

# score_input = input("enter your score: ")
# score_input = int(score_input)
# scorelist = [39, 44, 49, 54, 59, 64, 69, 74]
# gradelist = ["f9", "E8", "D7", "C6", "C5", "B3", "B2", "A1"]

# for score in scorelist:
#     scorelistpos = scorelist.index(score)
#     grade = gradelist[scorelistpos]
#     if score_input <= score: 
#         print (f"{score_input} is {grade}")
#         break
#     elif score_input > scorelist[-1]:
#         print(f"{score_input} is A1")
#         break
#     else:
#         pass

