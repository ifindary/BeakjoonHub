def solve(a):
    n=len(a)
    ans = 0

    for i in range(0,n):
        ans = ans + a[i]
    
    return ans
