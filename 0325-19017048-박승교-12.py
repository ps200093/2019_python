import turtle

t=turtle.Pen()

for i in range(6):
    Dir = input("왼쪽=l, 오른쪽=r : ")
    if (Dir == "l"):
        t.left(60)
        t.forward(50)
    if (Dir == "r"):
        t.right(60)
        t.forward(50)
    
