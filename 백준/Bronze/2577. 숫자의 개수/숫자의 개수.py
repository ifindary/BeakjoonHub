import sys
input=sys.stdin.readline

numbers = [int(input()) for _ in range(3)]
result = str(numbers[0]*numbers[1]*numbers[2])
ans = [0]*10

for a in result:
    ans[int(a)] += 1

print(*ans, sep='\n')