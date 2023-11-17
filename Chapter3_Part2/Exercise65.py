import math
Chuvi=0
khoangcach=0
x1=0
y1=0
x_first=None
y_first=None
while True:
    x=input("Enter the x part of the coordinate: ")    
    if x=="":
        break        
    else:
        y=float(input("Enter the y part of the coordinate: "))
        if x_first==None:
            x_first=float(x)
            y_first=y
        else:
            khoangcach=math.sqrt((float(x)-x1)**2+(y-y1)**2)
            Chuvi = Chuvi+khoangcach
        x1=float(x)
        y1=y
if x_first is not None:
    khoangcach=math.sqrt((float(x_first)-x1)**2+(float(y_first)-y1)**2) #Tính khoảng cách từ điểm đầu đến điểm cuối
    Chuvi=Chuvi+khoangcach
print("The perimeter of that polygon is", Chuvi)

