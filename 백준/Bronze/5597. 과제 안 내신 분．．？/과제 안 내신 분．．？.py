import sys
input = sys.stdin.readline

students = [0]*31

for _ in range(28):
    A = int(input())
    students[A] += 1

for i in range(1, 31):
    if not students[i]:
        print(i)