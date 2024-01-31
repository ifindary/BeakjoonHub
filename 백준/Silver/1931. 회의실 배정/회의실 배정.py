import sys
input=sys.stdin.readline

def schedule():
  N = int(input()) # 전체 회의 수
  M = [] # 회의 정보
  end = 0 # 회의가 끝나는 시간
  cnt = 0 # 회의실 별 회의 수

  for _ in range(N):
    s, e = map(int, input().split())
    M.append((s,e))
  
  M.sort(key=lambda x: (x[1], x[0])) # 종료 시간이 빠른 순서대로 정렬

  for mStart, mEnd in M:
    if mStart >= end:
      end = mEnd
      cnt += 1

  print(cnt)


schedule()