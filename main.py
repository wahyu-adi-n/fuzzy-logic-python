from fuzzy.tsukamoto import FuzzyTsukamoto
from fuzzy.sugeno import FuzzySugeno
from fuzzy.mamdani import FuzzyMamdani


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
            # mamdani = FuzMamdani(a=suhu, b=bising, c=cahaya)
            # mamdani.fuzzifikasi(zy)
            # print(f"Fuzzy Out: {mamdani.defuzzifikasi():.2f}")
        else:
            print("FUZZY INFERENCE SYSTEM")
            break


if __name__ == "__main__":
    main()
