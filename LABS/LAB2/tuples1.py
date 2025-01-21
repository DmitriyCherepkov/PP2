thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
tuple1 = ("apple", "banana", "cherry")
list = list(tuple1)
list[0] = 1
tuple1 = tuple(list)
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(thistuple, len(thistuple), type(thistuple))
print(thistuple[1], thistuple[-1])
print(thistuple[2:5])
print(thistuple[:2])
print(thistuple[3:])
print(thistuple[-5:-2])
print(tuple1)

y = ("orange",)
thistuple += y
print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)