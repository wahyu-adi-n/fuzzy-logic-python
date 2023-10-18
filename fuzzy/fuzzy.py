class Fuzzy:
    def __init__(self, a, b, c):
        self.alpha = []
        self.z = []
        self.nk = {}
        self.a = a
        self.b = b
        self.c = c

    def cari_nilai_minimal(self, x, y, z) -> float:
        return min(x, y, z)

    def defuzzifikasi(self) -> float:
        alpha_z_product_sums = 0
        alpha_sums = 0
        for i in range(len(self.alpha)):
            alpha_z_product_sums += self.alpha[i] * self.z[i]
            alpha_sums += self.alpha[i]
        z_akhir = alpha_z_product_sums / alpha_sums
        return z_akhir
