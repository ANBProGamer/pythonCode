import random
import turtle
t = turtle.Pen()
turtle.speed(10)


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
        x = 65*p
        y = 37*q - 252
        t.up()
        t.goto(x,y)
        t.down()
        t.dot(3,"green")
        (z) = random.randrange(1,100)
        if (z) <= 85:
                (p,q) = function85(p,q)
        elif (z) <= 92:
                (p,q) = function7a(p,q) 
        elif (z) <= 99:
                (p,q) = function7b(p,q)
        elif (z) <= 100:
                (p,q) = function1(p,q)
                
        

