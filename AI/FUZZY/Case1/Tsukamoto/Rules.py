from Variable import Produksi


class Rules:
    def __init__(self):
        self.apred1 = 0
        self.apred2 = 0
        self.apred3 = 0
        self.apred4 = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0

    def rule_1(self, u_turun, u_banyak):
        self.apred1 = min(u_turun, u_banyak)
        produksi = Produksi()
        maks_produksi = produksi.maks_produksi
        selisih = 5000
        self.r1 = maks_produksi - (selisih * self.apred1)

    def rule_2(self, u_turun, u_sedikit):
        self.apred2 = min(u_turun, u_sedikit)
        produksi = Produksi()
        maks_produksi = produksi.maks_produksi
        selisih = 5000
        self.r2 = maks_produksi - (selisih * self.apred2)

    def rule_3(self, u_naik, u_banyak):
        self.apred3 = min(u_naik, u_banyak)
        produksi = Produksi()
        min_produksi = produksi.min_produksi
        selisih = 5000
        self.r3 = min_produksi + (selisih * self.apred3)

    def rule_4(self, u_naik, u_sedikit):
        self.apred4 = min(u_naik, u_sedikit)
        produksi = Produksi()
        min_produksi = produksi.min_produksi
        selisih = 5000
        self.r4 = min_produksi + (selisih * self.apred4)

    def aggregasi(self):
        return [self.apred1, self.apred2, self.apred3, self.apred4], [
            self.r1,
            self.r2,
            self.r3,
            self.r4,
        ]
