chuoi = input("Nhap vao chuoi =  ")
tong_in_hoa = 0
tong_in_thuong = 0
tong_ky_tu_so = 0

for c in chuoi:
    if c in "0123456789":
        tong_ky_tu_so  = tong_ky_tu_so + 1
    else:
        if c == c.upper():
            tong_in_hoa = tong_in_hoa + 1
        elif c == c.lower():
            tong_in_thuong = tong_in_thuong + 1

print("Tong chu hoa = {}, tong chu thuong = {}, tong ki tu so = {}".format(tong_in_hoa, tong_in_thuong, tong_ky_tu_so))