N = int(input())
numbers = list(map(int, input().rstrip().split()))

temp_min = min(numbers)
temp_max = max(numbers)

print(temp_min, temp_max)