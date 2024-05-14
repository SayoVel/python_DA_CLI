num1 = 50

num2 = 40
# if num1 == 50:
#     print("num1 is 50")

if num1 == 40:
    print("num1 is 40")
else:
    print("num1 is not 40")

if num1 == 40:
    print("num1 is 40")
elif num1 < 40:
    print("num1 is less than 40")
elif num1 > 60:
    print("num1is greater than 50")
elif num1 is 70:
    print("num1 is 70")
elif num1 < 70:
    print("num1 is less than 70")
else:
    print("num1 is unknown")

if num1 > 60 and num2 < 30:
    print ("the test failed")
else:
    print("test succeded")

if num1 > 60 and num2 == 40 :
    print ("test2 successful")
else:
    print("test2 failed")

if num1 > 60 or num2 == 40 :
    print ("test3 successful")
else:
    print("test3 failed")

    """
    UI requires students to score 50 or above in both English and mathematics to be considered for admission
    OAU requires students to score 50and above in either English or mathematics to be considered for admission
    Task
    write a programme that takes a score and check if student is eligible for either UI admission or OAU admission
    """

    """
    A1 = 75
    B2 = 70-74,
    B3 = 65-69, 
    C4 = 60-64,
    C5 = 55-59,
    C6 = 50-54,
    D7 = 45-49,
    E8 = 40-44,
    F9 = 39
    your grade for 57 is C5
    IF YU INPUT SCORE IT SHOULD GIVE THEUR GRAGE
    """

E = input("english score:")

M = input("maths score:")


if E >= 50 and M >= 50:
    print("UI admission")

elif E >= 50 or M >= 50:
    print("OAU admission")
else:
    print("No admission")

score = input("input score:")

if score <= 39:
    print ("f9")
elif score == 40 or score <= 44:
    print("E8")
elif score == 45 or score <= 49:
    print("D7")
elif score == 50 or score <= 54:
    print("C6")
elif score == 55 or score <= 59:
    print("C5")
elif score == 60 or score <= 64:
    print("C4")
elif score == 65 or score <= 69:
    print("B3")
elif score == 70 or score <= 74:
    print("B2")
elif score == 75:
    print("A1")
