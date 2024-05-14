# LIST METHODS

#append()
#adds an element to the list

students = ["Sayo", "Tobi", "Timi"]
students.append("Vel")
print(students)

#clear: removes all elements from the list

# students.clear()
# print(students)

#copy: makes a copy of the list

studentslist = students.copy()
print(studentslist)

#count() counts the number of a specified element in the list

Newlist = ["sayo", "Tope", "Tope"]
x = Newlist.count("Tope")
print(x)

#extend(): extends a list

# students.extend(Newlist)
# print(students)

#index: tells the position of the elements in a list
students.index("Timi")

#inert(): inserts an element to a specified position on the list
students.insert(2, "Fela")
print(students)

#pop(): removes an element a a specified position
students.pop(2)
print(students)

#remove: removes a specified element from the list
students.remove("Timi")
print(students)

#reverse(): reverses theorder of the list
students.reverse()
print(students)

#sort(): sorts the list alphabetically

students.sort()
print(students)


#TUPLE METHODS

# count(): counts the number of times a specified element appears in the tuple

ages = (1, 2, 2, 3, 4, 2, 2)
x = ages.count(2)
print(x)

#index(): finds the index number of a specified element

x = ages.index(4)
print(x)

#SET METHODS
#add():adds an element to the set

fruits = {"watermelon", "apples", "tangerine", "orange"}
fruits.add("lemon")
print(fruits)

#clear(): removes all elements from the set

# fruits.clear()
# print(fruits)

#copy(): copies the set

# x = fruits.copy()
# print(x)

#difference() gives the elements that are in set fruits butnotin food

food = {"amala", "watermelon", "eba", "tangerine", "poundo"}
# y = fruits.difference(food)
# print(y)

#difference_update: removes commonelements in both sets

z = fruits.difference_update(food)
print(z)

# discard: removes a specified item

fruits.discard("orange")
print(fruits)

w = fruits.intersection(food)
print(w)

fruits.intersection_update(food)
print(fruits)

V = fruits.isdisjoint(food)
print(V)

s = {1, 2, 3}
t = {1, 2, 3, 4, 5}

r = s.issubset(t)
print(r)

k = {7, 8, 9, 10, 11, 12}
m = {7, 8, 9}
o = k.issuperset(m)
print(o)

# #pop( removes a random item formthe set)
k.pop()
print(k)

# #remove() removes a specified item from the set
k.remove(10)
print(k)

# #symmetric_difference() gives the other items not present in both sets

j = fruits.symmetric_difference(food)
print(j)

g = k.symmetric_difference_update(m)
print(g)

#union(): gives a set that has all the items in both set but will not the duplicate items

f = k.union(m)
print(f)

#update()
s.update(t)
print(s)