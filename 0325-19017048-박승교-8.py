total = int(input("총 금액 : "))

if (total >= 1000):
    discount = total*0.1
    print("할인액 : ",discount)
else :
    if (total > 500 ) :
        discount = total*0.05
        print("할인액 : ", discount)
    else:
        print("할인 안됨!")
