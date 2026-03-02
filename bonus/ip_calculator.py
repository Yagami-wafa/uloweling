"""
MODUL KALKULATOR IP ADDRESS (BONUS SOAL)
Menghitung subnet mask, network address, broadcast address, dan konversi IP
"""


class KalkulatorIP:
    """Kelas untuk kalkulator IP Address"""
    
    def __init__(self, history_manager):
        """
        Inisialisasi kalkulator IP
        
        Args:
            history_manager: Object untuk mengelola history
        """
        self.history = history_manager
    
    def menu(self):
        """Menu utama kalkulator IP"""
        while True:
            print("\n" + "="*60)
            print("          KALKULATOR IP ADDRESS (BONUS)")
            print("="*60)
            print("╔════════════════════════════════════════════════╗")
            print("║  1. Hitung Subnet Mask dari Prefix Length      ║")
            print("║  2. Hitung Network & Broadcast Address          ║")
            print("║  3. Hitung Jumlah Host Tersedia                 ║")
            print("║  4. Konversi IP Desimal ke Biner                ║")
            print("║  0. Kembali ke Menu Utama                       ║")
            print("╚════════════════════════════════════════════════╝")
            
            try:
                pilihan = int(input("\nPilih menu: "))
                
                if pilihan == 0:
                    break
                elif pilihan == 1:
                    self.hitung_subnet_mask()
                elif pilihan == 2:
                    self.hitung_network_broadcast()
                elif pilihan == 3:
                    self.hitung_jumlah_host()
                elif pilihan == 4:
                    self.konversi_ip_ke_biner()
                else:
                    print("❌ Pilihan tidak valid!")
                    
            except ValueError:
                print("❌ Input harus berupa angka!")
    
    def hitung_subnet_mask(self):
        """Menghitung subnet mask dari prefix length"""
        print("\n" + "─"*50)
        print("           HITUNG SUBNET MASK")
        print("─"*50)
        
        try:
            prefix = int(input("Masukkan prefix length (contoh: 24 untuk /24): "))
            
            if prefix < 0 or prefix > 32:
                print("❌ Prefix length harus antara 0 dan 32!")
                return
            
            # Hitung subnet mask
            mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
            octet1 = (mask >> 24) & 0xFF
            octet2 = (mask >> 16) & 0xFF
            octet3 = (mask >> 8) & 0xFF
            octet4 = mask & 0xFF
            
            subnet_mask = f"{octet1}.{octet2}.{octet3}.{octet4}"
            
            # Tampilkan dalam bentuk biner juga
            biner = f"{octet1:08b}.{octet2:08b}.{octet3:08b}.{octet4:08b}"
            
            print(f"\n✅ Prefix /{prefix} = Subnet Mask: {subnet_mask}")
            print(f"   Dalam biner: {biner}")
            
            # Tampilkan kelas IP berdasarkan prefix
            if prefix <= 8:
                kelas = "A"
            elif prefix <= 16:
                kelas = "B"
            elif prefix <= 24:
                kelas = "C"
            else:
                kelas = "CIDR (Classless)"
            
            print(f"   Kelas IP: {kelas}")
            
            self.history.add("IP - Subnet Mask", f"/{prefix}", subnet_mask)
            
        except ValueError:
            print("❌ Input harus berupa angka!")
    
    def hitung_network_broadcast(self):
        """Menghitung network address dan broadcast address"""
        print("\n" + "─"*50)
        print("           HITUNG NETWORK & BROADCAST")
        print("─"*50)
        
        try:
            ip = input("Masukkan IP address (format: x.x.x.x): ").strip()
            prefix = int(input("Masukkan prefix length (contoh: 24): "))
            
            # Validasi IP
            octet = ip.split('.')
            if len(octet) != 4:
                print("❌ Format IP tidak valid!")
                return
            
            ip_int = 0
            for i, o in enumerate(octet):
                if not o.isdigit() or int(o) < 0 or int(o) > 255:
                    print(f"❌ Oktet {i+1} tidak valid!")
                    return
                ip_int |= int(o) << (24 - i*8)
            
            # Hitung mask
            mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
            
            # Hitung network address
            network_int = ip_int & mask
            
            # Hitung broadcast address
            broadcast_int = network_int | (~mask & 0xFFFFFFFF)
            
            # Konversi ke format dotted decimal
            network = f"{(network_int >> 24) & 0xFF}.{(network_int >> 16) & 0xFF}.{(network_int >> 8) & 0xFF}.{network_int & 0xFF}"
            broadcast = f"{(broadcast_int >> 24) & 0xFF}.{(broadcast_int >> 16) & 0xFF}.{(broadcast_int >> 8) & 0xFF}.{broadcast_int & 0xFF}"
            
            print(f"\n✅ Network Address: {network}")
            print(f"✅ Broadcast Address: {broadcast}")
            
            self.history.add("IP - Network/Broadcast", f"{ip}/{prefix}", f"Network: {network}, Broadcast: {broadcast}")
            
        except ValueError:
            print("❌ Input tidak valid!")
    
    def hitung_jumlah_host(self):
        """Menghitung jumlah host tersedia"""
        print("\n" + "─"*50)
        print("           HITUNG JUMLAH HOST")
        print("─"*50)
        
        try:
            prefix = int(input("Masukkan prefix length (contoh: 24): "))
            
            if prefix < 0 or prefix > 32:
                print("❌ Prefix length harus antara 0 dan 32!")
                return
            
            # Jumlah host = 2^(32-prefix) - 2
            jumlah_host = (1 << (32 - prefix)) - 2
            
            if jumlah_host < 0:
                jumlah_host = 0
            
            print(f"\n✅ Jumlah host tersedia untuk /{prefix}: {jumlah_host:,} host")
            
            if jumlah_host == 0:
                print("   (Hanya untuk point-to-point link)")
            elif jumlah_host == 1:
                print("   (Tidak praktis untuk penggunaan umum)")
            
            self.history.add("IP - Jumlah Host", f"/{prefix}", f"{jumlah_host} host")
            
        except ValueError:
            print("❌ Input harus berupa angka!")
    
    def konversi_ip_ke_biner(self):
        """Konversi IP desimal ke biner"""
        print("\n" + "─"*50)
        print("           KONVERSI IP KE BINER")
        print("─"*50)
        
        try:
            ip = input("Masukkan IP address (format: x.x.x.x): ").strip()
            
            octet = ip.split('.')
            if len(octet) != 4:
                print("❌ Format IP tidak valid!")
                return
            
            biner = []
            for i, o in enumerate(octet):
                if not o.isdigit() or int(o) < 0 or int(o) > 255:
                    print(f"❌ Oktet {i+1} tidak valid!")
                    return
                biner.append(f"{int(o):08b}")
            
            ip_biner = '.'.join(biner)
            
            print(f"\n✅ IP Address: {ip}")
            print(f"✅ Dalam biner: {ip_biner}")
            
            # Tampilkan perhitungan
            print("\n📊 Perhitungan:")
            for i, o in enumerate(octet):
                print(f"   Oktet {i+1}: {o} desimal = {biner[i]} biner")
            
            self.history.add("IP - Konversi Biner", ip, ip_biner)
            
        except ValueError:
            print("❌ Input tidak valid!")