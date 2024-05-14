# print("Hello, World!")
# print("Hello") #this is a comment
# x = 5
# y = "John"
# print(y)
# x, y, z = "orange", "Banana", "Pineapple"
# print(x)
# print(y)
# print(z)
# x = 5
# y = 6
# print(x + y)


def convert():
    amount = input(" enter amount in dollars: ")
    if amount.isnumeric():
        dollars = int(amount)
        naira = dollars*1100
        print(naira)      
    else:
        print("invalid input")
convert()