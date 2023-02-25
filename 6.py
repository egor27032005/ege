import turtle

turtle.tracer(0)
turtle.pendown()
turtle.forward(5 * 45)
turtle.left(90)
for i in range(7):
    turtle.forward(2 * 45)
    turtle.left(50)
    turtle.forward(2 * 45)
    turtle.right(122)
turtle.penup()
for x in range(51):
    for y in range(51):
        turtle.setpos(x * 45, y * 45)
        turtle.dot(3, 'green')
turtle.done()
##Повтори 7 [Вперёд 2 Налево 50 Вперёд 2 Направо 122].