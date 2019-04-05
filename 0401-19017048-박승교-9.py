##카운트 다운하기
import time


count=int(input("숫자 입력 : "))


for i in range (count,0,-1):
    print(i)
    time.sleep(1) ##1초 멈춤
print("발사!!!")
