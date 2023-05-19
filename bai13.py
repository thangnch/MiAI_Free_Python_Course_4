n = input("Nhap vao so nguyen duong = ") # N se la chuoi ki tu
tong_chan = 0
tong_le = 0
for c in n: # Duyet qua tung chu so trong N
    so = int(c)
    if so % 2==0:
        tong_chan = tong_chan + 1
    else:
        tong_le = tong_le  + 1

print("So luong chu so le = {}, so luong chu so chan = {}".format(tong_le, tong_chan))

