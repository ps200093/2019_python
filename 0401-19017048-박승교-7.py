

asd=str(input("사과의 상태 : "))

if asd == '신선':
    apple=int(input("사과 가격 : "))
    if (apple < 1000):
        print("10개 구매")
    else:
        print("5개 구매")
else :
    print("사과를 구매하지 않습니다.")
