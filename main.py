print("ax + by = e")
print("cx + dy = f")
a = float(input("Enter 'a' : "))
b = float(input("Enter 'b' : "))
c = float(input("Enter 'c' : "))
d = float(input("Enter 'd' : "))
e = float(input("Enter 'e' : "))
f = float(input("Enter 'f' : "))
def Cramers_Rule_2_Equations():
    det = ((a*d)-(b*c))
    if det==0:
        print("Determinant cannot equal to 0")
    det_x = ((e*d)-(f*b))
    det_y = ((a*f)-(c*e))
    x = det_x/det
    y = det_y/det
    return x,y
print("x and y :",Cramers_Rule_2_Equations())
