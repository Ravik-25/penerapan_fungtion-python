def hitung_ongkir(kota, berat):
    tarif_perkilo = {
        "padang": 10000,
        "jakarta": 12000,
        "bekasi": 11000,
    }

    if kota in tarif_perkilo:
        ongkir = berat * tarif_perkilo[kota]
        print(f"ongkir ke {kota} untuk berat {berat} kg adalah {ongkir})")
    else: 
        print("kota tidak ada di list")

hitung_ongkir("padang", 2)
hitung_ongkir("papua", 1)

#jadi disini kita mengunakan dictionary untuk menyimpan data tarif ongkir per kota