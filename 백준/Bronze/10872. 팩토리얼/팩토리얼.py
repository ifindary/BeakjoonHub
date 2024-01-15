import sys

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n

number=int(sys.stdin.readline().strip())

print(factorial(number))