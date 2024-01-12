score= int(input())

if score<0:
    print("점수는 음수일 수 없습니다.")
elif score<60:
    print("F")
elif score<70:
    print("D")
elif score<80:
    print("C")
elif score<90:
    print("B")
elif score<=100:
    print("A")
else:
    print("점수가 이상합니다.")