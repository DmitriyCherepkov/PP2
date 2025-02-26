import math, time

#1 Write a Python program with builtin function to multiply all the numbers in a list
given_list, edited_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], []

for i in given_list:
    edited_list.append(pow(i, 2))

#for i in edited_list:
#    print(i)

#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
given_string, upctr, lowctr = "ABCdefghijklmnop", 0, 0

for i in given_string:
    if i.isupper(): upctr += 1
    else: lowctr += 1

#print(upctr, lowctr)

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
given_palindromes = ["abccba", "abcba", "abc", "ee", "qwe", "ewq", "qwwq"]

#for i in given_palindromes:
#    if str(i) == str(i)[::-1]: print("Yes")
#    else: print("No")

#4 Write a Python program that invoke square root function after specific milliseconds.
#root, milsec = float(input("Type root ")), float(input("Type milliseconds "))

#time.sleep(milsec)
#print(f"Square root of {root} after {milsec} milliseconds is {math.sqrt(root)}")

#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
given_tuple, another_tuple = (1, 1, 1, 1, 1, 1), (1,0,0,0,0)
haszero = False

for i in another_tuple:
    if i != 1:
        haszero = True
        break

if not haszero: print("Has no false")
else: print("Has false")