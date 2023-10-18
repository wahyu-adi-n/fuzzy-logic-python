from fuzzy.fuzzy import Fuzzy
from variable.suhu import Suhu
from variable.kebisingan import Kebisingan
from variable.pencahayaan import Pencahayaan
from variable.produksi import Produksi



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
