def inputting():
    x1 = int(input("Input x1 numeric value: "))
    y1 = int(input("Input y1 numeric value: "))
    x2 = int(input("Input x2 numeric value: "))
    y2 = int(input("Input y2 numeric value: "))
    xvalue = int(input("Input new x value on coordinate plane established: "))
    return xvalue, x1, y1, x2, y2


def tuple_time(x1, y1, x2, y2):
    coord1 = (x1, y1)
    coord2 = (x2, y2)
    print(coord1, coord2)
    return coord1, coord2


def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    print("slope value is: ")
    print(m)
    return m


def y_val(m, xvalue, y1, x1):
    b = y1 - m*x1
    y = m*xvalue + b
    print("y value is: ")
    print(y)
    return(y)


if __name__ == "__main__":
    xval, x1, y1, x2, y2 = inputting()
    coor1, coor2 = tuple_time(x1, y1, x2, y2)
    slopeing = slope(x1, y1, x2, y2)
    yval = y_val(slopeing, xval, y1, x1)
