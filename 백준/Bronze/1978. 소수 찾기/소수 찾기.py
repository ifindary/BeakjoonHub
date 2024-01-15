import sys
import math

def is_decimal(number):
    if number==1: # 1은 소수가 아님. 0은 자연수가 아니므로 고려 X
        return 0
    elif number==2: # 2는 짝수지만 소수니까 예외
        return 1
    elif number%2==0: # 짝수면 소수가 아님
        return 0
    else:
        temp_sqrt=int(math.sqrt(number)) # 소수점 버림

        for j in range(3, temp_sqrt+1):
            if number%j==0:
                return 0
        return 1

total_n=int(sys.stdin.readline())
number_list=[]

number_list=list(map(int, sys.stdin.readline().split()))

decimal_count=0 # 소수 개수 저장

for i in range(total_n):
    if is_decimal(number_list[i])==1:
        decimal_count += 1

print(decimal_count)