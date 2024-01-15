import sys

def move(n: int, start, target):
    if n==1:
        print(f'{start} {target}')
    else:
        move(n-1, start, 6-target-start)
        print(f'{start} {target}')
        move(n-1, 6-target-start, target)

number=int(sys.stdin.readline().strip())

print(2**number-1)

if number <= 20:
    move(number, 1, 3)