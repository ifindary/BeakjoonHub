import sys
input = sys.stdin.readline

N, M = input().split()
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B)+len(B-A))