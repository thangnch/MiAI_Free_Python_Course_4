import math
so = int(input("Nhap vao s = "))

#9 -> 3
#8 -> khong chinh phuong
can_bac_hai = int(math.sqrt(so))

if can_bac_hai * can_bac_hai == so:
    print("Chinh phuong")
else:
    print("Khong chinh phuong")