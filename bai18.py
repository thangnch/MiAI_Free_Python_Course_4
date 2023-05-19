chuoi = input("Nhap vao chuoi =  ")
tong = 0

for c in chuoi:
    if c in "0123456789":
        tong = tong + int(c)

print("Tong cac ki tu so = ", tong)