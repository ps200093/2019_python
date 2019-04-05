##import random

from random import randint


print("*****숫자 게임*****")
Q1=int(input("1~100사이의 숫자 추측하기 : "))
ans= randint(1,100)

if Q1>ans:
    print("입력값이 큼")

elif Q1==ans:
    print("맞았습니다")
        
else:
    print("입력값이 작음")


print("게임 종료")

print("정답은 ",ans)
