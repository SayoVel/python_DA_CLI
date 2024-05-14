# write a code that lists  1 to 1000

# for number in range(1, 101):
#     print(number)
# for number in range(1, 101):
#     if number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)
#         for number in range(1, 101):
#             if number % 3 == 0:
#                 print('Buzz')

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#      print('FizzBuzz')




#      given a range of numbers 1 to 50
#      if your number is divisible by 3
# print fizz
# if it is divisible by 5 print buz
# if divisible by 3 and 5 print fizzbuzz
# else print number

# psuedo code is a description of steps in an 

# 1 = 1
# 2 = 2
# 3 = fizz
# 4 = 4
# 5 = buzz
# 6 = fizz
# 7 = 7
# 8 = 8
# 9 = fizz
# 10 = buzz
# 11 = 11 
# 12 = fizz
# 13 = 13
# 14 = 14
# 15 = fizzbuzz


# for number in range(1, 50):
#     # print(number)
#     if number % 3 == 0 and number % 5 == 0:
#         print('fizzbuzz')
#     elif number % 3 == 0:
#         print('fizz')
#     elif number % 5 == 0:
#         print('buzz')
#     else:
#         print(number)

# write a function that takes a number 
# from range 1 to n perform the fizzbuzz task

def word():
    x = input('number: ')
    if x.isdigit():
        xn = int(x)

        for number in range(1, xn):    
            if number % 3 == 0 and number % 5 == 0:
                print('fizzbuzz')
            elif number % 3 == 0:
                print('fizz')
            elif number % 5 == 0:
                print('buzz')
            else:
                print(number)
    else:
        print('you have inpuuted an invalid value')
word()



