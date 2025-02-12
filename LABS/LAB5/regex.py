import re

str1 = "abbbbabab0a0"
str2 = "d______a_b_c"
str3 = "aFAefdABC__DEFfDDD"
str4 = "ahello_worldb"
str5 = "Hello. I'm fine, but you... Hm..."
str6 = "example_of_lowercase_sentence_being_turned_into_another_type"
str7 = "HelloWorldPython"

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
print(re.findall("a{1}b*", str1))

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
print(re.findall("a{1}b{2}|a{1}b{3}", str1))

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
print(re.findall(r"(?=([a-z]+_[a-z]+))", str2))

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
print(re.findall("[A-Z][a-z]+", str3))

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print(re.findall("a.+b", str4))

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
print(re.sub("\s|[.]|[,]", ":", str5))

#7 Write a python program to convert snake case string to camel case string.
list_of_letters = re.findall("_[a-zA-Z]", str6)
list_of_letters_len, ctr = len(list_of_letters), 0

i = 0
while i != len(str6)-1:
    if str6[i] == '_': 
        print(list_of_letters[ctr][1].upper(), end="")
        ctr += 1
        i += 1
    else:
        print(str6[i], end="")
    i += 1
print()

#8 Write a Python program to split a string at uppercase letters.
print(re.split('(?=[A-Z])', str7))

#9 Write a Python program to insert spaces between words starting with capital letters.
first = True

def add_space(match):
    global first
    if first:
        first = False
        return match.group(0)
    else:
        return ' ' + match.group(0)

print(re.sub(r"[A-Z]", add_space, str7))

#10 Write a Python program to convert a given camel case string to snake case.
str8 = "HelloHowAreYou"
newstr, i = "", 0

while i != len(str8):
    if str8[i].isupper() and i != 0:
        newstr += '_'
    newstr += str8[i].lower()
    i += 1

print(newstr)