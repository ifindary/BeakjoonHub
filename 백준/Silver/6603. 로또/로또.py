from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    numbers = list(map(int, input().rstrip().split()))

    if numbers[0] == 0:
        break

    for comb in combinations(numbers[1:], 6):
        print(*list(comb))

    print()