import sys
input = sys.stdin.readline

A = input().rstrip()
ans = ''

for a in A:
    if a.isupper():
        ans += a.lower()
    else:
        ans += a.upper()

print(ans)