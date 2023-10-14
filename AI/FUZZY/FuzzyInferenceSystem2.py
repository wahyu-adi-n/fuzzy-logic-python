class Suhu:
    def rendah(self, mins=18, median=22, maks=26, suhu=0):
        if suhu < mins or suhu > maks:
            return 0
        elif suhu >= mins and suhu <= median:
            return (suhu - mins) / (median - mins)
        elif suhu >= median and suhu <= maks:
            return (maks - suhu) / (maks - median)

    def normal(self, mins=22, median=26, maks=32, suhu=0):
        if suhu < mins or suhu > maks:
            return 0
        elif suhu >= mins and suhu <= median:
            return (suhu - mins) / (median - mins)
        elif suhu >= median and suhu <= maks:
            return (maks - suhu) / (maks - median)

    def tinggi(self, mins=26, median=32, maks=38, suhu=0):
        if suhu < mins or suhu > maks:
            return 0
        elif suhu >= mins and suhu <= median:
            return (suhu - mins) / (median - mins)
        elif suhu >= median and suhu <= maks:
            return (maks - suhu) / (maks - median)


class Kebisingan:
    def tenang(self, mins=35, median=55, maks=75, bising=0):
        if bising < mins or bising > maks:
            return 0
        elif bising >= mins and bising <= median:
            return (bising - mins) / (median - mins)
        elif bising >= median and bising <= maks:
            return (maks - bising) / (maks - median)

    def agakbising(self, mins=55, median=75, maks=90, bising=0):
        if bising < mins or bising > maks:
            return 0
        elif bising >= mins and bising <= median:
            return (bising - mins) / (median - mins)
        elif bising >= median and bising <= maks:
            return (maks - bising) / (maks - median)

    def bising(self, mins=75, median=90, maks=105, bising=0):
        if bising < mins or bising > maks:
            return 0
        elif bising >= mins and bising <= median:
            return (bising - mins) / (median - mins)
        elif bising >= median and bising <= maks:
            return (maks - bising) / (maks - median)


class Pencahayaan:
    def redup(self, mins=0, median=150, maks=300, cahaya=0):
        if cahaya < mins or cahaya > maks:
            return 0
        elif cahaya >= mins and cahaya <= median:
            return (cahaya - mins) / (median - mins)
        elif cahaya >= median and cahaya <= maks:
            return (maks - cahaya) / (maks - median)

    def agakterang(self, mins=150, median=300, maks=500, cahaya=0):
        if cahaya < mins or cahaya > maks:
            return 0
        elif cahaya >= mins and cahaya <= median:
            return (cahaya - mins) / (median - mins)
        elif cahaya >= median and cahaya <= maks:
            return (maks - cahaya) / (maks - median)

    def terang(self, mins=300, median=500, maks=700, cahaya=0):
        if cahaya < mins or cahaya > maks:
            return 0
        elif cahaya >= mins and cahaya <= median:
            return (cahaya - mins) / (median - mins)
        elif cahaya >= median and cahaya <= maks:
            return (maks - cahaya) / (maks - median)


class Produksi:
    def agregasi_berkurang(self, mins=143, maks=153, nilai_minimal=0):
        return maks - ((maks - mins) * nilai_minimal)

    def agregasi_bertambah(self, mins=143, maks=153, nilai_minimal=0):
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
            1: ["suhu_rendah", "bising_tenang", "cahaya_redup", "bertambah"],
            2: ["suhu_rendah", "bising_tenang", "cahaya_agakterang", "bertambah"],
            3: ["suhu_rendah", "bising_tenang", "cahaya_terang", "bertambah"],
            4: ["suhu_rendah", "bising_agakbising", "cahaya_redup", "bertambah"],
            5: ["suhu_rendah", "bising_agakbising", "cahaya_agakterang", "bertambah"],
            6: ["suhu_rendah", "bising_agakbising", "cahaya_terang", "berkurang"],
            7: ["suhu_rendah", "bising_bising", "cahaya_redup", "berkurang"],
            8: ["suhu_rendah", "bising_bising", "cahaya_agakterang", "berkurang"],
            9: ["suhu_rendah", "bising_bising", "cahaya_terang", "berkurang"],
            10: ["suhu_normal", "bising_tenang", "cahaya_redup", "bertambah"],
            11: ["suhu_normal", "bising_tenang", "cahaya_agakterang", "bertambah"],
            12: ["suhu_normal", "bising_tenang", "cahaya_terang", "bertambah"],
            13: ["suhu_normal", "bising_agakbising", "cahaya_redup", "bertambah"],
            14: ["suhu_normal", "bising_agakbising", "cahaya_agakterang", "bertambah"],
            15: ["suhu_normal", "bising_agakbising", "cahaya_terang", "bertambah"],
            16: ["suhu_normal", "bising_bising", "cahaya_redup", "berkurang"],
            17: ["suhu_normal", "bising_bising", "cahaya_agakterang", "bertambah"],
            18: ["suhu_normal", "bising_bising", "cahaya_terang", "berkurang"],
            19: ["suhu_tinggi", "bising_tenang", "cahaya_redup", "berkurang"],
            20: ["suhu_tinggi", "bising_tenang", "cahaya_agakterang", "bertambah"],
            21: ["suhu_tinggi", "bising_tenang", "cahaya_terang", "berkurang"],
            22: ["suhu_tinggi", "bising_agakbising", "cahaya_redup", "berkurang"],
            23: ["suhu_tinggi", "bising_agakbising", "cahaya_agakterang", "berkurang"],
            24: ["suhu_tinggi", "bising_agakbising", "cahaya_terang", "berkurang"],
            25: ["suhu_tinggi", "bising_bising", "cahaya_redup", "berkurang"],
            26: ["suhu_tinggi", "bising_bising", "cahaya_agakterang", "berkurang"],
            27: ["suhu_tinggi", "bising_bising", "cahaya_terang", "berkurang"],
        }

    def hitung_nilai_keanggotaan(self) -> dict:
        suhu = Suhu()
        bising = Kebisingan()
        cahaya = Pencahayaan()

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
