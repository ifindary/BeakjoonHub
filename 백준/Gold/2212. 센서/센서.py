import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().rstrip().split())))

ans = []

for i in range(1, N):
    ans.append(sensors[i]-sensors[i-1])

ans.sort()

print(sum(ans[:N-K]))