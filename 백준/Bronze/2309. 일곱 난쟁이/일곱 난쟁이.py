import sys
input = sys.stdin.readline

def find_dwarf(dwarfs:list):
    total = sum(dwarfs)

    for i in range(9):
        for j in range(i+1, 9):
            if total - dwarfs[i] - dwarfs[j] == 100:
                dwarfs.remove(dwarfs[i])
                dwarfs.remove(dwarfs[j-1])
                
                return dwarfs
    
    return False


height = [int(input()) for _ in range(9)]

ans = sorted(find_dwarf(height))

print(*ans, sep='\n')