import sys

N=9 # 정수 9개가 주어짐
number_list=[] # 자연수를 입력 받을 리스트 정의

# 한 줄에 하나의 자연수가 주어지니까 for로 받기
# 띄어쓰기로 받을 거면 list(map(int, input().split())) 이용하면 됨
for i in range(N):
    number_list.append(int(sys.stdin.readline()))

# list 내의 첫 숫자를 임시로 최대값으로 지정
max_number = number_list[0]
max_order = 1

for i in range(1,N):
    if number_list[i] > number_list[max_order-1]:
        max_order = i+1
        max_number = number_list[i]
    # 서로 다른 자연수니까 같을 케이스는 고려하지 않음

print(max_number, max_order, sep='\n')