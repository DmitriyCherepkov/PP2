fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for x in fruits:
    print(x)

for x in "banana":
    print(x)

for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass