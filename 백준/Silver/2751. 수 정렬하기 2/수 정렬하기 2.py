from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
ans = []

# 최대 힙 만들기(최상단 노드가 최대값)
def heapify(parent):
        while parent < (len(a)//2):
            cl = parent*2 + 1 # 왼쪽 자식 노드
            cr = parent*2 + 2 # 오른쪽 자식 노드

            if cr < len(a) and a[cl] < a[cr]:
                child = cr
            else:
                child = cl

            if a[parent] > a[child]:
                break
            else:
                a[parent], a[child] = a[child], a[parent]
                parent = child

# 힙 정렬
def heap_sort():
    # 배열을 힙으로 만들기
    for i in range((n-1)//2, -1, -1): # 힙 크기의 반 -> 0
        heapify(i)

    # 최대값 찾기
    while a:
        a[0], a[-1] = a[-1], a[0] # 최상단 노드(최대값)와 최하단 노드 바꾸기
        ans.append(a.pop()) # 최대값인 노드 ans에 넣기

        heapify(0) # 새로운 최상단 노드 대상으로 다시 힙 정렬
    

heap_sort()

print(*reversed(ans), sep="\n")