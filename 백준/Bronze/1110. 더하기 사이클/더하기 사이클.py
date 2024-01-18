import sys
input = sys.stdin.readline

global n, count
count = 1 # 사이클을 몇 번 수행했는지 카운트

def sum_cycle(a) -> int:
    global n, count
    
    temp = a%10 + a//10 # 덧셈의 결과로 나오는 임시 숫자
    new_n = (a%10)*10 + temp%10 # 연산의 결과로 나오는 새로운 수

    if new_n == n:
        return count
    else:
        count += 1
        sum_cycle(new_n)


n = int(input().strip())

sum_cycle(n)
print(count)