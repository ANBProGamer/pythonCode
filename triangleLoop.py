my_list.append([z,z])
my_list.append([y,z])
drawDot(z,z,20,"red")
drawDot(y,y,20,"red")
drawDot(y,z,20,"red")

if(debug):
        print(my_list)

turtle.bgcolor("black")
# Picking the starting coordinate
a = random.randint(-100,100)
b = random.randint(-100,100)
if(debug):
        print(a, b)
drawDot(a,b,5,"maroon")

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

        # Changing starting coordinates into midPoint
        a,b = midPoint
turtle.update()


