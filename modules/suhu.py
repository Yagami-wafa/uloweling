"""
MODUL KALKULATOR SUHU (SOAL 2)
Mendukung konversi antar 4 skala suhu: Celsius, Fahrenheit, Kelvin, Reaumur
"""


class KalkulatorSuhu:
    """Kelas untuk kalkulator konversi suhu"""
    
    def __init__(self, history_manager):
        """
        Inisialisasi kalkulator suhu
        
        Args:
            history_manager: Object untuk mengelola history
        """
        self.history = history_manager
        self.skala = {
            'C': ('Celsius', '°C'),
            'F': ('Fahrenheit', '°F'),
            'K': ('Kelvin', 'K'),
            'R': ('Reaumur', '°R')
        }
    
    def menu(self):
        """Menu utama kalkulator suhu"""
        while True:
            print("\n" + "="*60)
            print("          KALKULATOR SUHU")
            print("="*60)
            print("╔════════════════════════════════════════════════╗")
            print("║  1. Konversi Satuan                            ║")
            print("║  2. Tabel Konversi                              ║")
            print("║  3. Klasifikasi Suhu                            ║")
            print("║  0. Kembali ke Menu Utama                       ║")
            print("╚════════════════════════════════════════════════╝")
            
            try:
                pilihan = int(input("\nPilih menu: "))
                
                if pilihan == 0:
                    break
                elif pilihan == 1:
                    self.konversi_satuan()
                elif pilihan == 2:
                    self.tabel_konversi()
                elif pilihan == 3:
                    self.klasifikasi_suhu()
                else:
                    print("❌ Pilihan tidak valid!")
                    
            except ValueError:
                print("❌ Input harus berupa angka!")
    
    def konversi_celsius_ke(self, nilai, tujuan):
        """
        Konversi dari Celsius ke skala lain
        
        Args:
            nilai (float): Nilai dalam Celsius
            tujuan (str): Skala tujuan (F/K/R)
            
        Returns:
            float: Hasil konversi
        """
        if tujuan == 'F':
            return (nilai * 9/5) + 32
        elif tujuan == 'K':
            return nilai + 273.15
        elif tujuan == 'R':
            return nilai * 4/5
        else:  # C
            return nilai
    
    def konversi_fahrenheit_ke(self, nilai, tujuan):
        """
        Konversi dari Fahrenheit ke skala lain
        
        Args:
            nilai (float): Nilai dalam Fahrenheit
            tujuan (str): Skala tujuan
            
        Returns:
            float: Hasil konversi
        """
        # Ke Celsius dulu
        celsius = (nilai - 32) * 5/9
        return self.konversi_celsius_ke(celsius, tujuan)
    
    def konversi_kelvin_ke(self, nilai, tujuan):
        """
        Konversi dari Kelvin ke skala lain
        
        Args:
            nilai (float): Nilai dalam Kelvin
            tujuan (str): Skala tujuan
            
        Returns:
            float: Hasil konversi
        """
        # Ke Celsius dulu
        celsius = nilai - 273.15
        return self.konversi_celsius_ke(celsius, tujuan)
    
    def konversi_reaumur_ke(self, nilai, tujuan):
        """
        Konversi dari Reaumur ke skala lain
        
        Args:
            nilai (float): Nilai dalam Reaumur
            tujuan (str): Skala tujuan
            
        Returns:
            float: Hasil konversi
        """
        # Ke Celsius dulu
        celsius = nilai * 5/4
        return self.konversi_celsius_ke(celsius, tujuan)
    
    def konversi(self, nilai, asal, tujuan):
        """
        Fungsi utama konversi suhu
        
        Args:
            nilai (float): Nilai suhu
            asal (str): Skala asal
            tujuan (str): Skala tujuan
            
        Returns:
            float: Hasil konversi
        """
        if asal == tujuan:
            return nilai
        
        if asal == 'C':
            return self.konversi_celsius_ke(nilai, tujuan)
        elif asal == 'F':
            return self.konversi_fahrenheit_ke(nilai, tujuan)
        elif asal == 'K':
            return self.konversi_kelvin_ke(nilai, tujuan)
        elif asal == 'R':
            return self.konversi_reaumur_ke(nilai, tujuan)
    
    def klasifikasi(self, celsius):
        """
        Mengklasifikasikan suhu berdasarkan Celsius
        
        Args:
            celsius (float): Suhu dalam Celsius
            
        Returns:
            str: Klasifikasi suhu
        """
        if celsius <= 0:
            return "Beku"
        elif celsius <= 15:
            return "Dingin"
        elif celsius <= 25:
            return "Normal"
        elif celsius <= 35:
            return "Panas"
        else:
            return "Sangat Panas"
    
    def konversi_satuan(self):
        """Fungsi untuk konversi satuan suhu"""
        print("\n" + "─"*50)
        print("           KONVERSI SATUAN SUHU")
        print("─"*50)
        print("Skala yang tersedia:")
        for kode, (nama, simbol) in self.skala.items():
            print(f"  {kode} = {nama} ({simbol})")
        print("─"*50)
        
        try:
            asal = input("Dari (C/F/K/R): ").strip().upper()
            if asal not in self.skala:
                print("❌ Skala asal tidak valid!")
                return
            
            tujuan = input("Ke (C/F/K/R): ").strip().upper()
            if tujuan not in self.skala:
                print("❌ Skala tujuan tidak valid!")
                return
            
            nilai = float(input(f"Nilai ({self.skala[asal][0]}): "))
            
            # Konversi
            hasil = self.konversi(nilai, asal, tujuan)
            
            # Konversi ke Celsius untuk klasifikasi
            celsius = self.konversi(nilai, asal, 'C')
            klasifikasi = self.klasifikasi(celsius)
            
            print(f"\n✅ Hasil: {nilai}{self.skala[asal][1]} = {hasil:.2f}{self.skala[tujuan][1]}")
            print(f"📊 Klasifikasi: {klasifikasi}")
            
            # Tampilkan rumus yang digunakan
            print("\nRumus yang digunakan:")
            if asal == 'C' and tujuan == 'F':
                print(f"  {nilai}°C × 9/5 + 32 = {hasil:.2f}°F")
            elif asal == 'C' and tujuan == 'K':
                print(f"  {nilai}°C + 273.15 = {hasil:.2f}K")
            elif asal == 'C' and tujuan == 'R':
                print(f"  {nilai}°C × 4/5 = {hasil:.2f}°R")
            elif asal == 'F' and tujuan == 'C':
                print(f"  ({nilai}°F - 32) × 5/9 = {hasil:.2f}°C")
            elif asal == 'K' and tujuan == 'C':
                print(f"  {nilai}K - 273.15 = {hasil:.2f}°C")
            
            self.history.add("Suhu - Konversi", 
                           f"{nilai}{self.skala[asal][1]} → {tujuan}", 
                           f"{hasil:.2f}{self.skala[tujuan][1]} ({klasifikasi})")
            
        except ValueError:
            print("❌ Input suhu harus berupa angka!")
    
    def tabel_konversi(self):
        """Menampilkan tabel konversi untuk rentang suhu"""
        print("\n" + "─"*60)
        print("           TABEL KONVERSI SUHU")
        print("─"*60)
        print("Rentang: 0°C - 100°C dengan step 10°C")
        print("─"*60)
        
        # Header tabel
        print(f"{'Celsius (°C)':^15} {'Fahrenheit (°F)':^18} {'Kelvin (K)':^15} {'Reaumur (°R)':^15}")
        print("─"*60)
        
        for c in range(0, 101, 10):
            f = self.konversi_celsius_ke(c, 'F')
            k = self.konversi_celsius_ke(c, 'K')
            r = self.konversi_celsius_ke(c, 'R')
            print(f"{c:^15.1f} {f:^18.2f} {k:^15.2f} {r:^15.2f}")
        
        print("─"*60)
        self.history.add("Suhu - Tabel", "0°C - 100°C (step 10)", "Tabel ditampilkan")
    
    def klasifikasi_suhu(self):
        """Menampilkan klasifikasi suhu"""
        print("\n" + "─"*50)
        print("           KLASIFIKASI SUHU")
        print("─"*50)
        print("Klasifikasi berdasarkan skala Celsius:")
        print("  ╔══════════════╦════════════════════╗")
        print("  ║ Rentang (°C) ║    Klasifikasi     ║")
        print("  ╠══════════════╬════════════════════╣")
        print("  ║ ≤ 0          ║ Beku               ║")
        print("  ║ 1 - 15       ║ Dingin             ║")
        print("  ║ 16 - 25      ║ Normal             ║")
        print("  ║ 26 - 35      ║ Panas              ║")
        print("  ║ > 35         ║ Sangat Panas       ║")
        print("  ╚══════════════╩════════════════════╝")
        
        try:
            suhu = float(input("\nMasukkan suhu dalam Celsius: "))
            klasifikasi = self.klasifikasi(suhu)
            
            # Tampilkan dengan warna (simbol)
            if klasifikasi == "Beku":
                emoji = "❄️"
            elif klasifikasi == "Dingin":
                emoji = "🌡️"
            elif klasifikasi == "Normal":
                emoji = "😊"
            elif klasifikasi == "Panas":
                emoji = "🔥"
            else:
                emoji = "🥵"
            
            print(f"\n{emoji} {suhu}°C termasuk kategori: {klasifikasi.upper()}")
            self.history.add("Suhu - Klasifikasi", f"{suhu}°C", klasifikasi)
            
        except ValueError:
            print("❌ Input harus berupa angka!")