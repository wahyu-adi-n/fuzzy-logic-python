class Produksi:
    def agregasi_berkurang(self, mins, maks, nilai_minimal):
        return maks - ((maks - mins) * nilai_minimal)

    def agregasi_bertambah(self, mins, maks, nilai_minimal):
        return mins + ((maks - mins) * nilai_minimal)
