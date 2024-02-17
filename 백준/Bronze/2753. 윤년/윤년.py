import sys
input=sys.stdin.readline

def leapyear():
    N = int(input())
    
    if (N%4 == 0) and (N%100 != 0 or N%400 == 0):
        print(1)
    else:
        print(0)


# main
leapyear()