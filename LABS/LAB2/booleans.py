a = 200
b = 33

print(10 > 9, 10 == 9, 10 < 9)

if b > a:
   print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool("abc"), bool(123), bool(["apple", "cherry", "banana"]))
print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

def myFunction() :
  return True

print(myFunction())

if myFunction():
   print("YES!")
else:
   print("NO!")

print(isinstance(200, int))