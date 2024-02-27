import sys
input=sys.stdin.readline

def moviename():
    N = int(input())
    
    numbers = 666
    index = 0

    while True:
        if '666' in str(numbers):
            index += 1
        if index >= N:
            break
        
        numbers += 1
        
    print(numbers)


# main
moviename()