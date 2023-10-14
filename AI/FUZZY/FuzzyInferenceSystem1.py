class Permintaan:
    def turun(self, mins=1000, maks=5000, permintaan=0):
        if permintaan < mins:
            return 1
        elif permintaan >= mins and permintaan <= maks:
            return (maks - permintaan) / (maks - mins)
        else:
            return 0

    def naik(self, mins=1000, maks=5000, permintaan=0):
        if permintaan < mins:
            return 0
        elif permintaan >= mins and permintaan <= maks:
            return (permintaan - mins) / (maks - mins)
        else:
            return 1


class Persediaan:
    def sedikit(self, mins=100, maks=600, persediaan=0):
        if persediaan < mins:
            return 1
        elif persediaan >= mins and persediaan <= maks:
            return (maks - persediaan) / (maks - mins)
        else:
            return 0

    def banyak(self, mins=100, maks=600, persediaan=0):
        if persediaan < mins:
            return 0
        elif persediaan >= mins and persediaan <= maks:
            return (persediaan - mins) / (maks - mins)
        else:
            return 1


class Produksi:
    def agregasi_berkurang(self, mins=2000, maks=7000, nilai_minimal=0):
        return maks - ((maks - mins) * nilai_minimal)

    def agregasi_bertambah(self, mins=2000, maks=7000, nilai_minimal=0):
        return mins + ((maks - mins) * nilai_minimal)


class Fuzzy:
    def __init__(self, x, y) -> None:
        self.alpha = []
        self.z = []
        self.nk = {}
        self.x = x
        self.y = y

    def cari_nilai_minimal(self, a, b) -> float:
        return min(a, b)

    def defuzzifikasi(self) -> float:
        alpha_z_product_sums = 0
        alpha_sums = 0
        for i in range(len(self.alpha)):
            alpha_z_product_sums += self.alpha[i] * self.z[i]
            alpha_sums += self.alpha[i]
        z_akhir = alpha_z_product_sums // alpha_sums
        return z_akhir


class FuzzyTsukamoto(Fuzzy):
    def aturan(self) -> dict:
        return {
            1: ["permintaan_turun", "persediaan_banyak", "berkurang"],
            2: ["permintaan_turun", "persediaan_sedikit", "berkurang"],
            3: ["permintaan_naik", "persediaan_banyak", "bertambah"],
            4: ["permintaan_naik", "persediaan_sedikit", "bertambah"],
        }

    def hitung_nilai_keanggotaan(self) -> dict:
        permintaan = Permintaan()
        persediaan = Persediaan()

        self.nk["permintaan_naik"] = permintaan.naik(permintaan=self.x)
        self.nk["permintaan_turun"] = permintaan.turun(permintaan=self.x)
        self.nk["persediaan_banyak"] = persediaan.banyak(persediaan=self.y)
        self.nk["persediaan_sedikit"] = persediaan.sedikit(persediaan=self.y)

        return self.nk

    def fuzzifikasi(self):
        produksi = Produksi()
        rules = self.aturan()
        nk = self.hitung_nilai_keanggotaan()

        for _, rule in rules.items():
            nilai_minimal = self.cari_nilai_minimal(a=nk[rule[0]], b=nk[rule[1]])
            self.alpha.append(nilai_minimal)

            if rule[-1] == "berkurang":
                nilai_agregasi = produksi.agregasi_berkurang(
                    nilai_minimal=nilai_minimal
                )
            elif rule[-1] == "bertambah":
                nilai_agregasi = produksi.agregasi_bertambah(
                    nilai_minimal=nilai_minimal
                )
            else:
                raise NotImplementedError
            self.z.append(nilai_agregasi)


