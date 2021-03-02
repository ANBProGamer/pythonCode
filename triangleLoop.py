import random
import turtle
debug = 0
t = turtle.Pen()

def drawDot(coord1, coord2, sizeD, colorD):
        t.up()
        t.goto(coord1, coord2)
        t.down()
        t.dot(sizeD, colorD)
             

my_list = []

# Picks three co-ordinates to form the triangle

    
y = (-300)
z = (300)
my_list.append([y,y])
my_list.append([z,z])
my_list.append([y,z])
drawDot(z,z,20,"red")
drawDot(y,y,20,"red")
drawDot(y,z,20,"red")
#t.up()
#t.goto(z,z)
#t.down()
#t.dot(20,"red")
##t.up()
##t.goto(y,y)
##t.down()
##t.dot(20,"red")
##t.up()
##t.goto(y,z)
##t.down()
##t.dot(20,"red")
if(debug):
        print(my_list)

turtle.bgcolor("black")
# Picking the starting coordinate
a = random.randint(-100,100)
b = random.randint(-100,100)
if(debug):
        print(a, b)
drawDot(a,b,5,"maroon")
##t.up()
##t.goto(a,b)
##t.down()
##t.dot(5,"green")
turtle.tracer(0, 0)
colorList = ["red","orange","yellow","green","blue","purple","pink","black","brown"]
for l in range(0,20000):
        # Choosing a random point of the triangle
        trianglePoint = random.choice(my_list)

        # Mid-point of starting number and random point of the triangle
        i,j = trianglePoint
        if(debug):
                print(i, j)
        midPoint = [(a+i)/2, (b+j)/2]
        if(debug):
                print('midpoint') 
        if(debug):
                print(midPoint)
        color = random.choice(colorList)
        drawDot((a+i)/2, (b+j)/2,3, color)
##        t.up()
##        t.goto( [(a+i)/2, (b+j)/2])
##        t.down()
##        t.dot(3,random.choice(colorList))
        # Changing starting coordinates into midPoint
        a,b = midPoint
turtle.update()

