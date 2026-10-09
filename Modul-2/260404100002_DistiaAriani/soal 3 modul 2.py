suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))
if suhu > 1000:
    if tekanan > 50 :
        status_bahaya = "MELTDOWN! SEGERA EVAKUASI!"
    else : 
        status_bahaya = "Bahaya Suhu : Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status_bahaya = "Tekanan Tidak Stabil"
    else:
        status_bahaya = "Operasi Reaktor Normal"
else:
    status_bahaya = "Reaktor Belum Cukup Panas"

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("\n------ HASIL PEMANTAUAN REAKTOR ------")
print(f"suhu Reaktor: {suhu} °C")
print(f"tekanan Gas: {tekanan} Bar")
print(f"status Bahaya: {status_bahaya}")
print(f"status Pompa air: {status_pompa}")