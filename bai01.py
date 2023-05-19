toan = float(input("Nhập vào điểm toán = "))
van = float(input("Nhập vào điểm văn = "))
anh = float(input("Nhập vào điểm anh = "))
if (0 <= toan <= 10) and (0 <= van <=10) and (0<=anh<=10):
    # Thuc hien tinh toan
    trung_binh = (toan + van + anh)/3
    print("Diem trung binh = ", trung_binh)
    if (trung_binh>=8) and ( (toan>=8)or(van>=8) ) and (toan>=6.5) and (van>=6.5) and (anh>=6.5):
        print("Hoc sinh gioi!")
    else:
        if (trung_binh>=6.5) and ( (toan>=6.5)or(van>=6.5) ) and (toan>=5) and (van>=5) and (anh>=5):
            print("Hoc sinh kha")
        else:
            if (trung_binh >= 5) and ((toan >= 5) or (van >= 5)) and (toan >= 3.5) and (van >= 3.5) and (anh >= 3.5):
                print("Hoc sinh trung binh")
            else:
                if (trung_binh >= 3.5) and ((toan >= 3.5) or (van >= 3.5)) and (toan >= 2) and (van >= 2) and (anh >= 2):
                    print("Hoc sinh yeu")
                else:
                    print("Hoc sinh kem")

else:
    print("Diem nhap vao khong hop le!")