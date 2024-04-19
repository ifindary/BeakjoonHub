import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

M = int(input())

for _ in range(M):
    command = list(input().rstrip().split())

    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])
    else:
        print("ERROR")

right.reverse()
print(*(left+right), sep='')