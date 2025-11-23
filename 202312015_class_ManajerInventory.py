class ManajerInventori:
    def __init__(self):
        self.inventori = {}
    
    def tambah_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            self.inventori[nama_barang] += jumlah
        else:
            self.inventori[nama_barang] = jumlah
        return f"Berhasil tambah {jumlah} {nama_barang}"
    
    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang not in self.inventori:
            return f"Barang {nama_barang} tidak ditemukan"
        if self.inventori[nama_barang] < jumlah:
            return f"Stok {nama_barang} tidak mencukupi"
        
        self.inventori[nama_barang] -= jumlah
        return f"Berhasil hapus {jumlah} {nama_barang}"
    
    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        return self.inventori

# Demonstrasi semua method
manajer = ManajerInventori()

# Test tambah_barang
print(manajer.tambah_barang("Laptop", 5))
print(manajer.tambah_barang("Mouse", 10))
print(manajer.tambah_barang("Laptop", 3))

# Test lihat_inventori
print("\nInventori saat ini:")
print(manajer.lihat_inventori())

# Test hapus_barang
print(manajer.hapus_barang("Laptop", 2))
print(manajer.hapus_barang("Keyboard", 1))  # Barang tidak ada

# Test lihat_inventori akhir
print("\nInventori akhir:")
print(manajer.lihat_inventori())