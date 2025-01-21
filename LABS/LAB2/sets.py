myset = {"apple", "banana", "cherry", True, 1, 2}
tropical = {"pineapple", "mango", "papaya"}
thisset = set(("apple", "banana", "cherry"))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

print(myset, len(myset), type(myset))
for x in thisset:
    print(x)
print("banana" in thisset)

thisset.add("orange")
print(thisset)

thisset.update(tropical)
print(thisset)

thisset.remove("banana")
thisset.discard("cherry")
print(thisset)

set3 = set1.union(set2)
anotherset3 = set1 | set2
print(set3, anotherset3)

myset = set1.union(set2, set3, set4)
anothermyset = set1 | set2 | set3 |set4
print(myset, anothermyset)

aset1 = {"apple", "banana", "cherry"}
aset2 = {"google", "microsoft", "apple"}
print(aset1.intersection(aset2), aset1 & aset2)
print(set1.difference_update(set2), set1-set2)