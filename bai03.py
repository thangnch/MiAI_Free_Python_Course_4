import math
# Giải và biện luận phương trình ax^2 + bx + c = 0
a = float(input("Nhap vao a ="))
b = float(input("Nhap vao b ="))
c = float(input("Nhap vao c ="))

# Tinh delta
delta = b**2 - 4*a*c

if delta < 0:
    print("Phuong trinh vo nghiem!")
elif delta==0:
    print("Phuong trinh co nghiem kep =  ", -b/(2*a))
else:
    nghiem_1 = ( -b + math.sqrt(delta) ) / (2*a)
    nghiem_2 = ( -b - math.sqrt(delta) ) / (2*a)
    print("Phuong trinh co 2 nghiem x1= {} va x2={}".format(nghiem_1, nghiem_2))
