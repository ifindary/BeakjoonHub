import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())
numbers = {A, B, C}
m = max(A, B, C)

if len(numbers) == 1:
    print(10000+m*1000)
elif len(numbers) == 2:
    if A == B or A == C:
        print(1000+A*100)
    else:
        print(1000+B*100)
else:
    print(m*100)