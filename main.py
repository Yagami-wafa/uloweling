"""
SISTEM KALKULATOR MULTI-FUNGSI
Program utama yang mengintegrasikan semua modul kalkulator
"""

import os
import sys
from datetime import datetime

# Menambahkan path untuk import modul
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from history import HistoryManager
from modules.aritmatika import KalkulatorAritmatika
from modules.suhu import KalkulatorSuhu
from modules.bilangan import KalkulatorBilangan
from bonus.ip_calculator import KalkulatorIP
from utils.validators import input_angka, input_ya_tidak
from utils.helpers import clear_screen, tampilkan_header, tampilkan_footer


class KalkulatorMultiFungsi:
    """Kelas utama yang mengintegrasikan semua fitur kalkulator"""
    
    def __init__(self):
        """Inisialisasi history manager dan semua modul kalkulator"""
        self.history = HistoryManager()
        self.kalkulator_aritmatika = KalkulatorAritmatika(self.history)
        self.kalkulator_suhu = KalkulatorSuhu(self.history)
        self.kalkulator_bilangan = KalkulatorBilangan(self.history)
        self.kalkulator_ip = KalkulatorIP(self.history)
        
    def tampilkan_menu_utama(self):
        """Menampilkan menu utama aplikasi"""
        clear_screen()
        tampilkan_header("SISTEM KALKULATOR MULTI-FUNGSI")
        print("""
    ╔════════════════════════════════════════════════════════╗
    ║                     MENU UTAMA                         ║
    ╠════════════════════════════════════════════════════════╣
    ║  1. Kalkulator Aritmatika                              ║
    ║  2. Kalkulator Suhu                                    ║
    ║  3. Kalkulator Konversi Bilangan                       ║
    ║  4. Riwayat Perhitungan                                ║
    ║  5. Export Hasil ke File                               ║
    ║  6. Kalkulator IP Address (BONUS)                      ║
    ║  0. Keluar                                             ║
    ╚════════════════════════════════════════════════════════╝
        """)
        
    def jalankan(self):
        """Menjalankan program utama"""
        while True:
            self.tampilkan_menu_utama()
            
            pilihan = input_angka("Pilih menu (0-6): ", 0, 6)
            
            if pilihan == 0:
                print("\n" + "="*60)
                print("Terima kasih telah menggunakan Kalkulator Multi-Fungsi!")
                print("="*60)
                # Tanya apakah ingin menyimpan history sebelum keluar
                if self.history.history and input_ya_tidak("\nSimpan history ke file sebelum keluar? (y/n): "):
                    self.history.export_to_file()
                break
                
            elif pilihan == 1:
                self.kalkulator_aritmatika.menu()
                
            elif pilihan == 2:
                self.kalkulator_suhu.menu()
                
            elif pilihan == 3:
                self.kalkulator_bilangan.menu()
                
            elif pilihan == 4:
                clear_screen()
                tampilkan_header("RIWAYAT PERHITUNGAN")
                self.history.show()
                input("\nTekan Enter untuk kembali ke menu utama...")
                
            elif pilihan == 5:
                clear_screen()
                tampilkan_header("EXPORT HASIL KE FILE")
                if not self.history.history:
                    print("\n⚠️  History masih kosong! Tidak ada data untuk diekspor.")
                else:
                    filename = input("Masukkan nama file (default: history_kalkulator.txt): ").strip()
                    if not filename:
                        filename = "exports/history_kalkulator.txt"
                    elif not filename.endswith('.txt'):
                        filename += '.txt'
                    
                    # Pastikan folder exports ada
                    os.makedirs("exports", exist_ok=True)
                    
                    if self.history.export_to_file(filename):
                        print(f"\n✅ History berhasil diekspor ke {filename}")
                
                input("\nTekan Enter untuk kembali ke menu utama...")
                
            elif pilihan == 6:
                self.kalkulator_ip.menu()


if __name__ == "__main__":
    try:
        app = KalkulatorMultiFungsi()
        app.jalankan()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\nTerjadi error: {e}")
        print("Program akan ditutup.")