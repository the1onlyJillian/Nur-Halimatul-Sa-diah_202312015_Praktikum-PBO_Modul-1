class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"
    
    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
    
    def info_kendaraan(self):
        return f"{self.merk} {self.warna} ({self.tahun})"

# Inisialiasasi object
kendaraan1 = Kendaraan("Toyota", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda", "Merah", 2023)

# Demonstrasi akses instance attribute
print("=== INSTANCE ATTRIBUTE ===")
print(f"Kendaraan 1: {kendaraan1.info_kendaraan()}")
print(f"Kendaraan 2: {kendaraan2.info_kendaraan()}")

# Demonstrasi akses class attribute
print("\n=== CLASS ATTRIBUTE ===")
print(f"Bahan bakar kendaraan1: {kendaraan1.bahan_bakar}")
print(f"Bahan bakar kendaraan2: {kendaraan2.bahan_bakar}")
print(f"Bahan bakar class: {Kendaraan.bahan_bakar}")

# Demonstrasi perbedaan
print("\n=== PERBEDAAN ===")
print("Instance attribute berbeda untuk setiap objek:")
print(f"kendaraan1.merk = {kendaraan1.merk}")
print(f"kendaraan2.merk = {kendaraan2.merk}")

print("\nClass attribute sama untuk semua objek:")
print(f"kendaraan1.bahan_bakar = {kendaraan1.bahan_bakar}")
print(f"kendaraan2.bahan_bakar = {kendaraan2.bahan_bakar}")
print(f"Kendaraan.bahan_bakar = {Kendaraan.bahan_bakar}")

# Mengubah class attribute
print("\n=== MENGUBAH CLASS ATTRIBUTE ===")
Kendaraan.bahan_bakar = "Solar"
print("Setelah mengubah class attribute:")
print(f"kendaraan1.bahan_bakar = {kendaraan1.bahan_bakar}")
print(f"kendaraan2.bahan_bakar = {kendaraan2.bahan_bakar}")