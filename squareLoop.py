import random
import turtle
debug = 0
t = turtle.Pen()

my_list = []

# Picks three co-ordinates to form the triangle

    
y = (-300)
z = (300)
my_list.append([y,y])
my_list.append([z,z])
my_list.append([y,z])
my_list.append([z,y])
t.up()
t.goto(z,z)
t.down()
t.dot(20,"red")
t.up()
t.goto(y,y)
t.down()
t.dot(20,"red")
t.up()
t.goto(y,z)
t.down()
t.dot(20,"red")
t.up()
t.goto(z,y)
t.down()
t.dot(20,"red")
if(debug):
        print(my_list)

# Picking the starting coordinate
a = random.randint(-300,300)
b = random.randint(-300,300)
if(debug):
        print(a, b)
t.up()
t.goto(a,b)
t.down()
t.dot(20,"sandybrown")
turtle.tracer(0, 0)
colorList = ["yellow","gold","orange","red","maroon","violet","magenta","purple","navy","blue","skyblue","cyan","turquoise","lightgreen","green","darkgreen","chocolate","brown","black","gray"]
for l in range(0,40000):
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
        t.up()
        t.goto( [(a+i)/2, (b+j)/2])
        t.down()
        t.dot(3,random.choice(colorList))
        # Changing starting coordinates into midPoint
        a,b = midPoint
turtle.update()
