goodw = "awesome"
x = 5
y = "John"
a1, a2, a3 = str(3), int(3), float(3)

b1 = b2 = b3 = "Orange"
fruits = ["apple", "orange", "pomegranate"]
c1, c2, c3 = fruits #The number of variables must be equal to the number of the elements in fruits array

#The proper way of naming variables
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

word1 = "Python"
word2 = "is"
word3 = "a great language"
n1, n2 = 5, 10

# The improper way of naming variables
# 2myvar = "John" The first symbol must not be integer
# my-var = "John" - symbol is prohibited
# my var = "John" Spaces are forbidden

# Camel Case myVariableName = "John"
# Pascal Case MyVariableName = "John"
# Snake Case my_variable_name = "John"

print (y + " is " + str(x) + " years old")
print(type(a1), type(a2), type(a3))
print(b1, b2, b3)
print(c1, c2, c3)
print(word1, word2, word3)
print(n1 + n2)

def myfunc():
  global goodw
  goodw = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)