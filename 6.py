import turtle

turtle.tracer(0)
turtle.pendown()

turtle.left(90)

for i in range(7):
    turtle.forward(10 * 15)
    turtle.right(90)
    turtle.forward(20 * 15)
    turtle.right(90)
turtle.right(180)
for i in range(3):
    turtle.forward(5*25)
    turtle.left(90)
turtle.penup()
for x in range(51):
    for y in range(51):
        turtle.setpos(x * 15, y * 15)
        turtle.dot(3, 'green')
turtle.done()
##Повтори 7 [Вперёд 2 Налево 50 Вперёд 2 Направо 122].