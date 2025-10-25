# lirik_multo.py
# Menampilkan lirik lagu "Multo - Cup of Joe" dengan efek typewriter

import sys
import time

# ======== LIRIK ========
lirik = [
    "==Multo - Cup of Joe==",
    "",
    "Hindi na makalaya",
    "Dinadalaw mo 'ko bawat gabi",
    "Wala mang nakikita",
    "Haplos mo'y ramdam pa rin sa dilim",
    "",
    "Hindi na nananaginip",
    "Hindi na ma-makagising",
    "Pasindi na ng ilaw",
    "Minumulto na 'ko ng damdamin ko",
    "Ng damdamin ko",
    "",
    "Hindi mo ba ako lilisanin?",
    "Hindi pa ba sapat pagpapahirap sa 'kin? (Damdamin ko)",
    "Hindi na ba ma-mamamayapa?",
    "Hindi na ba ma-mamamayapa?",
]

# ======== FUNGSI CETAK DENGAN EFEK KETIK ========
def ketik_barisan(baris: str, delay_per_char: float = 0.03):
    """Menampilkan satu baris teks dengan efek ketik per karakter."""
    for ch in baris:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay_per_char)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ======== FUNGSI UNTUK MENJALANKAN LIRIK ========
def jalanin_lirik(lines, char_delay=0.03, line_pause=0.6):
    """
    lines: daftar baris lirik
    char_delay: jeda per karakter (detik)
    line_pause: jeda antar baris (detik)
    """
    for baris in lines:
        if baris.strip() == "":
            time.sleep(line_pause * 1.5)
            print()
        else:
            ketik_barisan(baris, delay_per_char=char_delay)
            time.sleep(line_pause)

# ======== PROGRAM UTAMA ========
if __name__ == "__main__":
    cepat_karakter = 0.02   # semakin kecil semakin cepat
    jeda_antar_baris = 0.6
    jalanin_lirik(lirik, char_delay=cepat_karakter, line_pause=jeda_antar_baris)
