class Variable:
    def kondisi(self, mins, median, maks, x):
        if x < mins or x > maks:
            return 0
        elif x >= mins and x <= median:
            return (x - mins) / (median - mins)
        elif x >= median and x <= maks:
            return (maks - x) / (maks - median)


class Suhu(Variable):
    def __init__(self) -> None:
        self.var = Variable()

    def rendah(self, suhu):
        return self.var.kondisi(mins=18, median=22, maks=26, x=suhu)

    def normal(self, suhu):
        return self.var.kondisi(mins=22, median=26, maks=32, x=suhu)

    def tinggi(self, suhu):
        return self.var.kondisi(mins=26, median=32, maks=38, x=suhu)


class Kebisingan(Variable):
    def __init__(self) -> None:
        self.var = Variable()

    def tenang(self, bising):
        return self.var.kondisi(mins=35, median=55, maks=75, x=bising)

    def agakbising(self, bising):
        return self.var.kondisi(mins=55, median=75, maks=90, x=bising)

    def bising(self, bising):
        return self.var.kondisi(mins=75, median=90, maks=105, x=bising)


class Pencahayaan(Variable):
    def __init__(self) -> None:
        self.var = Variable()

    def redup(self, cahaya):
        return self.var.kondisi(mins=0, median=150, maks=300, x=cahaya)

    def agakterang(self, cahaya):
        return self.var.kondisi(mins=150, median=300, maks=500, x=cahaya)

    def terang(self, cahaya):
        return self.var.kondisi(mins=300, median=500, maks=700, x=cahaya)


class Produksi:
    def agregasi_berkurang(self, mins, maks, nilai_minimal):
        return maks - ((maks - mins) * nilai_minimal)

    def agregasi_bertambah(self, mins, maks, nilai_minimal):
        return mins + ((maks - mins) * nilai_minimal)


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


class FuzzyTsukamoto(Fuzzy):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

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

        self.nk["suhu_rendah"] = suhu.rendah(suhu=self.a)
        self.nk["suhu_normal"] = suhu.normal(suhu=self.a)
        self.nk["suhu_tinggi"] = suhu.tinggi(suhu=self.a)
        self.nk["bising_tenang"] = bising.tenang(bising=self.b)
        self.nk["bising_agakbising"] = bising.agakbising(bising=self.b)
        self.nk["bising_bising"] = bising.bising(bising=self.b)
        self.nk["cahaya_redup"] = cahaya.redup(cahaya=self.c)
        self.nk["cahaya_agakterang"] = cahaya.agakterang(cahaya=self.c)
        self.nk["cahaya_terang"] = cahaya.terang(cahaya=self.c)

        return self.nk

    def fuzzifikasi(self):
        produksi = Produksi()
        rules = self.aturan()
        nk = self.hitung_nilai_keanggotaan()

        for _, rule in rules.items():
            nilai_minimal = self.cari_nilai_minimal(
                x=nk[rule[0]], y=nk[rule[1]], z=nk[rule[2]]
            )
            self.alpha.append(nilai_minimal)

            if rule[-1] == "berkurang":
                nilai_agregasi = produksi.agregasi_berkurang(
                    mins=143, maks=153, nilai_minimal=nilai_minimal
                )
            elif rule[-1] == "bertambah":
                nilai_agregasi = produksi.agregasi_bertambah(
                    mins=143, maks=153, nilai_minimal=nilai_minimal
                )
            else:
                raise NotImplementedError
            self.z.append(nilai_agregasi)


