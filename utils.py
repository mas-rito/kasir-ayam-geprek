from datetime import datetime
from tabulate import tabulate

def format_rupiah(angka):
    return f"Rp {angka:,.2f}"

def waktu_sekarang():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def show_menus(daftar_menu):
    print("Daftar Menu:")
    menu_bernomor = [(index + 1, menu, format_rupiah(harga)) for index, (menu, harga) in enumerate(daftar_menu.items())]
    # Membuat tabel dengan tabulate
    tabel_menu = tabulate(menu_bernomor, headers=["No", "Menu", "Harga"], tablefmt="grid")
    print(tabel_menu)