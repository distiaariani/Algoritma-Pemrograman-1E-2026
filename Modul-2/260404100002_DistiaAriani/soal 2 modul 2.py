total_awal = int(input("Masukkan total belanja awal (Rp): "))

if total_awal % 100000 == 0:
    diskon = 100
elif total_awal % 50000 == 0:
    diskon = 50
elif total_awal % 10000 == 0:
    diskon = 20
elif total_awal >= 200000:
    diskon = 10
else:
    diskon = 0

potongan = int(total_awal * diskon / 100)
total_akhir = int(total_awal - potongan)
status_poin = "Poin bertambah" if total_awal > 0 else "tidak ada poin"


print("\n------ hasil belanja siti ------")
print("Total belanja awal: Rp", total_awal)
print("Diskon:", diskon, "%" )
print("Potongan: Rp", potongan)
print("Total akhir: Rp", total_akhir)
print("Status poin:", status_poin)