class FuzzySugeno(Fuzzy):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def aturan(self) -> dict:
        return {
            1: ["suhu_rendah", "bising_tenang", "cahaya_redup", 148.0],
            2: ["suhu_rendah", "bising_tenang", "cahaya_agakterang", 150.9],
            3: ["suhu_rendah", "bising_tenang", "cahaya_terang", 146.5],
            4: ["suhu_rendah", "bising_agakbising", "cahaya_redup", 143.1],
            5: ["suhu_rendah", "bising_agakbising", "cahaya_agakterang", 146.53],
            6: ["suhu_rendah", "bising_agakbising", "cahaya_terang", 142.73],
            7: ["suhu_rendah", "bising_bising", "cahaya_redup", 136.73],
            8: ["suhu_rendah", "bising_bising", "cahaya_agakterang", 140.77],
            9: ["suhu_rendah", "bising_bising", "cahaya_terang", 135.97],
            10: ["suhu_normal", "bising_tenang", "cahaya_redup", 149.73],
            11: ["suhu_normal", "bising_tenang", "cahaya_agakterang", 153.27],
            12: ["suhu_normal", "bising_tenang", "cahaya_terang", 152.13],
            13: ["suhu_normal", "bising_agakbising", "cahaya_redup", 148.0],
            14: ["suhu_normal", "bising_agakbising", "cahaya_agakterang", 150.63],
            15: ["suhu_normal", "bising_agakbising", "cahaya_terang", 147.63],
            16: ["suhu_normal", "bising_bising", "cahaya_redup", 141.47],
            17: ["suhu_normal", "bising_bising", "cahaya_agakterang", 145.67],
            18: ["suhu_normal", "bising_bising", "cahaya_terang", 140.2],
            19: ["suhu_tinggi", "bising_tenang", "cahaya_redup", 142.10],
            20: ["suhu_tinggi", "bising_tenang", "cahaya_agakterang", 146.53],
            21: ["suhu_tinggi", "bising_tenang", "cahaya_terang", 142.17],
            22: ["suhu_tinggi", "bising_agakbising", "cahaya_redup", 138.7],
            23: ["suhu_tinggi", "bising_agakbising", "cahaya_agakterang", 141.4],
            24: ["suhu_tinggi", "bising_agakbising", "cahaya_terang", 138.3],
            25: ["suhu_tinggi", "bising_bising", "cahaya_redup", 133.33],
            26: ["suhu_tinggi", "bising_bising", "cahaya_agakterang", 138.33],
            27: ["suhu_tinggi", "bising_bising", "cahaya_terang", 133.77],
        }

    def hitung_nilai_keanggotaan(self) -> dict:
        suhu = Suhu()
        bising = Kebisingan()
        cahaya = Pencahayaan()

        self.nk["suhu_rendah"] = suhu.rendah(suhu=self.a)
        self.nk["suhu_normal"] = suhu.normal(suhu=self.a)
        self.nk["suhu_tinggi"] = suhu.tinggi(suhu=self.a)
        self.nk["bising_tenang"] = bising.tenang(bising=self.b)
        self.nk["bising_agakbising"] = bising.agakbising(bising=self.b)
        self.nk["bising_bising"] = bising.bising(bising=self.b)
        self.nk["cahaya_redup"] = cahaya.redup(cahaya=self.c)
        self.nk["cahaya_agakterang"] = cahaya.agakterang(cahaya=self.c)
        self.nk["cahaya_terang"] = cahaya.terang(cahaya=self.c)

        return self.nk

    def fuzzifikasi(self):
        rules = self.aturan()
        nk = self.hitung_nilai_keanggotaan()

        for _, rule in rules.items():
            nilai_minimal = self.cari_nilai_minimal(
                x=nk[rule[0]], y=nk[rule[1]], z=nk[rule[2]]
            )
            self.alpha.append(nilai_minimal)
            nilai_agregasi = rule[-1]
            self.z.append(nilai_agregasi)


class FuzzyMamdani(Fuzzy):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

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

        self.nk["suhu_rendah"] = suhu.rendah(suhu=self.a)
        self.nk["suhu_normal"] = suhu.normal(suhu=self.a)
        self.nk["suhu_tinggi"] = suhu.tinggi(suhu=self.a)
        self.nk["bising_tenang"] = bising.tenang(bising=self.b)
        self.nk["bising_agakbising"] = bising.agakbising(bising=self.b)
        self.nk["bising_bising"] = bising.bising(bising=self.b)
        self.nk["cahaya_redup"] = cahaya.redup(cahaya=self.c)
        self.nk["cahaya_agakterang"] = cahaya.agakterang(cahaya=self.c)
        self.nk["cahaya_terang"] = cahaya.terang(cahaya=self.c)

        return self.nk

    def fuzzifikasi(self):
        pass

    def defuzzifikasi(self):
        pass


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

        suhu = int(input("Masukkan Nilai Suhu: "))
        bising = int(input("Masukkan Nilai Kebisingan: "))
        cahaya = int(input("Masukkan Nilai Pencahayaan: "))

        if logic == 1:
            print("\nFuzzy Tsukamoto")
            print("=" * 50)
            tsukamoto = FuzzyTsukamoto(a=suhu, b=bising, c=cahaya)
            tsukamoto.fuzzifikasi()
            print(f"Fuzzy Out: {tsukamoto.defuzzifikasi():.2f}")

        elif logic == 2:
            print("\nFuzzy Sugeno")
            print("=" * 50)

            sugeno = FuzzySugeno(a=suhu, b=bising, c=cahaya)
            sugeno.fuzzifikasi()
            print(f"Fuzzy Out: {sugeno.defuzzifikasi():.2f}")

        elif logic == 3:
            print("\nFuzzy Mamdani")
            print("=" * 50)
            mamdani = FuzzyMamdani(a=suhu, b=bising, c=cahaya)
            mamdani.fuzzifikasi()
            # print(f"Fuzzy Out: {mamdani.defuzzifikasi():.2f}")
        else:
            print("FUZZY INFERENCE SYSTEM")
            break


if __name__ == "__main__":
    main()
