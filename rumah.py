from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, listrik, luas_tanah):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.listrik = listrik
        self.luas_tanah = luas_tanah

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
   
    def get_listrik(self):
        return str(self.listrik) + " VA"
    
    def get_luas_tanah(self):
        return str(self.luas_tanah) + " m^2"