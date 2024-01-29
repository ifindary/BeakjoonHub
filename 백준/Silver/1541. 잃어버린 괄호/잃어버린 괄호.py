import sys
input=sys.stdin.readline

expression = input().split('-')

for i in range(len(expression)):
  expression[i] = sum(map(int, expression[i].split('+')))
  
  if i > 0:
    expression[0] -= expression[i]

print(expression[0])