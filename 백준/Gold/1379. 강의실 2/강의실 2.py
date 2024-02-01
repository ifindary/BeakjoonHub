import heapq
import sys
input=sys.stdin.readline

def min_room():
    N = int(input()) # 강의실 개수
    lecture = [] # 강의 정보
    room = [0]*(N+1) # idx: 강의 번호, 값: 해당 강의 번호의 강의실
    heap = [] # 우선 순위 큐 사용

    lecture = [list(map(int, input().split())) for _  in range(N)]
    lecture.sort(key=lambda x:(x[1], x[2])) # 시작 시간이 빠른 순서대로 정렬

    room_num = 0

    for order, start, end in lecture:        
        heapq.heappush(heap, (end, start, order))
        
        if heap[0][0] <= start:
            room[order] = room[heap[0][2]]
            heapq.heappop(heap)
        else:
            room_num += 1
            room[order] = room_num

    print(room_num)

    for i in room[1:]:
        print(i)


# main
min_room()