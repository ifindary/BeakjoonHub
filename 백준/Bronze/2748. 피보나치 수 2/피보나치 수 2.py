import sys
input = sys.stdin.readline

n = int(input())

fibo = [0, 1] # 초기 DP 테이블

for i in range(2, n+1):
    fibo.append(fibo[i-2] + fibo[i-1])

print(fibo[n])