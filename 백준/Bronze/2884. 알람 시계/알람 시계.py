import sys
input = sys.stdin.readline

H, M = map(int, input().rstrip().split())

temp = 45

if M < temp:
    M = 60 - (temp - M)
    
    if H == 0:
        H = 23
    else:
        H -= 1
else:
    M -= temp

print(H,M)