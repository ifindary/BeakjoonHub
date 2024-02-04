import sys
input=sys.stdin.readline

def snail_up():
    N = int(input()) # 테스트 케이스의 개수

    for _ in range(N):
        score = 0

        test = input().rstrip().split('X')

        for ans in test:
            if ans:
                for i in range(len(ans)):
                    score += (i+1)

        print(score)


# main
snail_up()