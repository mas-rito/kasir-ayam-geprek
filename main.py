import json
from utils import format_rupiah, waktu_sekarang, show_menus

# kode Rincian toko
toko_nama = "====== Ayam Geprek Selamet ======"
toko_alamat = "Jl. Selamet No. 1"
toko_nomor_telepon = "083814336508"

# Daftar menu
with open("menu.json", "r") as file:
    daftar_menu = json.load(file)

# Tampilkan rincian toko
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 36)


# Tampilkan daftar menu
show_menus()

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
print("=" * 36)
print('Total belanja: ', format_rupiah(total_harga))
uang_pelanggan = float(input("Input uang: "))

# Tampilkan struk
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 36)
print("=" * 36)
print("Menu yang dipesan:")
for item, jumlah in pesanan.items():
    print(f"{item}: {jumlah}")
print("Total: ", total_harga)
if diskon > 0:
    print(f"Diskon: {diskon}")
print("Uang: ", uang_pelanggan)
print("Kembalian: ", uang_pelanggan - total_harga)
print("=" * 36)
print("Barang yang sudah dibeli tidak dapat dikembalikan")
print("=" * 36)
print(waktu_sekarang())