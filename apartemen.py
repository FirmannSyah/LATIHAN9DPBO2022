from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, listrik, luas_tanah):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.listrik = listrik
        self.luas_tanah = luas_tanah
    
    def get_listrik(self):
        return str(self.listrik) + " VA"
    
    def get_luas_tanah(self):
        return str(self.luas_tanah) + " m^2"

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik