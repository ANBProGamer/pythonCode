import random
import turtle
t = turtle.Pen()


def function85(x, y):
        a = 0.85*x + 0.04*y
        b = -0.04*x + 0.85*y + 1.6
        return(a,b)
def function1(x,y):
        a = 0
        b = 0.16*y
        return(a,b)
def function7a(x,y):
        a = 0.2*x - 0.26*y
        b = 0.23*x + 0.22*y + 1.6
        return(a,b)
def function7b(x,y):
        a = -0.15*x + 0.28*y
        b = 0.26*x + 0.24*y + 0.44
        return(a,b)

(p,q) = (0,0)
for i in range(1000000):
        (z) = random.randrange(1,100)
        if (z) <= 85:
                (p,q) = function85(p,q)
                t.up()
                t.goto(p,q)
                t.down()
                t.dot(3,"red")
        elif (z) <= 92:
                (p,q) = function7a(p,q)
                t.up()
                t.goto(p,q)
                t.down()
                t.dot(3,"red")
        elif (z) <= 99:
                (p,q) = function7b(p,q)
                t.up()
                t.goto(p,q)
                t.down()
                t.dot(3,"red")
        elif (z) <= 100:
                (p,q) = function1(p,q)
                t.up()
                t.goto(p,q)
                t.down()
                t.dot(3,"red")

        
