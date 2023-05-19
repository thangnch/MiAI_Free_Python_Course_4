thang = int(input("Nhap vao thang = "))
nam = int(input("Nhap vao nam = "))

# Bo qua kiem tra dieu kien thang (1-12) va nam phai hop le
# Rule de giai
# - Neu nam % 4 -> nam nhuan:
# + thang 2 no co 29 ngay
# + THang 1,3,5,7,8,10,12: 31 ngay
# + Thang con lai: 30 ngay
# - Neu nam % 4 khong chia het -> nam khong nhuan:
# + thang 2 no co 28 ngay
# + THang 1,3,5,7,8,10,12: 31 ngay
# + Thang con lai: 30 ngay

if nam % 4 ==0 : # Chia het cho 4 -> nam nhuan
    # Tinh toan voi nam nhuan
    if thang == 2:
        print("Thang co 29 ngay!")
    elif (thang == 1 ) or (thang==3) or (thang==5) or (thang==7) or (thang==8) or (thang==10) or (thang==12):
        print("Thang co 31 ngay!")
    else:
        print("Thang co 30 ngay!")
else: # Nam khong nhuan
    # Tinh toan voi nam khong nhuan
    if thang == 2:
        print("Thang co 28 ngay!")
    elif (thang == 1) or (thang == 3) or (thang == 5) or (thang == 7) or (thang == 8) or (thang == 10) or (thang == 12):
        print("Thang co 31 ngay!")
    else:
        print("Thang co 30 ngay!")