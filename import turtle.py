import turtle

def desenhaquadrado (tart):
    for i in range(5):
        tart.fd(100)
        tart.left(90)
    
def deslocadireita(tart):
    tart.up()
    tart.fd(100)
    tart.down()
    
def desenhaquadradocolorido (tart, cor):
    tart.begin_fill()
    tart.fillcolor(cor)
    for i in range(4):
        tart.fd(100)
    tart.end_fill()
    
t=turtle.Turtle()
t.reset()
t.left(45)
desenhaquadradocolorido(t, 'green')
t.right(45)
deslocadireita(t)
t.left(45)
desenhaquadradocolorido(t, 'yellow')
turtle.done()
