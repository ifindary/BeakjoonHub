
import sys
input=sys.stdin.readline

def postfix():
    exp = input().rstrip()
    ans = []

    for s in exp:
        if 'A' <= s <= 'Z':
            print(s, end='')
        
        else:
            if s == '(':
                ans.append(s)

            elif s == '*' or s == '/':
                while ans and (ans[-1] == '*' or ans[-1] == '/'):
                    print(ans.pop(), end='')
                ans.append(s)

            elif s == '+' or s == '-':
                while ans and ans[-1] != '(':
                    print(ans.pop(), end='')
                ans.append(s)

            elif s == ')':
                while ans and ans[-1] != '(':
                    print(ans.pop(), end='')
                ans.pop()

    while ans:
        print(ans.pop(), end='')


postfix()