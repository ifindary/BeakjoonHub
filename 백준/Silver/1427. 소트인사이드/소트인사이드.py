import sys
input = sys.stdin.readline

numbers = input().rstrip()
temp = list()

for n in numbers:
    temp.append(int(n))

temp.sort(reverse=True)

print(*temp, sep='')