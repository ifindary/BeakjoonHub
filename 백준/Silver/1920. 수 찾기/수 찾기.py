import sys
input = sys.stdin.readline

def binary_search(search:list, start:int, end:int, target:int):
    if start > end:
        return 0
    
    mid = (start+end)//2
    
    if search[mid]==target:
        return 1
    elif search[mid]>target:
        return binary_search(search, start, mid-1, target)
    else:
        return binary_search(search, mid+1, end, target)

n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    print(binary_search(n_list, 0, n-1, m_list[i]))