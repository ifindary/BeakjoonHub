import sys
input=sys.stdin.readline

def sentence():
    string= list(input().rstrip().split(' '))

    if '' in string:
        string.remove('')

    print(len(string))


# main
sentence()