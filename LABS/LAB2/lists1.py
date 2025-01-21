mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
anotherlist = list(("apple", "banana", "cherry"))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

print(mylist, thislist, len(thislist), type(mylist))
print(anotherlist, anotherlist[0], anotherlist[-1])
print(mylist[2:5]) # Interval
print(mylist[:4]) # Interval from the first element till the given
print(mylist[3:]) # Interval from the given till the last element
print(mylist[-4:-1])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# To change the item of a list we can simply write the following
list1[0] = 1
list1[1:3] = [2, 3]
list1[3:4] = ["blackcurrant", "pinetree"]
print(list1)
list1[1:5] = ["watermelon"]
list1.insert(len(list1), "Hello")
list1.append("Hello2")
list1.insert(0, "Bye bye")
print(list1)

fruits = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
fruits.extend(tropical)
fruits.remove("apple")
fruits.pop()
print(fruits)
del fruits
list1.clear()
print(list1)