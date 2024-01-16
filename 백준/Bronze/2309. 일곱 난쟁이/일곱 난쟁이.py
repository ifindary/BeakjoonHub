import sys
input = sys.stdin.readline

def find_dwarf(dwarfs:list):
    total = sum(dwarfs)

    for i in range(9):
        for j in range(9):
            if i != j  and total - dwarfs[i] - dwarfs[j] == 100:
                temp_i=dwarfs[i]
                temp_j=dwarfs[j]

                dwarfs.remove(temp_i)
                dwarfs.remove(temp_j)
                
                return dwarfs
    
    return False


height = [int(input()) for _ in range(9)]

ans = sorted(find_dwarf(height))

print(*ans, sep='\n')