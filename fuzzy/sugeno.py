from fuzzy.fuzzy import Fuzzy
from variable.suhu import Suhu
from variable.kebisingan import Kebisingan
from variable.pencahayaan import Pencahayaan


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
