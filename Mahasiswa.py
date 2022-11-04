class Mahasiswa:

  def __init__(self, nama, umur, jk, alamat, kota):
    self.nama = nama
    self.umur = str(umur)
    self.jk = jk
    self.alamat = alamat
    self.kota = kota

  def bioData(self):
    print("-- Bio Data Mahasiswa --")
    print("Nama Lengkap    : " + self.nama)
    print("Umur Saat Ini   : " + self.umur)
    print("Jenis Kelamin   : " + self.jk)
    print("Alamat Sekarang : " + self.alamat)
    print("Kota            : " + self.kota)
data = Mahasiswa("HAKIM",19,'Pria','Tangerang','Banten')
data.bioData()
