import sys
input=sys.stdin.readline

def compare():
    A, B = map(int, input().split())
    
    temp1 = A//100
    temp2 = (A//10)%10
    temp3 = A%10
    A = temp3*100 + temp2*10 + temp1

    temp1 = B//100
    temp2 = (B//10)%10
    temp3 = B%10
    B = temp3*100 + temp2*10 + temp1

    print(max(A, B))


# main
compare()