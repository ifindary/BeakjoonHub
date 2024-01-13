import sys

# 한 줄에 하나의 자연수가 주어지니까 for로 받기
number=[int(sys.stdin.readline()) for _ in range(9)]

# 내장 함수 이용 가능
print(max(number))
print(number.index(max(number))+1)