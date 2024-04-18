import sys
input = sys.stdin.readline

T = int(input())

time = [300, 60, 10]
cnt = [0, 0, 0]

for i in range(3):
    while True:
        if T < time[i]:
            break

        T -= time[i]
        cnt[i] += 1

if T == 0:
    print(*cnt, sep=' ')
else:
    print(-1)