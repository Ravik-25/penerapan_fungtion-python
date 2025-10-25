def cek_status_driver(jaket_dipakai, aplikasi_menyala):
    if jaket_dipakai and aplikasi_menyala:
        print("sedang bekerja")
    elif jaket_dipakai:
        print("sedang menunggu orderan")
    else:
        print("sedang tidak berkerja")
        
cek_status_driver(False, False)
