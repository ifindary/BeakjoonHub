import sys
input=sys.stdin.readline

def count_zero():
    N = int(input())
    cnt = 0

    for i in range(1, N+1):
        while i >= 5:
            if i%5 == 0:
               cnt += 1
               i = i//5
            else:
                break

    print(cnt)


count_zero()