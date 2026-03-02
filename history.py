"""
MODUL HISTORY
Mengelola riwayat perhitungan dan export ke file
"""

from datetime import datetime
import os


class HistoryManager:
    """Kelas untuk mengelola riwayat perhitungan"""
    
    def __init__(self, max_history=10):
        """
        Inisialisasi history manager
        
        Args:
            max_history (int): Jumlah maksimal history yang disimpan
        """
        self.history = []
        self.max_history = max_history
    
    def add(self, calculation_type, input_data, result):
        """
        Menambahkan perhitungan ke history
        
        Args:
            calculation_type (str): Jenis perhitungan
            input_data (str): Data input
            result (str): Hasil perhitungan
        """
        entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': calculation_type,
            'input': input_data,
            'result': result
        }
        self.history.append(entry)
        
        # Batasi jumlah history
        if len(self.history) > self.max_history:
            self.history.pop(0)
    
    def show(self):
        """Menampilkan history perhitungan"""
        if not self.history:
            print("\n╔════════════════════════════════════════════════════════╗")
            print("║              HISTORY MASIH KOSONG                      ║")
            print("╚════════════════════════════════════════════════════════╝")
            return
        
        print("\n" + "="*70)
        print(f"RIWAYAT PERHITUNGAN ({len(self.history)}/{self.max_history} Terakhir)")
        print("="*70)
        
        for i, entry in enumerate(self.history, 1):
            print(f"\n{i}. 📅 [{entry['timestamp']}]")
            print(f"   📌 Jenis    : {entry['type']}")
            print(f"   📝 Input    : {entry['input']}")
            print(f"   ✅ Hasil    : {entry['result']}")
            print("-"*70)
    
    def export_to_file(self, filename="exports/history_kalkulator.txt"):
        """
        Mengekspor history ke file teks
        
        Args:
            filename (str): Nama file output
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            # Buat folder jika belum ada
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("="*70 + "\n")
                f.write("             RIWAYAT PERHITUNGAN KALKULATOR MULTI-FUNGSI\n")
                f.write(f"Dibuat pada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*70 + "\n\n")
                
                if not self.history:
                    f.write("Belum ada riwayat perhitungan.\n")
                else:
                    for i, entry in enumerate(self.history, 1):
                        f.write(f"{i}. [{entry['timestamp']}]\n")
                        f.write(f"   Jenis : {entry['type']}\n")
                        f.write(f"   Input : {entry['input']}\n")
                        f.write(f"   Hasil : {entry['result']}\n")
                        f.write("-"*70 + "\n")
                
                f.write("\n" + "="*70 + "\n")
                f.write("                 AKHIR LAPORAN\n")
                f.write("="*70 + "\n")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Gagal mengekspor file: {e}")
            return False
    
    def clear(self):
        """Menghapus semua history"""
        self.history.clear()
        print("\n✅ Semua history telah dihapus.")