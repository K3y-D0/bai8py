kho = {
    "sua tuoi": 25000,
    "banh mi": 15000,
    "trung ga": 35000,
    "ca phe": 60000,
    "duong": 20000
}
print(kho.items())

ten = input("Nhap ten san pham can tra gia: ")
gia = kho.get(ten)

if gia is not None :
    print(f"Gia san pham: {gia} VND")
else:
    print("San pham khong ton tai!")

print("\nDanh sach san pham theo gia tang dan:")

danh_sach = list(kho.items())

for i in range(len(danh_sach)):
    for j in range(i + 1, len(danh_sach)):
        if danh_sach[i][1] > danh_sach[j][1]:
            tam = danh_sach[i]
            danh_sach[i] = danh_sach[j]
            danh_sach[j] = tam

for ten_sp, gia_sp in danh_sach:
    print(f"{ten_sp} : {gia_sp} VND")

print("\nTong don gia mot don vi moi mat hang:")

tong = 0
for ten_sp, gia_sp in kho.items():
    print(f"{ten_sp} : {gia_sp} VND")
    tong = tong + gia_sp

print(f"Tong tien: {tong} VND")
