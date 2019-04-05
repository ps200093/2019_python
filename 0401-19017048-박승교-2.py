year=int(input("연도 입력 : "))

x=year%4==0
y=year%100!=0
z=year%400==0

if ((x and y) or (z)):
    print(year,"년은 윤년")
else:
    print(year,"년은 윤년 아님")
