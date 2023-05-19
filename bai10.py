a = int(input("Nhao vao so a="))
nguyen_to = True # Gia dinh la so nguyen to

for so in range(2,a):
    if a % so ==0:
        nguyen_to = False
        break

if nguyen_to:
    print("Day la so nguyen to")
else:
    print("Day khong phai la so nguyen to")
