ID=['kim','lee','park']
input_ID=str(input("아이디 입력 : "))
PW='1234'
if input_ID in ID:
    input_PW=input("패스워드 입력 : ")
    if (input_PW == PW):
        print("환영합니다.")
    else:
        print("잘못된 패스워드!")
else:
    print("알 수 없는 사용자!")
