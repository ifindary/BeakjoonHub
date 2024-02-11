import sys
input=sys.stdin.readline

def sentence():
    string= list(input().rstrip().split())

    print(len(string))


# main
sentence()