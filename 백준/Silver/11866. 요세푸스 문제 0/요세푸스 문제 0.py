import sys
input = sys.stdin.readline
print = sys.stdout.write

# N명의 사람을 K번째마다 삭제
N, K = map(int, input().split())
people = []
delete = []

a = K-1

for i in range(1, N+1):
    people.append(i)

# pop은 인덱스, remove는 값을 제거한다는 점을 주의
delete.append(people.pop(K-1))

while len(people) != 0:
    if len(people) == 1:
        delete.append(people.pop())
    elif a + K-1 < len(people):
        a = a+K-1
        delete.append(people.pop(a))
    else:
        a = a+K-len(people)-1
        
        while a >= len(people):
            a = a - len(people)
        
        delete.append(people.pop(a))

print('<')
for i in range(len(delete)):
    if i != len(delete)-1:
        print(str(delete[i])+', ')
    else:
        print(str(delete[i]))
print('>')