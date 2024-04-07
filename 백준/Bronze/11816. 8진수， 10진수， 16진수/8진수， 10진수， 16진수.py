import sys
input = sys.stdin.readline

X = input().rstrip()

if X[0] == '0' and X.isdigit(): # 8진수
    print(int(X, 8))
elif X.isdigit(): # 10진수
    print(X)
else: # 16진수
    print(int(X, 16))