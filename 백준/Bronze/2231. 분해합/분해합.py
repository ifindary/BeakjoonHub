import sys
input = sys.stdin.readline

def d_sum():
    N = int(input())

    for A in range(1, N+1):
        ans = str(A)

        test = int(ans)

        for i in range(len(ans)):
            test += int(ans[i])

        if test == N:
            return ans
        
    return 0

print(d_sum())