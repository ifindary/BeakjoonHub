import sys
input=sys.stdin.readline


A, B, C = map(int, input().split())

def multiple(a, b, c):
    if b == 1:
        return a%c
    else:
        temp = multiple(a, b//2, c)

        if b%2 == 0:
            return (temp * temp)%c
        else:
            return (temp * temp * a)%c


print(multiple(A, B, C))