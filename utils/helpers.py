"""
MODUL HELPER
Fungsi-fungsi pembantu untuk tampilan dan utilitas
"""

import os


def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_header(judul):
    """
    Menampilkan header dengan format yang rapi
    
    Args:
        judul (str): Judul header
    """
    print("="*70)
    print(f"{judul:^70}")
    print("="*70)


def tampilkan_footer():
    """Menampilkan footer"""
    print("\n" + "="*70)


def format_angka(angka, desimal=2):
    """
    Memformat angka dengan pemisah ribuan
    
    Args:
        angka (float): Angka yang akan diformat
        desimal (int): Jumlah desimal
        
    Returns:
        str: Angka terformat
    """
    return f"{angka:,.{desimal}f}".replace(",", ".")