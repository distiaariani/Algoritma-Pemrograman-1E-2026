
pin = int(input("Masukkan 3 digit PIN : "  ))
jam = int(input("Masukkan jam (0-23): "  ))

d1 = pin // 100
d2 = (pin // 10) % 10
d3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        pesan = "Garasi Pagi Terbuka"
    else :
        pesan = "Garasi Malam Terbuka, Lampu Dinyalakan" 
elif pin % 2 == 0:
    if d1 + d3 == d2:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan = "Akses Ditolak Sepenuhnya"

cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("\n--Digit PIN: ", d1, ",", d2, ",", d3)
print("Status Pintu:", pesan)
print("Status CCTV:", cctv)