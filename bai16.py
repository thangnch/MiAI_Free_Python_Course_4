chuoi = input("Nhap vao dang a,b,c = ")
# No lai sau
arr = chuoi.split(",")
tong = 0
for so in arr:
    tong = tong + int(so)

print("Tong  = ", tong)
