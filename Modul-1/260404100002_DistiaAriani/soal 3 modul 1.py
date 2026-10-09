bahan_bakar_per_liter = 40
jarak = 100
sisa_bahan_bakar = 1.5
harga_bahan_bakar_per_liter = 10000


total_jarak = jarak * 2
print("total jarak: ", total_jarak)

kebutuhan_bahan_bakar = total_jarak / bahan_bakar_per_liter
print("kebutuhan bahan bakar: ", kebutuhan_bahan_bakar) 

bahan_bakar_dibeli = kebutuhan_bahan_bakar - sisa_bahan_bakar
print("bahan bakar yang dibeli: ", bahan_bakar_dibeli)

total_biaya = bahan_bakar_dibeli * harga_bahan_bakar_per_liter
print("total biaya: ", total_biaya)
