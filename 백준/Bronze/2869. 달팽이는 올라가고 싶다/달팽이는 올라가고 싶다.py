import sys
input=sys.stdin.readline

def snail_up():
    A, B, V = map(int, input().split()) # 낮 속도, 밤 속도, 높이

    if (V-B)%(A-B)==0:
        print((V-B)//(A-B))
    else:
        print((V-B)//(A-B)+1)


# main
snail_up()