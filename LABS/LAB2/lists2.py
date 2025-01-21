fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist = ["apple", "banana", "cherry"]
newlist = []
anotherlist = [i for i in thislist if "a" in i]
anotherlist1 = [i for i in thislist if i != "apple"]
numlist = [2**i for i in range(11) if i != 0]
upperlist = [i.upper() for i in thislist]
digitslist = [100, 50, 65, 82, 23]

def myfunc(n):
    return abs(n-50)

for i in thislist:
    print(i)

for i in range(len(thislist)):
    print(thislist[i])

while i < len(thislist):
    print(thislist[i])
    i += 1

for i in thislist:
    if 'a' in i:
        newlist.append(i)
print(newlist, anotherlist, anotherlist1)
print(numlist)
print(upperlist)
fruits.sort(reverse = "True")
print(fruits)
digitslist.sort(key = myfunc)
print(digitslist)

list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort(key = str.lower)
print(list)

mylist = thislist.copy()
mylist2 = thislist[:]
print(mylist, mylist2)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1 + list2)