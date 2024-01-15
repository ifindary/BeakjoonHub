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

number_list=[int(sys.stdin.readline()) for _ in range(n)]

quick_sort(number_list, 0, len(number_list)-1)

for i in number_list:
    print(i)