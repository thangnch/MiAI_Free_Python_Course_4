chuoi = input("Nhap vao mot chuoi = ")
#python is good
for i in range(0, len(chuoi)):
    if chuoi[i] == " ":
        tu_dau_tien = chuoi[0:i]
        print("Tu dau tien  = {}".format(tu_dau_tien))
        break


