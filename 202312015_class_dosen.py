class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn
    
    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"

# Instansiasi 2 object dosen
dosen1 = Dosen("Dr. Ahmad Wijaya", "123456")
dosen2 = Dosen("Prof. Sari Dewi", "789012")

# Memanggil method ajar_mata_kuliah()
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Basis Data"))