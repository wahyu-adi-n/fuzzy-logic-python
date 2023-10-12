class Permintaan:
    def __init__(self):
        self.u_turun = 0
        self.u_naik = 0
        self.min_permintaan = 1000
        self.maks_permintaan = 5000

    def _turun(self, x):
        if (x >= self.min_permintaan) and (x <= self.maks_permintaan):
            self.u_turun = (self.maks_permintaan - x) / (
                self.maks_permintaan - self.min_permintaan
            )
        elif x < self.min_permintaan:
            self.u_turun = 1
        return self.u_turun

    def _naik(self, x):
        if (x >= self.min_permintaan) and (x <= self.maks_permintaan):
            self.u_naik = (x - self.min_permintaan) / (
                self.maks_permintaan - self.min_permintaan
            )
        elif x > self.maks_permintaan:
            self.u_naik = 1
        return self.u_naik


class Persediaan:
    def __init__(self):
        self.u_sedikit = 0
        self.u_banyak = 0
        self.min_persediaan = 100
        self.maks_persediaan = 600

    def _sedikit(self, x):
        if (x >= self.min_persediaan) and (x <= self.maks_persediaan):
            self.u_sedikit = (self.maks_persediaan - x) / (
                self.maks_persediaan - self.min_persediaan
            )
        elif x < self.min_persediaan:
            self.u_sedikit = 1
        return self.u_sedikit

    def _banyak(self, x):
        if (x >= self.min_persediaan) and (x <= self.maks_persediaan):
            self.u_banyak = (x - self.min_persediaan) / (
                self.maks_persediaan - self.min_persediaan
            )
        elif x > self.maks_persediaan:
            self.u_banyak = 1
        return self.u_banyak


class Produksi:
    def __init__(self):
        self.min_produksi = 2000
        self.maks_produksi = 7000

    def _berkurang(self, x):
        if (x >= self.min_produksi) and (x <= self.maks_produksi):
            return (self.maks_produksi - x) / (self.maks_produksi - self.min_produksi)
        elif x < self.min_produksi:
            return 1
        else:
            return 0

    def _bertambah(self, x):
        if (x >= self.min_produksi) and (x <= self.maks_produksi):
            return (x - self.min_produksi) / (self.maks_produksi - self.min_produksi)
        elif x > self.maks_produksi:
            return 1
        else:
            return 0
