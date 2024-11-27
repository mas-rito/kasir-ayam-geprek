import json
from utils import format_rupiah, waktu_sekarang, show_menus

# kode Rincian toko
toko_nama = "======================= Ayam Geprek Pakde Bagong ======================="
toko_alamat = "Jl. Selamet No. 1"
toko_nomor_telepon = "083814336508"

# Daftar menu
with open("menu.json", "r") as file:
    daftar_menu = json.load(file)

# Tampilkan rincian toko
print(toko_nama)
print(toko_alamat.center(72))
print(toko_nomor_telepon.center(72))
print("=" * 72)


# Tampilkan daftar menu
show_menus(daftar_menu)

pesanan = {}
total_harga = 0

while True:
    pilihan = input("Pilih menu (1-7) atau ketik 'selesai' untuk mengakhiri pesanan: ")
    if pilihan.lower() == 'selesai':
        break
    elif not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(daftar_menu):
        print("Pilihan tidak valid.")
    else:
        indeks_menu = int(pilihan) - 1
        menu_terpilih = list(daftar_menu.keys())[indeks_menu]
        jumlah = input(f"Jumlah {menu_terpilih} yang dipesan: ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah tidak valid. Harap masukkan angka positif.")
            jumlah = input(f"Jumlah {menu_terpilih} yang dipesan: ")
        jumlah = int(jumlah)
        total_harga += daftar_menu[menu_terpilih] * jumlah
        pesanan[menu_terpilih] = jumlah

# Diskon 15% jika total harga lebih dari 100rb
# Diskon 20% jika total harga lebih dari 200rb
diskon = 0
if total_harga > 100000:
    diskon = 0.15 * total_harga
elif total_harga > 200000:
    diskon = 0.2 * total_harga

# Input uang dari pelanggan
print("=" * 72)
print('Total belanja: ', format_rupiah(total_harga))
uang_pelanggan = float(input("Input uang: "))

# Tampilkan struk
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 72)
for item, jumlah in pesanan.items():
    print(f"{item:<68}{jumlah:>4}")
print("=" * 72)
print(f"{'Total:':<58} {format_rupiah(total_harga):>12}")
if diskon > 0:
    print(f"{'Diskon:':<59} {format_rupiah(int(diskon)):>12}")
print(f"{'Uang:':<58} {format_rupiah(int(uang_pelanggan)):>12}")
print(f'{"Kembalian:":<59} {format_rupiah(int(uang_pelanggan - total_harga)):>12}')
print("=" * 72)
print("Terimakasih telah berbelanja di toko kami.".center(72))
print("=" * 72)
print(waktu_sekarang().center(72))