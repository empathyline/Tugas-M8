daftar_karyawan = [("Joko", "IT", 7000), ("Rina", "HR", 5000), ("Toni", "Data", 8000), ("Lia", "IT", 6500)]
total_gaji_gabungan = 0

for nama, divisi, gaji in daftar_karyawan:
    if divisi in ("IT", "Data"):
        total_gaji_gabungan += gaji

print(f"Total gaji karyawan IT dan Data adalah ${total_gaji_gabungan:,.2f}")

print("-" * 40)

#New

for baris in range(1, 5):
    for kolom in range(1, 5):
        print("*", end=" ")
    print("*")

print("-" * 40)