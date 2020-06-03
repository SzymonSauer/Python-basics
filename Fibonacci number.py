def fibonacci(n):
    first_elements = (0,1)
    a, b = first_elements
    while n>0:
        print(b),
        a, b = b, a+b
        n-=1

print("Enter a number: ")
n = int(input())
print("Fibonacci number of the given digits: ")

def fib(n):
    first_elements = (0,1)
    a, b = first_elements
    while a<n:
        a, b = b, a+b
        print(a)
fib(n)