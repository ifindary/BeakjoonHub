import sys
input=sys.stdin.readline
print=sys.stdout.write

def sorting():
    N = int(input())

    ans = [0] * 10001

    for _ in range(N):
        ans[int(input())] += 1

    for i in range(len(ans)):
        while ans[i]:
            print(str(i)+'\n')
            ans[i] -= 1

# main
sorting()