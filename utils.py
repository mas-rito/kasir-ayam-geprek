from datetime import datetime

def format_rupiah(angka):
    return f"Rp {angka:,.2f}"

def waktu_sekarang():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")