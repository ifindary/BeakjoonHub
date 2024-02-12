from itertools import permutations
import sys
input=sys.stdin.readline

def maximum():
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = 0

    for a in permutations(numbers):
        temp = 0

        for i in range(N-1):
            temp += abs(a[i]-a[i+1])
        
        ans = max(ans, temp)

    print(ans)


# main
maximum()