#coordinate determining 

def input_val(in1, in2, x):
    print("Input x1,y1,x2,y2 values as parameters")
    x1, y1 = in1[:]
    x1 = float(x1)
    y1 = float(y1)
    x2, y2 = in2[:]
    x2 = float(x2)
    y2 = float(y2)
    print("You chose: ")
    print(x1,y1,x2,y2)
    print("Input x coordinate parameter: ")
    m = slope_calc(x1,y1,x2,y2)
    y = y_val(x1,y1,m,x)
    print("The y value coordinate is: ")
    print(y)
    return y

def slope_calc(xx1,yy1,xx2,yy2):
    m1 = (yy1-yy2)/(xx1-xx2)
    return m1

def y_val(xxx1,yyy1,mm1,xxx):
    yval = ((xxx-xxx1)*mm1)+yyy1
    return yval
    

if __name__ == "__main__":
    input1 = tuple(input("Choice value of x1 and y1(type space between):").split())
    input2 = tuple(input("Choice value of x2 and y2 (type space between):").split())
    x = int(input("Choice value of x: "))
    input_val(input1,input2,x)
    
    