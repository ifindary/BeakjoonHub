import sys
input = sys.stdin.readline

N = int(input())
hiddens = input().rstrip()
temp = ""
numbers = []

for a in hiddens:    
    if a.isdigit():
        temp += a
    elif temp != "":
        numbers.append(int(temp))
        temp = ""

if temp != "":
    numbers.append(int(temp))
    temp = ""

print(sum(numbers))