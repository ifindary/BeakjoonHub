import sys

n=int(sys.stdin.readline().strip())

a=set(str(sys.stdin.readline().strip()) for _ in range(n))

words=list(a)

words.sort()
words.sort(key=len)

for i in words:
    sys.stdout.write(i+'\n')