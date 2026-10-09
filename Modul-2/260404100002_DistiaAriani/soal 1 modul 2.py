kode = int(input("masukkan kode rahasia 3 digit: "))

digit1= kode // 100
digit2= (kode // 10) % 10
digit3= kode % 10

pelacakan_awal = digit1 * digit3

if digit2 % 2 == 1 :
    pelacak_tahap_pertama = pelacakan_awal + 25
else :
    pelacak_tahap_pertama = pelacakan_awal - digit2
if pelacak_tahap_pertama % 3 == 0 :
    pelacak_akhir = pelacak_tahap_pertama // 3
else :
    pelacak_akhir = pelacak_tahap_pertama * 2

if pelacak_akhir > 50 :
    status = "password terdeteksi sebagai kategori A"
elif pelacak_akhir > 20 :
    status = "password terdeteksi sebagai kategori B"
else :
    status = "password salah, silahkan coba lagi" 

print ("=== HASIL EVALUASI PASSWORD BRANKAS ===")
print ("Digit 1: ", digit1)
print ("Digit 2: ", digit2)
print ("Digit 3: ", digit3)
print ("Nilai Pelacakan Awal: ", pelacakan_awal)
print ("setelah Tahap Pertama: ", pelacak_tahap_pertama)
print ("Nilai Akhir: ", pelacak_akhir)
print ("Status: ", status) 