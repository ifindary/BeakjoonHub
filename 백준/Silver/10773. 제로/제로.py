import sys
input=sys.stdin.readline

def money():
    K = int(input())
    numbers = []

    for _ in range(K):
        temp = int(input())

        if temp == 0:
            numbers.pop()
        else:
            numbers.append(temp)

    print(sum(numbers))


# main
money()