chuoi = input("Nhap vao chuoi =  ")
manh = False
co_ki_tu_dac_biet = False
co_ki_tu_hoa = False
co_ki_tu_so = False
co_ki_tu_thuong = False

if len(chuoi) >6:
    for c in chuoi:
        if c in "0123456789":
            co_ki_tu_so = True
        elif c in "@~*&^%$#": # Dinh nghia tam de lam bai
            co_ki_tu_dac_biet = True
        else:
            if c == c.upper():
                co_ki_tu_hoa = True
            if c == c.lower():
                co_ki_tu_thuong = True

    manh = co_ki_tu_so and co_ki_tu_dac_biet and co_ki_tu_hoa and co_ki_tu_thuong

if manh:
    print("Mat khau manh")
else:
    print("Mat khau yeu")
