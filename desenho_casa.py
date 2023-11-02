
import turtle
import math
construtor = turtle.Turtle()
x = 75

#retângulo
construtor.begin_fill()
construtor.fillcolor('pink')
for i in range(2):
    construtor.fd(2*x)
    construtor.left(90)
    construtor.fd(x)
    construtor.left(90)
construtor.end_fill()

#porta
construtor.begin_fill()
construtor.fillcolor('black')
construtor.fd(x/3)
construtor.left(90)
construtor.fd(2*x/3)
construtor.right(90)
construtor.fd(x/3)
construtor.right(90)
construtor.fd(2*x/3)
construtor.end_fill()

#janelas
construtor.up()
construtor.left(90)
construtor.fd(x/4)
construtor.left(90)
construtor.fd(x/3)
construtor.down()

construtor.begin_fill()
construtor.fillcolor('darkblue')
for i in range(4):
    construtor.fd(x/3)
    construtor.right(90)

construtor.up()
construtor.right(90)
construtor.fd(1.5*x/3)
construtor.down()

for i in range(4):
    construtor.fd(x/3)
    construtor.left(90)
construtor.end_fill()

#telhado
construtor.up()
construtor.left(90)
construtor.fd(2*x/3)
construtor.right(90)
construtor.down()
construtor.fd(x/3 + 1.25*x/2)
construtor.left(135)

construtor.begin_fill()
construtor.fillcolor('brown')
construtor.fd(x * math.sqrt(4))
construtor.left(90)
construtor.fd(x * math.sqrt(4))
construtor.end_fill()

turtle.done()