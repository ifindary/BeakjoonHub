from itertools import combinations
import sys
input = sys.stdin.readline

def teaching():
    N, K = map(int, input().rstrip().split())
    words = [0] * N

    for i in range(N):
        temp = input().rstrip()

        for t in temp[4:len(temp)-4]:
            words[i] |= (1 << (ord(t)-ord('a')))

    if K < 5:
        return 0
    elif K >= 26:
        return N
    
    basics = {'a','n','t','i','c'}
    remains = set(chr(i) for i in range(97, 123)) - basics
    K -= len(basics)

    ans = 0

    for test in combinations(remains, K):
        cnt = 0
        temp = 0

        for b in basics:
            temp |= (1 << (ord(b)-ord('a')))

        for x in test:
            temp |= (1 << (ord(x)-ord('a')))

        for word in words:
            if temp & word == word:
                cnt += 1

        ans = max(ans, cnt)

    return ans


print(teaching())