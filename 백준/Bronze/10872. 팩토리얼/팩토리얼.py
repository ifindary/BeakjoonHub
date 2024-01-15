import sys

def factorial(n: int):
    temp_ans=1

    if n == 0:
        return temp_ans
    
    for i in range(1,n+1):
        temp_ans=temp_ans*i

    return temp_ans

number=int(sys.stdin.readline().strip())
ans=factorial(number)

print(ans)