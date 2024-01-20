import sys
input = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)

numbers = list(map(int, input()))

def dfs(s_idx, e_idx):
    if e_idx - s_idx == 1: # 검사할 서브 트리의 노드가 하나인 경우
        print(numbers[s_idx])
        return
    
    # 오른쪽 서브 트리가 없거나 왼쪽 서브 트리가 없는 경우
    if numbers[s_idx] > numbers[e_idx-1] or numbers[s_idx] < numbers[s_idx+1]:
        dfs(s_idx+1, e_idx) # for문을 거치지 않고 바로 다시 탐색
        print(numbers[s_idx])
        return
    
    for i in range(s_idx, e_idx): # 오른쪽 서브 트리가 어디인지 탐색
        if numbers[i] > numbers[s_idx]: # 오른쪽 서브 트리 시작점을 발견하면
            break # for문 종료
    
    dfs(s_idx+1, i)
    dfs(i, e_idx)
    print(numbers[s_idx])

dfs(0, len(numbers))