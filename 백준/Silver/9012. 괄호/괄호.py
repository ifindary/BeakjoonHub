import sys
input=sys.stdin.readline

def parenthesis():
    N = int(input())
    

    for _ in range(N):
        text = input().rstrip()

        temp = []

        for a in text:
            if a == '(':
                temp.append(a)
            elif a == ')' and temp:
                temp.pop()
            else:
                temp.append("ERROR")
                break

        if not temp:
            print("YES")
        else:
            print("NO")


# main
parenthesis()