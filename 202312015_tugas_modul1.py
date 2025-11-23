class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"
    
    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    
    def perkenalan_diri(self):
        return f"Halo, saya {self.nama} (NIM: {self.nim}) dari {self.jurusan}"
    
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK berhasil diupdate menjadi {self.ipk}"
        else:
            return "IPK harus antara 0.0 - 4.0"
    
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"

# Instansiasi 3 object mahasiswa
mhs1 = Mahasiswa("Nur Halimatul Sa'diah", "202312015", "Teknik Informatika", 3.8)
mhs2 = Mahasiswa("Erlina Rosa Paraditha", "202312049", "Sistem Informasi", 3.2)
mhs3 = Mahasiswa("Aqhlia Nurfahma", "202312026", "Teknik Informatika", 2.4)

# Demonstrasi semua method
print("=== DEMONSTRASI CLASS MAHASISWA ===\n")

print("1. PERKENALAN DIRI:")
print(mhs1.perkenalan_diri())
print(mhs2.perkenalan_diri())
print(mhs3.perkenalan_diri())

print("\n2. PREDIKAT KELULUSAN AWAL:")
print(f"{mhs1.nama}: {mhs1.predikat_kelulusan()}")
print(f"{mhs2.nama}: {mhs2.predikat_kelulusan()}")
print(f"{mhs3.nama}: {mhs3.predikat_kelulusan()}")

print("\n3. UPDATE IPK:")
print(mhs3.update_ipk(2.8))  # Update IPK Budi
print(f"Predikat baru {mhs3.nama}: {mhs3.predikat_kelulusan()}")

print(mhs2.update_ipk(3.6))  # Update IPK Siti
print(f"Predikat baru {mhs2.nama}: {mhs2.predikat_kelulusan()}")

print("\n4. CLASS ATTRIBUTE:")
print(f"Universitas: {Mahasiswa.universitas}")

print("\n5. INFORMASI FINAL:")
mahasiswa_list = [mhs1, mhs2, mhs3]
for mhs in mahasiswa_list:
    print(f"{mhs.nama} - IPK: {mhs.ipk} - Predikat: {mhs.predikat_kelulusan()}")