#자동 판매기 프로그램

price=int(input("상품의 가격을 입력해주세요 : "))

print("돈을 넣어주세요")

won5000 = int(input(" 5000원 지폐 수 "))

won1000 =  int(input("1000원 지폐 수 "))

won500 =  int(input("500원 동전 수 "))

won100 =  int(input("100원 동전 수 "))

won50 =  int(input("50원 동전 수 "))

in_money= won5000*5000 + won1000*1000 +won500*500 + won100*100 + won50*50
out_money =  in_money-price




if price<=in_money:
            print("거스름 돈은 ",out_money,"원 입니다.")
            
else :
            print("돈이 부족합니다.")
            print("거스름돈은 ",in_money,"원 입니다.")



out1000 = out_money//1000
out_money = out_money%1000
out500= out_money//500
out_money = out_money%500
out100= out_money//100
out_money = out_money%100
out50= out_money//50
out_money = out_money%50
print("     ")
print("     ")
print("     ")
print("     ")
print("< 거스름돈 >")
print("1000원 지폐개수 : ", out1000)
print("500원 지폐개수 : ", out500)
print("100원 지폐개수 : ", out100)
print("50원 지폐개수 : ",out50 )


