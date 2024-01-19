import sys
input = sys.stdin.readline

n, s = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

count = 0

def part_sum(a: list, idx: int, sum: int):
    global count

    if idx >= len(a): # 종료 조건: 확인 중인 인덱스가 범위 밖일 때
        return

    sum += a[idx]

    if sum == s: # 현재까지 더한 합계가 목표에 맞는지 확인
        count += 1

    # 지금 a[idx]를 더하는 경우의 수를 다시 탐색
    part_sum(a, idx+1, sum)

    # 더하지 않는 경우의 수를 다시 탐색
    part_sum(a, idx+1, sum-a[idx])


part_sum(numbers, 0, 0)

print(count)