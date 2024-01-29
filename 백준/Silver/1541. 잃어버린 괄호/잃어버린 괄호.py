import sys
input=sys.stdin.readline

expression = list(input().split('-'))
number = []
temp=[]

for i in expression:
  if not '+' in i:
    number.append(int(i))
  else:
    temp = list(map(int, i.split('+')))
    number.append(sum(temp))

for i in range(1,len(number)):
  number[0] -= number[i]

print(number[0])