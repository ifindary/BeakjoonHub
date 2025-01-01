import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

ans1 = int(A)+int(B)-int(C)
ans2 = int(A+B)-int(C)

print(ans1)
print(ans2)