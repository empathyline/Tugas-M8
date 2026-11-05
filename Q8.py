data_penjualan = [("Kopi", 60, False), ("Teh", 30, False), ("Boba", 80, True)]
ambang_batas = 50

for item, terjual, sedang_promo in data_penjualan:
    if terjual > ambang_batas and not sedang_promo:
        print(f"Selamat produk {item} laku keras dengan jumlah minuman sebanyak {terjual}")
    elif sedang_promo and terjual > ambang_batas:
        print(f"Maaf produk {item}, belum laris tanpa adanya promo, silakan jual lagi!")
    else:
        print(f"Produk {item} masih belum laris, silakan buat inovasi lagi!")