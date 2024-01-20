import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

numbers = []

# EOF 에러 처리 # int 안 붙이면 빈값도 계속 받음
while True:
    try:
        numbers.append(int(input().rstrip()))
    except:
        break

def postorder(s_idx, e_idx): # (시작 인덱스, 종료 인덱스)
    if s_idx > e_idx:
        return
    
    # 오른쪽 서브 트리의 시작 인덱스를 끝값까지 두기
    # 모든 노드가 왼쪽 서브 트리라고 가정
    right_idx = e_idx + 1

    for i in range(s_idx+1, e_idx+1):
        if numbers[i] > numbers[s_idx]: # 루트 노드보다 큰값을 발견하면
            right_idx = i # 그 인덱스부터 오른쪽 서브 트리임을 알 수 있으니까 저장
            break

    # 왼쪽 서브 트리를 대상으로 다시 탐색
    postorder(s_idx+1, right_idx-1)

    # 왼쪽이 다 끝나면 서브 트리를 대상으로 다시 탐색
    postorder(right_idx, e_idx)

    print(numbers[s_idx])


postorder(0, len(numbers)-1)
    