import sys
input=sys.stdin.readline

def makesum():
    n = int(input())
    sum = 0

    for i in range(1, n+1):
        sum += i

    print(sum)


# main
makesum()