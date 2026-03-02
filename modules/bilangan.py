"""
MODUL KALKULATOR BILANGAN (SOAL 3)
Mendukung konversi antar basis dan operasi aritmatika non-desimal
"""


class KalkulatorBilangan:
    """Kelas untuk kalkulator konversi bilangan dan operasi aritmatika non-desimal"""
    
    def __init__(self, history_manager):
        """
        Inisialisasi kalkulator bilangan
        
        Args:
            history_manager: Object untuk mengelola history
        """
        self.history = history_manager
        self.basis = {
            'DES': ('Desimal', 'Base 10'),
            'BIN': ('Biner', 'Base 2'),
            'OKT': ('Oktal', 'Base 8'),
            'HEX': ('Heksadesimal', 'Base 16')
        }
        self.heksa_digit = "0123456789ABCDEF"
    
    def menu(self):
        """Menu utama kalkulator bilangan"""
        while True:
            print("\n" + "="*60)
            print("          KALKULATOR BILANGAN")
            print("="*60)
            print("╔════════════════════════════════════════════════╗")
            print("║  1. Konversi Basis                             ║")
            print("║  2. Operasi Aritmatika Non-Desimal             ║")
            print("║  0. Kembali ke Menu Utama                       ║")
            print("╚════════════════════════════════════════════════╝")
            
            try:
                pilihan = int(input("\nPilih menu: "))
                
                if pilihan == 0:
                    break
                elif pilihan == 1:
                    self.konversi_basis()
                elif pilihan == 2:
                    self.operasi_non_desimal()
                else:
                    print("❌ Pilihan tidak valid!")
                    
            except ValueError:
                print("❌ Input harus berupa angka!")
    
    # ==================== FUNGSI KONVERSI ====================
    
    def desimal_ke_biner(self, n, tampilkan_langkah=True):
        """
        Konversi desimal ke biner dengan menampilkan langkah
        
        Args:
            n (int): Bilangan desimal
            tampilkan_langkah (bool): Menampilkan langkah konversi
            
        Returns:
            str: Bilangan biner
        """
        if n == 0:
            return "0"
        
        if tampilkan_langkah:
            print("\n📝 Langkah konversi desimal ke biner (pembagian beruntun):")
            print("   " + "─"*40)
        
        angka = n
        sisa_list = []
        
        while angka > 0:
            sisa = angka % 2
            sisa_list.append(sisa)
            if tampilkan_langkah:
                print(f"   {angka} / 2 = {angka//2} sisa {sisa} ↑")
            angka = angka // 2
        
        if tampilkan_langkah:
            print("   " + "─"*40)
            print("   (Dibaca dari bawah ke atas)")
        
        # Membaca dari bawah ke atas
        hasil = ''.join(str(bit) for bit in reversed(sisa_list))
        
        if tampilkan_langkah:
            print(f"\n✅ Hasil: {hasil}")
            self.tampilkan_verifikasi_biner(hasil, n)
        
        return hasil
    
    def tampilkan_verifikasi_biner(self, biner, nilai_desimal):
        """
        Menampilkan verifikasi konversi biner ke desimal
        
        Args:
            biner (str): Bilangan biner
            nilai_desimal (int): Nilai desimal asli
        """
        print("\n🔍 Verifikasi (biner ke desimal):")
        panjang = len(biner)
        total = 0
        ekspresi = ""
        
        for i, bit in enumerate(biner):
            pangkat = panjang - i - 1
            nilai_bit = int(bit) * (2 ** pangkat)
            total += nilai_bit
            if i > 0:
                ekspresi += " + "
            ekspresi += f"{bit} × 2^{pangkat}"
        
        print(f"   {ekspresi}")
        print(f"   = {total}")
        if total == nilai_desimal:
            print("   ✓ Verifikasi berhasil")
    
    def biner_ke_desimal(self, biner, tampilkan_langkah=True):
        """
        Konversi biner ke desimal dengan menampilkan langkah
        
        Args:
            biner (str): Bilangan biner
            tampilkan_langkah (bool): Menampilkan langkah konversi
            
        Returns:
            int: Bilangan desimal
        """
        # Validasi input biner
        if not all(c in '01' for c in biner):
            raise ValueError("Input bukan bilangan biner yang valid")
        
        if tampilkan_langkah:
            print("\n📝 Langkah konversi biner ke desimal:")
            print("   " + "─"*40)
        
        panjang = len(biner)
        total = 0
        langkah = []
        
        for i, bit in enumerate(biner):
            pangkat = panjang - i - 1
            nilai_bit = int(bit) * (2 ** pangkat)
            total += nilai_bit
            langkah.append(f"   {bit} × 2^{pangkat} = {nilai_bit}")
        
        if tampilkan_langkah:
            for l in langkah:
                print(l)
            print("   " + "─"*40)
            print(f"✅ Hasil: {biner} (biner) = {total} (desimal)")
        
        return total
    
    def desimal_ke_oktal(self, n, tampilkan_langkah=True):
        """
        Konversi desimal ke oktal dengan menampilkan langkah
        
        Args:
            n (int): Bilangan desimal
            tampilkan_langkah (bool): Menampilkan langkah konversi
            
        Returns:
            str: Bilangan oktal
        """
        if n == 0:
            return "0"
        
        if tampilkan_langkah:
            print("\n📝 Langkah konversi desimal ke oktal (pembagian beruntun):")
            print("   " + "─"*40)
        
        angka = n
        sisa_list = []
        
        while angka > 0:
            sisa = angka % 8
            sisa_list.append(sisa)
            if tampilkan_langkah:
                print(f"   {angka} / 8 = {angka//8} sisa {sisa} ↑")
            angka = angka // 8
        
        hasil = ''.join(str(digit) for digit in reversed(sisa_list))
        
        if tampilkan_langkah:
            print("   " + "─"*40)
            print(f"✅ Hasil: {hasil} (oktal)")
        
        return hasil
    
    def oktal_ke_desimal(self, oktal, tampilkan_langkah=True):
        """
        Konversi oktal ke desimal dengan menampilkan langkah
        
        Args:
            oktal (str): Bilangan oktal
            tampilkan_langkah (bool): Menampilkan langkah konversi
            
        Returns:
            int: Bilangan desimal
        """
        # Validasi input oktal
        if not all('0' <= c <= '7' for c in oktal):
            raise ValueError("Input bukan bilangan oktal yang valid")
        
        if tampilkan_langkah:
            print("\n📝 Langkah konversi oktal ke desimal:")
            print("   " + "─"*40)
        
        panjang = len(oktal)
        total = 0
        langkah = []
        
        for i, digit in enumerate(oktal):
            pangkat = panjang - i - 1
            nilai_digit = int(digit) * (8 ** pangkat)
            total += nilai_digit
            langkah.append(f"   {digit} × 8^{pangkat} = {nilai_digit}")
        
        if tampilkan_langkah:
            for l in langkah:
                print(l)
            print("   " + "─"*40)
            print(f"✅ Hasil: {oktal} (oktal) = {total} (desimal)")
        
        return total
    
    def desimal_ke_heksa(self, n, tampilkan_langkah=True):
        """
        Konversi desimal ke heksadesimal dengan menampilkan langkah
        
        Args:
            n (int): Bilangan desimal
            tampilkan_langkah (bool): Menampilkan langkah konversi
            
        Returns:
            str: Bilangan heksadesimal
        """
        if n == 0:
            return "0"
        
        if tampilkan_langkah:
            print("\n📝 Langkah konversi desimal ke heksadesimal (pembagian beruntun):")
            print("   " + "─"*40)
        
        angka = n
        sisa_list = []
        
        while angka > 0:
            sisa = angka % 16
            sisa_list.append(sisa)
            if tampilkan_langkah:
                print(f"   {angka} / 16 = {angka//16} sisa {sisa} ({self.heksa_digit[sisa]}) ↑")
            angka = angka // 16
        
        hasil = ''.join(self.heksa_digit[digit] for digit in reversed(sisa_list))
        
        if tampilkan_langkah:
            print("   " + "─"*40)
            print(f"✅ Hasil: {hasil} (heksadesimal)")
        
        return hasil
    
    def heksa_ke_desimal(self, heksa, tampilkan_langkah=True):
        """
        Konversi heksadesimal ke desimal dengan menampilkan langkah
        
        Args:
            heksa (str): Bilangan heksadesimal
            tampilkan_langkah (bool): Menampilkan langkah konversi
            
        Returns:
            int: Bilangan desimal
        """
        heksa = heksa.upper()
        
        # Validasi input heksadesimal
        for c in heksa:
            if c not in self.heksa_digit:
                raise ValueError("Input bukan bilangan heksadesimal yang valid")
        
        if tampilkan_langkah:
            print("\n📝 Langkah konversi heksadesimal ke desimal:")
            print("   " + "─"*40)
        
        panjang = len(heksa)
        total = 0
        langkah = []
        
        for i, digit in enumerate(heksa):
            pangkat = panjang - i - 1
            nilai_digit = self.heksa_digit.index(digit) * (16 ** pangkat)
            total += nilai_digit
            langkah.append(f"   {digit} × 16^{pangkat} = {nilai_digit}")
        
        if tampilkan_langkah:
            for l in langkah:
                print(l)
            print("   " + "─"*40)
            print(f"✅ Hasil: {heksa} (heksadesimal) = {total} (desimal)")
        
        return total
    
    # ==================== FUNGSI UTAMA KONVERSI ====================
    
    def konversi_basis(self):
        """Fungsi utama konversi antar basis"""
        print("\n" + "─"*60)
        print("           KONVERSI BASIS BILANGAN")
        print("─"*60)
        print("Basis yang tersedia:")
        for kode, (nama, base) in self.basis.items():
            print(f"  {kode} = {nama} ({base})")
        print("─"*60)
        
        try:
            asal = input("Dari (DES/BIN/OKT/HEX): ").strip().upper()
            if asal not in self.basis:
                print("❌ Basis asal tidak valid!")
                return
            
            tujuan = input("Ke (DES/BIN/OKT/HEX): ").strip().upper()
            if tujuan not in self.basis:
                print("❌ Basis tujuan tidak valid!")
                return
            
            nilai = input(f"Nilai ({self.basis[asal][0]}): ").strip()
            
            # TEST CASE WAJIB
            self.cek_test_case(nilai, asal, tujuan)
            
            # Konversi ke desimal terlebih dahulu
            if asal == 'DES':
                try:
                    desimal = int(nilai)
                except ValueError:
                    print("❌ Input desimal tidak valid!")
                    return
            elif asal == 'BIN':
                try:
                    desimal = self.biner_ke_desimal(nilai, tampilkan_langkah=True)
                except ValueError as e:
                    print(f"❌ {e}")
                    return
            elif asal == 'OKT':
                try:
                    desimal = self.oktal_ke_desimal(nilai, tampilkan_langkah=True)
                except ValueError as e:
                    print(f"❌ {e}")
                    return
            elif asal == 'HEX':
                try:
                    desimal = self.heksa_ke_desimal(nilai, tampilkan_langkah=True)
                except ValueError as e:
                    print(f"❌ {e}")
                    return
            
            # Konversi dari desimal ke tujuan
            print(f"\n📊 Nilai desimal: {desimal}")
            
            if tujuan == 'DES':
                hasil = str(desimal)
            elif tujuan == 'BIN':
                hasil = self.desimal_ke_biner(desimal, tampilkan_langkah=True)
            elif tujuan == 'OKT':
                hasil = self.desimal_ke_oktal(desimal, tampilkan_langkah=True)
            elif tujuan == 'HEX':
                hasil = self.desimal_ke_heksa(desimal, tampilkan_langkah=True)
            
            print(f"\n✅ Hasil akhir: {hasil} ({self.basis[tujuan][0]})")
            
            # Verifikasi dengan fungsi built-in
            print("\n🔍 Verifikasi dengan fungsi built-in:")
            if tujuan == 'BIN':
                print(f"   bin({desimal}) = {bin(desimal)[2:]}")
            elif tujuan == 'OKT':
                print(f"   oct({desimal}) = {oct(desimal)[2:]}")
            elif tujuan == 'HEX':
                print(f"   hex({desimal}) = {hex(desimal)[2:].upper()}")
            
            self.history.add("Bilangan - Konversi", 
                           f"{nilai} ({asal}) → {tujuan}", 
                           f"{hasil} ({tujuan})")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def cek_test_case(self, nilai, asal, tujuan):
        """Memeriksa test case wajib"""
        test_cases = [
            ('255', 'DES', 'BIN', '11111111'),
            ('101010', 'BIN', 'DES', '42'),
            ('FF', 'HEX', 'DES', '255'),
            ('377', 'OKT', 'DES', '255'),
            ('100', 'DES', 'HEX', '64')
        ]
        
        for tc_nilai, tc_asal, tc_tujuan, tc_hasil in test_cases:
            if nilai == tc_nilai and asal == tc_asal and tujuan == tc_tujuan:
                print(f"\n⚡ TEST CASE WAJIB TERDETEKSI!")
                print(f"   Input: {nilai} ({asal}) → {tujuan}")
                print(f"   Output yang diharapkan: {tc_hasil}")
    
    # ==================== FUNGSI OPERASI ARITMATIKA ====================
    
    def tambah_biner(self, a, b):
        """Penjumlahan dua bilangan biner"""
        des_a = self.biner_ke_desimal(a, tampilkan_langkah=False)
        des_b = self.biner_ke_desimal(b, tampilkan_langkah=False)
        hasil_des = des_a + des_b
        hasil_bin = self.desimal_ke_biner(hasil_des, tampilkan_langkah=False)
        
        return hasil_bin, des_a, des_b, hasil_des
    
    def kurang_biner(self, a, b):
        """Pengurangan dua bilangan biner"""
        des_a = self.biner_ke_desimal(a, tampilkan_langkah=False)
        des_b = self.biner_ke_desimal(b, tampilkan_langkah=False)
        
        if des_a < des_b:
            raise ValueError("Hasil pengurangan negatif (tidak didukung dalam mode ini)")
        
        hasil_des = des_a - des_b
        hasil_bin = self.desimal_ke_biner(hasil_des, tampilkan_langkah=False)
        
        return hasil_bin, des_a, des_b, hasil_des
    
    def tambah_oktal(self, a, b):
        """Penjumlahan dua bilangan oktal"""
        des_a = self.oktal_ke_desimal(a, tampilkan_langkah=False)
        des_b = self.oktal_ke_desimal(b, tampilkan_langkah=False)
        hasil_des = des_a + des_b
        hasil_okt = self.desimal_ke_oktal(hasil_des, tampilkan_langkah=False)
        
        return hasil_okt, des_a, des_b, hasil_des
    
    def kurang_oktal(self, a, b):
        """Pengurangan dua bilangan oktal"""
        des_a = self.oktal_ke_desimal(a, tampilkan_langkah=False)
        des_b = self.oktal_ke_desimal(b, tampilkan_langkah=False)
        
        if des_a < des_b:
            raise ValueError("Hasil pengurangan negatif (tidak didukung dalam mode ini)")
        
        hasil_des = des_a - des_b
        hasil_okt = self.desimal_ke_oktal(hasil_des, tampilkan_langkah=False)
        
        return hasil_okt, des_a, des_b, hasil_des
    
    def tambah_heksa(self, a, b):
        """Penjumlahan dua bilangan heksadesimal"""
        des_a = self.heksa_ke_desimal(a, tampilkan_langkah=False)
        des_b = self.heksa_ke_desimal(b, tampilkan_langkah=False)
        hasil_des = des_a + des_b
        hasil_heks = self.desimal_ke_heksa(hasil_des, tampilkan_langkah=False)
        
        return hasil_heks, des_a, des_b, hasil_des
    
    def kurang_heksa(self, a, b):
        """Pengurangan dua bilangan heksadesimal"""
        des_a = self.heksa_ke_desimal(a, tampilkan_langkah=False)
        des_b = self.heksa_ke_desimal(b, tampilkan_langkah=False)
        
        if des_a < des_b:
            raise ValueError("Hasil pengurangan negatif (tidak didukung dalam mode ini)")
        
        hasil_des = des_a - des_b
        hasil_heks = self.desimal_ke_heksa(hasil_des, tampilkan_langkah=False)
        
        return hasil_heks, des_a, des_b, hasil_des
    
    def tampilkan_perhitungan_column_wise(self, a, b, hasil, basis):
        """Menampilkan perhitungan secara column-wise"""
        print("\n📊 Perhitungan column-wise:")
        print("   " + "─"*30)
        
        # Menentukan panjang maksimal untuk alignment
        max_len = max(len(a), len(b), len(hasil))
        
        # Menampilkan angka
        print(f"   {a:>{max_len}}")
        print(f"   {b:>{max_len}}")
        print("   " + "─"*max_len)
        print(f"   {hasil:>{max_len}}")
        
        # Menampilkan carry jika ada (untuk biner)
        if basis == 'BIN':
            print("\n   Proses penjumlahan bit per bit:")
            panjang = max(len(a), len(b))
            a_padded = a.zfill(panjang)
            b_padded = b.zfill(panjang)
            
            carry = 0
            hasil_bit = []
            for i in range(panjang-1, -1, -1):
                bit_a = int(a_padded[i])
                bit_b = int(b_padded[i])
                total = bit_a + bit_b + carry
                hasil_bit.append(str(total % 2))
                carry = total // 2
                print(f"   Bit-{panjang-i-1}: {bit_a} + {bit_b} + carry {carry if i>0 else 0} = {total} → hasil {total%2}, carry {carry}")
            
            if carry:
                print(f"   Carry akhir: {carry}")
    
    def operasi_non_desimal(self):
        """Fungsi untuk operasi aritmatika non-desimal"""
        print("\n" + "─"*60)
        print("           OPERASI ARITMATIKA NON-DESIMAL")
        print("─"*60)
        print("Pilih jenis bilangan:")
        print("  1. Biner")
        print("  2. Oktal")
        print("  3. Heksadesimal")
        print("─"*30)
        
        try:
            pilihan = int(input("Pilih jenis bilangan (1-3): "))
            
            if pilihan not in [1, 2, 3]:
                print("❌ Pilihan tidak valid!")
                return
            
            print("\nPilih operasi:")
            print("  1. Penjumlahan (+)")
            print("  2. Pengurangan (-)")
            
            operasi = int(input("Pilih operasi (1-2): "))
            
            if operasi not in [1, 2]:
                print("❌ Pilihan operasi tidak valid!")
                return
            
            if pilihan == 1:  # Biner
                print("\nMasukkan dua bilangan biner:")
                a = input("Bilangan pertama: ").strip()
                b = input("Bilangan kedua: ").strip()
                
                # Validasi
                if not all(c in '01' for c in a) or not all(c in '01' for c in b):
                    print("❌ Input harus berupa bilangan biner (0 dan 1)!")
                    return
                
                if operasi == 1:
                    hasil, des_a, des_b, des_hasil = self.tambah_biner(a, b)
                    print(f"\n✅ {a} (biner) + {b} (biner) = {hasil} (biner)")
                else:
                    hasil, des_a, des_b, des_hasil = self.kurang_biner(a, b)
                    print(f"\n✅ {a} (biner) - {b} (biner) = {hasil} (biner)")
                
                print(f"\n📊 Dalam desimal: {des_a} - {des_b} = {des_hasil}")
                self.tampilkan_perhitungan_column_wise(a, b, hasil, 'BIN')
                
                self.history.add("Bilangan - Operasi Biner", 
                               f"{a} {'+' if operasi==1 else '-'} {b}", 
                               hasil)
                
            elif pilihan == 2:  # Oktal
                print("\nMasukkan dua bilangan oktal:")
                a = input("Bilangan pertama: ").strip()
                b = input("Bilangan kedua: ").strip()
                
                # Validasi
                if not all('0' <= c <= '7' for c in a) or not all('0' <= c <= '7' for c in b):
                    print("❌ Input harus berupa bilangan oktal (0-7)!")
                    return
                
                if operasi == 1:
                    hasil, des_a, des_b, des_hasil = self.tambah_oktal(a, b)
                    print(f"\n✅ {a} (oktal) + {b} (oktal) = {hasil} (oktal)")
                else:
                    hasil, des_a, des_b, des_hasil = self.kurang_oktal(a, b)
                    print(f"\n✅ {a} (oktal) - {b} (oktal) = {hasil} (oktal)")
                
                print(f"\n📊 Dalam desimal: {des_a} - {des_b} = {des_hasil}")
                
                self.history.add("Bilangan - Operasi Oktal", 
                               f"{a} {'+' if operasi==1 else '-'} {b}", 
                               hasil)
                
            else:  # Heksadesimal
                print("\nMasukkan dua bilangan heksadesimal:")
                a = input("Bilangan pertama: ").strip().upper()
                b = input("Bilangan kedua: ").strip().upper()
                
                # Validasi
                heksa_digit = "0123456789ABCDEF"
                if not all(c in heksa_digit for c in a) or not all(c in heksa_digit for c in b):
                    print("❌ Input harus berupa bilangan heksadesimal valid (0-9, A-F)!")
                    return
                
                if operasi == 1:
                    hasil, des_a, des_b, des_hasil = self.tambah_heksa(a, b)
                    print(f"\n✅ {a} (heksa) + {b} (heksa) = {hasil} (heksa)")
                else:
                    hasil, des_a, des_b, des_hasil = self.kurang_heksa(a, b)
                    print(f"\n✅ {a} (heksa) - {b} (heksa) = {hasil} (heksa)")
                
                print(f"\n📊 Dalam desimal: {des_a} - {des_b} = {des_hasil}")
                
                self.history.add("Bilangan - Operasi Heksa", 
                               f"{a} {'+' if operasi==1 else '-'} {b}", 
                               hasil)
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Terjadi kesalahan: {e}")