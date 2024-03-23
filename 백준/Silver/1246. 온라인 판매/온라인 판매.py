import sys
input = sys.stdin.readline

def egg_selling():
    N, M = map(int, input().split())
    P = list(int(input()) for _ in range(M))
    P.sort(reverse=True)
    
    price = 0
    max_profit = 0

    for i in range(min(M,N)):
        profit = (i+1)*P[i]

        if profit >= max_profit:
            price = P[i]
            max_profit = profit

    print(price, max_profit)


# main
egg_selling()