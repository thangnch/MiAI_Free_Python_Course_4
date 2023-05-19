a = int(input("Nhap vao so a="))
b = int(input("Nhap vao so b="))
so_nho_hon = min(a,b)

for so in range(1, so_nho_hon):
    if (a%so==0) and (b%so==0):
        print(so)

