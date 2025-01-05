import sys
input = sys.stdin.readline

def min_bags(N):
    bag1 = 5
    bag2 = 3
    
    if N%bag1 == 0:
        return N//bag1
    else:
        for No1 in range(N//bag1, -1, -1):
            extra = N - bag1*No1

            if extra%bag2 == 0:
                return No1 + extra//bag2
        
        return -1


### main
N = int(input())
print(min_bags(N))