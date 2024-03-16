import sys
input = sys.stdin.readline

Score = input().rstrip()

if Score == 'A+':
    print(4.3)
elif Score == 'A0':
    print(4.0)
elif Score == 'A-':
    print(3.7)
elif Score == 'B+':
    print(3.3)
elif Score == 'B0':
    print(3.0)
elif Score == 'B-':
    print(2.7)
elif Score == 'C+':
    print(2.3)
elif Score == 'C0':
    print(2.0)
elif Score == 'C-':
    print(1.7)
elif Score == 'D+':
    print(1.3)
elif Score == 'D0':
    print(1.0)
elif Score == 'D-':
    print(0.7)
else:
    print(0.0)