#1 Create a generator that generates the squares of numbers up to some number N.
#squares = [i*i for i in range(1, int(input("How many numbers? ")) + 1)]
#for i in squares:
#    print(i, end=" ")

#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
#even_numbers = [i for i in range(0, int(input("\nUp to what number? ")) + 1) if i % 2 == 0]
#print(", ".join(str(num) for num in even_numbers))

#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
#def numbers_generator(n):
#    for i in range(0, n+1):
#        if i % 3 == 0 and i % 4 == 0:
#            yield i

#numbers = numbers_generator(int(input("Up to what number? ")))
#print(", ".join(str(num) for num in numbers))

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

squares = squares(int(input("a: ")), int(input("b: ")))
for i in squares:
    print(i, end=" ")

#5 Implement a generator that returns all numbers from (n) down to 0.
def seq(n):
    for i in range(n, -1, -1):
        yield i

seq = seq(int(input("\nn: ")))
for i in seq:
    print(i, end=" ")