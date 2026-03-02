"""
MODUL KALKULATOR ARITMATIKA (SOAL 1)
Mendukung operasi dasar, ilmiah, dan ekspresi berantai
"""

import math


class KalkulatorAritmatika:
    """Kelas untuk kalkulator aritmatika dengan berbagai fitur"""
    
    def __init__(self, history_manager):
        """
        Inisialisasi kalkulator aritmatika
        
        Args:
            history_manager: Object untuk mengelola history
        """
        self.history = history_manager
    
    def menu(self):
        """Menu utama kalkulator aritmatika"""
        while True:
            print("\n" + "="*60)
            print("          KALKULATOR ARITMATIKA")
            print("="*60)
            print("╔════════════════════════════════════════════════╗")
            print("║  1. Operasi Dasar (+, -, *, /, %, ^, √)       ║")
            print("║  2. Operasi Ilmiah (sin, cos, tan, log, ln)   ║")
            print("║  3. Ekspresi Berantai                          ║")
            print("║  0. Kembali ke Menu Utama                      ║")
            print("╚════════════════════════════════════════════════╝")
            
            try:
                pilihan = int(input("\nPilih menu: "))
                
                if pilihan == 0:
                    break
                elif pilihan == 1:
                    self.operasi_dasar()
                elif pilihan == 2:
                    self.operasi_ilmiah()
                elif pilihan == 3:
                    self.ekspresi_berantai()
                else:
                    print("❌ Pilihan tidak valid!")
                    
            except ValueError:
                print("❌ Input harus berupa angka!")
    
    def operasi_dasar(self):
        """Fungsi untuk operasi dasar aritmatika"""
        print("\n" + "─"*50)
        print("           OPERASI DASAR")
        print("─"*50)
        print("Operasi yang tersedia:")
        print("  + : Penjumlahan")
        print("  - : Pengurangan")
        print("  * : Perkalian")
        print("  / : Pembagian")
        print("  % : Modulo (sisa bagi)")
        print("  ^ : Pangkat")
        print("  √ : Akar kuadrat")
        print("─"*50)
        
        try:
            operator = input("Masukkan operator: ").strip()
            
            if operator == '√':
                angka = float(input("Masukkan angka: "))
                if angka < 0:
                    print("❌ Akar kuadrat dari bilangan negatif tidak terdefinisi!")
                    return
                
                hasil = math.sqrt(angka)
                print(f"\n✅ Hasil: √{angka} = {hasil:.4f}")
                
                # Tampilkan langkah
                print(f"\nLangkah: √{angka} = {hasil:.4f}")
                
                self.history.add("Aritmatika - Akar", f"√{angka}", f"{hasil:.4f}")
                
            else:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
                
                if operator == '+':
                    hasil = a + b
                    print(f"\n✅ Hasil: {a} + {b} = {hasil:.4f}")
                    print(f"Langkah: {a} + {b} = {hasil:.4f}")
                    
                elif operator == '-':
                    hasil = a - b
                    print(f"\n✅ Hasil: {a} - {b} = {hasil:.4f}")
                    print(f"Langkah: {a} - {b} = {hasil:.4f}")
                    
                elif operator == '*':
                    hasil = a * b
                    print(f"\n✅ Hasil: {a} * {b} = {hasil:.4f}")
                    print(f"Langkah: {a} × {b} = {hasil:.4f}")
                    
                elif operator == '/':
                    if b == 0:
                        print("❌ Error: Pembagian dengan nol tidak diperbolehkan!")
                        return
                    hasil = a / b
                    print(f"\n✅ Hasil: {a} / {b} = {hasil:.4f}")
                    print(f"Langkah: {a} ÷ {b} = {hasil:.4f}")
                    
                elif operator == '%':
                    if b == 0:
                        print("❌ Error: Modulo dengan nol tidak diperbolehkan!")
                        return
                    hasil = a % b
                    print(f"\n✅ Hasil: {a} % {b} = {hasil:.4f}")
                    print(f"Langkah: {a} mod {b} = {hasil:.4f}")
                    
                elif operator == '^':
                    hasil = a ** b
                    print(f"\n✅ Hasil: {a} ^ {b} = {hasil:.4f}")
                    print(f"Langkah: {a}^{b} = {hasil:.4f}")
                    
                else:
                    print("❌ Operator tidak valid!")
                    return
                
                self.history.add("Aritmatika - Dasar", f"{a} {operator} {b}", f"{hasil:.4f}")
                
        except ValueError:
            print("❌ Input harus berupa angka yang valid!")
    
    def operasi_ilmiah(self):
        """Fungsi untuk operasi ilmiah (trigonometri dan logaritma)"""
        print("\n" + "─"*50)
        print("           OPERASI ILMIAH")
        print("─"*50)
        print("Fungsi yang tersedia:")
        print("  1. sin  (sinus)")
        print("  2. cos  (cosinus)")
        print("  3. tan  (tangen)")
        print("  4. log  (logaritma basis 10)")
        print("  5. ln   (logaritma natural)")
        print("─"*50)
        
        try:
            pilihan = int(input("Pilih fungsi (1-5): "))
            
            if pilihan == 1:
                sudut = float(input("Masukkan sudut dalam derajat: "))
                rad = math.radians(sudut)
                hasil = math.sin(rad)
                print(f"\n✅ Hasil: sin({sudut}°) = {hasil:.6f}")
                print(f"Langkah: sin({sudut}°) = sin({rad:.4f} rad) = {hasil:.6f}")
                self.history.add("Aritmatika - sin", f"sin({sudut}°)", f"{hasil:.6f}")
                
            elif pilihan == 2:
                sudut = float(input("Masukkan sudut dalam derajat: "))
                rad = math.radians(sudut)
                hasil = math.cos(rad)
                print(f"\n✅ Hasil: cos({sudut}°) = {hasil:.6f}")
                print(f"Langkah: cos({sudut}°) = cos({rad:.4f} rad) = {hasil:.6f}")
                self.history.add("Aritmatika - cos", f"cos({sudut}°)", f"{hasil:.6f}")
                
            elif pilihan == 3:
                sudut = float(input("Masukkan sudut dalam derajat: "))
                rad = math.radians(sudut)
                if abs(math.cos(rad)) < 1e-10:
                    print("❌ Error: Tangen tidak terdefinisi untuk sudut ini!")
                    return
                hasil = math.tan(rad)
                print(f"\n✅ Hasil: tan({sudut}°) = {hasil:.6f}")
                print(f"Langkah: tan({sudut}°) = tan({rad:.4f} rad) = {hasil:.6f}")
                self.history.add("Aritmatika - tan", f"tan({sudut}°)", f"{hasil:.6f}")
                
            elif pilihan == 4:
                angka = float(input("Masukkan angka (positif): "))
                if angka <= 0:
                    print("❌ Logaritma hanya terdefinisi untuk angka positif!")
                    return
                hasil = math.log10(angka)
                print(f"\n✅ Hasil: log({angka}) = {hasil:.6f}")
                print(f"Langkah: log₁₀({angka}) = {hasil:.6f}")
                self.history.add("Aritmatika - log", f"log({angka})", f"{hasil:.6f}")
                
            elif pilihan == 5:
                angka = float(input("Masukkan angka (positif): "))
                if angka <= 0:
                    print("❌ Logaritma natural hanya terdefinisi untuk angka positif!")
                    return
                hasil = math.log(angka)
                print(f"\n✅ Hasil: ln({angka}) = {hasil:.6f}")
                print(f"Langkah: ln({angka}) = {hasil:.6f}")
                self.history.add("Aritmatika - ln", f"ln({angka})", f"{hasil:.6f}")
                
            else:
                print("❌ Pilihan tidak valid!")
                
        except ValueError:
            print("❌ Input harus berupa angka yang valid!")
    
    def evaluate_expression(self, expression):
        """
        Fungsi internal untuk mengevaluasi ekspresi dengan precedence operator
        
        Args:
            expression (str): Ekspresi matematika
            
        Returns:
            float: Hasil evaluasi
        """
        # Membersihkan ekspresi dari spasi
        expression = expression.replace(' ', '')
        
        def apply_operator(operators, values):
            """Menerapkan operator pada dua nilai teratas"""
            operator = operators.pop()
            right = values.pop()
            left = values.pop()
            
            if operator == '+':
                values.append(left + right)
            elif operator == '-':
                values.append(left - right)
            elif operator == '*':
                values.append(left * right)
            elif operator == '/':
                if right == 0:
                    raise ValueError("Pembagian dengan nol!")
                values.append(left / right)
            elif operator == '^':
                values.append(left ** right)
        
        # Precedence operator
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
        values = []
        operators = []
        i = 0
        langkah = []
        
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                # Membaca angka (termasuk desimal)
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                values.append(float(expression[i:j]))
                i = j
            elif expression[i] in precedence:
                # Operator
                while (operators and operators[-1] != '(' and 
                       precedence.get(operators[-1], 0) >= precedence.get(expression[i], 0)):
                    apply_operator(operators, values)
                operators.append(expression[i])
                i += 1
            elif expression[i] == '(':
                operators.append(expression[i])
                i += 1
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()  # Menghapus '('
                i += 1
            else:
                i += 1
        
        while operators:
            apply_operator(operators, values)
        
        return values[0]
    
    def ekspresi_berantai(self):
        """Fungsi untuk mengevaluasi ekspresi berantai"""
        print("\n" + "─"*50)
        print("           EKSPRESI BERANTAI")
        print("─"*50)
        print("Contoh: 5 + 3 * 2 - 4 / 2")
        print("Operator yang didukung: +, -, *, /, ^, (, )")
        print("Precedence operator: ^ > * = / > + = -")
        print("─"*50)
        
        try:
            ekspresi = input("Masukkan ekspresi: ").strip()
            
            # Validasi sederhana
            if not ekspresi:
                print("❌ Ekspresi tidak boleh kosong!")
                return
            
            # Hitung hasil
            hasil = self.evaluate_expression(ekspresi)
            
            print(f"\n✅ Hasil: {ekspresi} = {hasil:.4f}")
            
            # Tampilkan langkah perhitungan
            print("\nLangkah perhitungan dengan precedence operator:")
            print("  • * dan / dievaluasi sebelum + dan -")
            print("  • ^ dievaluasi sebelum * dan /")
            print("  • Operasi dalam tanda kurung dievaluasi terlebih dahulu")
            
            self.history.add("Aritmatika - Ekspresi", ekspresi, f"{hasil:.4f}")
            
        except Exception as e:
            print(f"❌ Error dalam evaluasi ekspresi: {e}")