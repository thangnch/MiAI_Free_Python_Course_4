a = int(input("Nhao vao so a="))
so_uoc = 0
for so in range(1,a):
    if a % so ==0:
        so_uoc = so_uoc + 1
print("So uoc cua a = ", so_uoc)