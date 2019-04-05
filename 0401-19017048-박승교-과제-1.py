fresh=1
dirty=2

print("사과의 상태? 1(신선)  2(시들시들)")
print(" ")

apple=int(input("선택 : "))

if apple is fresh:
    apple=int(input("사과 가격 : "))
    if (apple < 1000):
        print("10개 구매")
        print("총 금액은 ",apple*10,"입니다.")
    else:
        print("5개 구매")
        print("총 금액은 ",apple*5,"입니다.")
else :
    print("사과를 구매하지 않습니다.")

