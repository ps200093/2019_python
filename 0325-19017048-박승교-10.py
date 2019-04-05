asd = input("문자열? ")
length=len(asd)

if (length%2==1):
    ch1 = asd[length // 2]
    print("중앙 글자 : ",ch1)
   
else :
    ch1 = asd[length//2-1]
    ch2=asd[length//2]
    print("중앙 글자 : ",ch1,ch2)
