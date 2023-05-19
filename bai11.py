so_nho_nhat = 9999999
so_lon_nhat = -9999999
so_nhap = 0
while so_nhap!=-1:
    so_nhap = int(input("Nhap so tiep theo = "))
    if so_nhap!=-1:
        if so_nhap > so_lon_nhat:
            so_lon_nhat = so_nhap

        if so_nhap < so_nho_nhat:
            so_nho_nhat = so_nhap

print("So lon nhat = {}, so nho nhat = {}".format(so_lon_nhat, so_nho_nhat))

