import sys
input = sys.stdin.readline
print = sys.stdout.write

# N명의 사람을 K번째마다 삭제
N, K = map(int, input().split())
people = [] # 대기열에 있는 사람
delete = [] # 삭제된 사람 목록

idx = 0 # 몇 번째 사람을 삭제할 건지

for i in range(1, N+1):
    people.append(i)

while len(people) != 0:
    idx += K - 1 # 인덱스는 0부터 시작이니까 1 빼기

    if idx < len(people):
        delete.append(people.pop(idx))
    else:
        while idx >= len(people):
            idx = idx - len(people)
        
        delete.append(people.pop(idx))

print('<')
for i in range(len(delete)):
    if i != len(delete)-1:
        print(str(delete[i])+', ')
    else:
        print(str(delete[i]))
print('>')