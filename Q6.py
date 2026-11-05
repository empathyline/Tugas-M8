daftar_pelamar = [("Budi", 3.2, 5), ("Siti", 3.6, 3), ("Dodi", 3.8, 1)]
for nama, ipk, pengalaman in daftar_pelamar:
    if ipk >= 3.5 and pengalaman > 2:
        print(f"Selamat anda diterima {nama}")
    else:
        print(f"Anda ditolak {nama}")

print("-" * 40)