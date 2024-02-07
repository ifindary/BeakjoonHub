from collections import deque
import sys
input=sys.stdin.readline

def cards():
    N = int(input())

    card = deque()

    for i in range(N):
        card.append(i+1)

    while len(card) > 1:
        
        card.popleft()
        card.append(card.popleft())

    print(card[0])


# main
cards()