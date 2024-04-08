import sys
input = sys.stdin.readline

target = list(input().rstrip())
frula = list(input().rstrip())
stack = []

for t in target:
    stack.append(t)

    if stack[len(stack)-len(frula):] == frula:
        for _ in range(len(frula)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")