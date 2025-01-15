import random

x = 35656222554887711 # int
y = 2.8  # float
z = 1j   # complex
x1 = 35e3
y1 = 12E4
z1 = -87.7e100

print(type(x), type(y), type(z))
print(type(x1), type(y1), type(z1))
print(x1, y1, z1)

x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)

print(a, b, c)
print(type(a), type(b), type(c))

print(random.randrange(1, 10))