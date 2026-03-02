"""
MODUL VALIDATOR
Fungsi-fungsi untuk validasi input pengguna
"""


def input_angka(prompt, min_val=None, max_val=None):
    """
    Meminta input angka dengan validasi
    
    Args:
        prompt (str): Teks prompt
        min_val (int, optional): Nilai minimum
        max_val (int, optional): Nilai maksimum
        
    Returns:
        int: Angka yang valid
    """
    while True:
        try:
            nilai = int(input(prompt))
            
            if min_val is not None and nilai < min_val:
                print(f"❌ Nilai harus >= {min_val}")
                continue
                
            if max_val is not None and nilai > max_val:
                print(f"❌ Nilai harus <= {max_val}")
                continue
                
            return nilai
            
        except ValueError:
            print("❌ Input harus berupa angka!")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan.")
            exit()


def input_ya_tidak(prompt):
    """
    Meminta input ya/tidak
    
    Args:
        prompt (str): Teks prompt
        
    Returns:
        bool: True jika ya, False jika tidak
    """
    while True:
        jawaban = input(prompt).strip().lower()
        if jawaban in ['y', 'ya', 'yes', '']:
            return True
        elif jawaban in ['n', 'tidak', 'no']:
            return False
        else:
            print("❌ Masukkan 'y' atau 'n'")


def validasi_ip(ip):
    """
    Validasi format IP address
    
    Args:
        ip (str): IP address
        
    Returns:
        bool: True jika valid, False jika tidak
    """
    try:
        octet = ip.split('.')
        if len(octet) != 4:
            return False
        
        for o in octet:
            if not o.isdigit():
                return False
            nilai = int(o)
            if nilai < 0 or nilai > 255:
                return False
        
        return True
        
    except:
        return False