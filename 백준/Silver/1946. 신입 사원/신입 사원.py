import sys
input=sys.stdin.readline

def recruit():
  N = int(input()) # 지원자의 숫자
  applicant = [] # 지원자 정보
  
  for _ in range(N):
    applicant.append(tuple(map(int, input().split())))

  applicant.sort() # 서류 순위가 제일 높은 사람은 무조건 뽑힘

  a, b = applicant[0] # 서류 1위 성적
  cnt = 1 # 뽑힌 인원 수

  for i in range(1, N):
    if applicant[i][0] < a or applicant[i][1] < b:
      cnt += 1
      
      a, b = applicant[i][0], applicant[i][1]

  print(cnt)


## main

T = int(input()) # 테스크 케이스 개수

for _ in range(T):
  recruit()