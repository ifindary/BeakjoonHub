import sys

a=int(sys.stdin.readline())

for _ in range(a):
    n, text=sys.stdin.readline().split()
    temp_n=int(n)

    for x in text:
        print(x*temp_n, end='')
    print()