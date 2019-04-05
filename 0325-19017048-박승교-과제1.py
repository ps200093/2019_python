shoppingList = ['milk','eggs','cheese','butter','cream']

print("<가격>")
print("milk : 2000")
print("eggs : 300")
print("cheese : 3000")
print("butter : 1500")
print("cream : 1000")
print( )

a =input("사야할 물품 입력 : ")
b = int(input("개수  : "))

milk = 2000
eggs = 300
cheese = 3000
butter = 1500
cream = 1000

d = a*b

if a in shoppingList:
    print(d)
    print(" ")
else :
        ##if
    print("목록에 없음!")
