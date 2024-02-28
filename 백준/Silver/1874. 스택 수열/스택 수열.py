import sys
input=sys.stdin.readline

def stack_sequence():
    n = int(input())
    stack = []
    ans = []
    cur = 1
    flag = True
    
    for _ in range(n):
        num = int(input())

        while cur <= num:
            stack.append(cur)
            ans.append('+')
            cur += 1

        if stack[-1] == num:
            stack.pop()
            ans.append('-')
        else:
            flag = False
            break

    if not flag:
        print("NO")
    else:
        print("\n".join(ans))


# main
stack_sequence()