class FuzzySugeno(Fuzzy):
    def aturan(self) -> dict:
        return {
            1: ["permintaan_turun", "persediaan_banyak", self.x - self.y],
            2: ["permintaan_turun", "persediaan_sedikit", self.x],
            3: ["permintaan_naik", "persediaan_banyak", self.x],
            4: ["permintaan_naik", "persediaan_sedikit", 1.25 * self.x - self.y],
        }

    def hitung_nilai_keanggotaan(self) -> dict:
        permintaan = Permintaan()
        persediaan = Persediaan()

        self.nk["permintaan_naik"] = permintaan.naik(permintaan=self.x)
        self.nk["permintaan_turun"] = permintaan.turun(permintaan=self.x)
        self.nk["persediaan_banyak"] = persediaan.banyak(persediaan=self.y)
        self.nk["persediaan_sedikit"] = persediaan.sedikit(persediaan=self.y)

        return self.nk

    def fuzzifikasi(self):
        rules = self.aturan()
        nk = self.hitung_nilai_keanggotaan()

        for _, rule in rules.items():
            nilai_minimal = self.cari_nilai_minimal(a=nk[rule[0]], b=nk[rule[1]])
            self.alpha.append(nilai_minimal)
            nilai_agregasi = rule[-1]
            self.z.append(nilai_agregasi)


class FuzzyMamdani(Fuzzy):
    def aturan(self) -> dict:
        return {
            1: ["permintaan_turun", "persediaan_banyak", "berkurang"],
            2: ["permintaan_turun", "persediaan_sedikit", "berkurang"],
            3: ["permintaan_naik", "persediaan_banyak", "bertambah"],
            4: ["permintaan_naik", "persediaan_sedikit", "bertambah"],
        }

    def hitung_nilai_keanggotaan(self) -> dict:
        permintaan = Permintaan()
        persediaan = Persediaan()

        self.nk["permintaan_naik"] = permintaan.naik(permintaan=self.x)
        self.nk["permintaan_turun"] = permintaan.turun(permintaan=self.x)
        self.nk["persediaan_banyak"] = persediaan.banyak(persediaan=self.y)
        self.nk["persediaan_sedikit"] = persediaan.sedikit(persediaan=self.y)

        return self.nk

    def fuzzifikasi(self):
        rules = self.aturan()
        nk = self.hitung_nilai_keanggotaan()

        for _, rule in rules.items():
            nilai_minimal = self.cari_nilai_minimal(a=nk[rule[0]], b=nk[rule[1]])
            self.alpha.append(nilai_minimal)
            nilai_agregasi = rule[-1]
            self.z.append(nilai_agregasi)


def main():
    print("== Program Fuzzy Logic ==")
    print("=" * 50)
    print("[1] Logika Fuzzy Tsukamoto")
    print("[2] Logika Fuzzy Sugeno")
    print("[3] Logika Fuzzy Mamdani")

    while True:
        try:
            logic = int(input("Masukkan Jenis Fuzzy Logic (1/2/3): "))
        except ValueError:
            logic = 1

        permintaan = 4000
        persediaan = 300

        if logic == 1:
            print("Fuzzy Tsukamoto")
            print("=" * 50)
            tsukamoto = FuzzyTsukamoto(x=permintaan, y=persediaan)
            tsukamoto.fuzzifikasi()
            print(f"Fuzzy Out: {tsukamoto.defuzzifikasi()}")

        elif logic == 2:
            print("Fuzzy Sugeno")
            print("=" * 50)

            sugeno = FuzzySugeno(x=permintaan, y=persediaan)
            sugeno.fuzzifikasi()
            print(f"Fuzzy Out: {sugeno.defuzzifikasi()}")

        elif logic == 3:
            print("Fuzzy Mamdani")
            print("=" * 50)
            # mamdani = FuzzyMamdani(x=permintaan, y=persediaan)
            # mamdani.fuzzifikasi()
            # print(f"Fuzzy Out: {mamdani.defuzzifikasi()}")
        else:
            print("FUZZY INFERENCE SYSTEM")
            break


if __name__ == "__main__":
    main()
