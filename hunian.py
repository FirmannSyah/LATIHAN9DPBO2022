class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, listrik = 1, luas_tanah = 1):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.listrik = listrik
        self.luas_tanah = luas_tanah

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_listrik(self):
        pass
        
    def get_jml_kamar(self):
        pass

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis + " memiliki " + str(self.jml_kamar) + " kamar ditempati oleh " + str(self.jml_penghuni) + " orang."

    def get_nama_pemilik(self):
        pass