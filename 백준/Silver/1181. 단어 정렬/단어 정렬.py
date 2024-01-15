import sys

def quick_sort(a, left:int, right:int):    
    pl = left
    pr = right
    x = a[(left+right)//2]

    while pl <= pr:
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr: quick_sort(a, left, pr)
    if right > pl: quick_sort(a, pl, right)

n=int(sys.stdin.readline().strip())

input_str=(str(sys.stdin.readline().strip()) for _ in range(n))

set_str = set(input_str)
re_str = list(set_str)

# 소문자로 준다고 했지만 소문자로 바꿔서 생각하겠다고 명시하였음 (공부용)
temp_str = sorted(re_str, key=str.lower)
new_str = sorted(temp_str, key=len)

for i in new_str:
    print(i)