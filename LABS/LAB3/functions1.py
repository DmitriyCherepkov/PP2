from itertools import permutations 
from math import pi
from random import randint

#1
def toOunces(grams):
    return float(grams) / 28.3495231

#2
def toCelcium(fahrenheit):
    return (5 / 9) * (float(fahrenheit) - 32)

#3
def solve(numheads, numlegs):
    chickens, rabbits = numheads, 0 

    while chickens*2 + rabbits*4 != numlegs:
        chickens -= 1
        rabbits += 1
    print(chickens, rabbits)

#4
def isprime(n):
    for i in range(2, n):
        if n%i==0: return 0
    if not (n == 0 or n == 1): return 1

def filter_prime(arr):
    for i in arr: 
        if isprime(i): print(i)

#5
def printallperms(str):
    for i in list(permutations(str)):
        print(i)

#6
def strreverse(str):
    temp, words, ctr = "", [], len(str)-1

    for i in str:
        if i != ' ': temp += i
        if i == ' ' or ctr == 0:
            words.insert(0, temp)
            temp = ""
        ctr -= 1

    return ' '.join(words)

#7
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == 3 and nums[i-1] == 3: return True
    return False

#8
def spy_game(nums):
    arr, index = [0,0,7], 0

    for i in nums:
        if index == 2: return True
        if i == arr[index]: index += 1
    return False

#9
def spherevol(r):
    return 4/3 * pi * float(r)**3

#10
def uarr(arr):
    newarr, rep = [], 0
    for i in arr:
        for j in newarr:
            if i == j:
                rep = 1
                break
        if rep == 0: newarr.append(i)
        rep = 0
    return newarr

#11
def palindrome(str):
    temp, words, ctr, ispal = "", [], len(str)-1, True

    for i in str:
        if i != ' ': temp += i
        if i == ' ' or ctr == 0:
            words.append(temp)
            temp = ""
        ctr -= 1
    
    if (len(words) == 1): 
        for i in range(int(len(str)/2)):
            if str[i] != str[len(str)-1-i]:
                ispal = False
                break
    else:
        for i in range(len(words)):
            if words[i] != words[len(words)-1-i]:
                ispal = False
                break
    return ispal

#12
def histogram(arr):
    for i in arr:
        print("*"*i)

#13
def guessgame():
    name = input("Hello! What is your name?\n")
    ctr = 1
    num = randint(1,20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    while True:
        guess = int(input("Take a guess.\n"))
        if guess > num: print("\nYour guess is too high.")
        elif guess < num: print("\nYour guess is too low.")
        else: 
            print(f"Good job, KBTU! You guessed my number in {ctr} guesses!")
            break
        ctr += 1