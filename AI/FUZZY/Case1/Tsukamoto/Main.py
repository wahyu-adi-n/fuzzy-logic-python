from Variable import *
from Rules import *
from Modules import *


def main():
    x = 4000
    y = 300
    z = 0
    permintaan = Permintaan()
    persediaan = Persediaan()
    produksi = Produksi()
    rules = Rules()

    u_turun, u_naik = permintaan._turun(x), permintaan._naik(x)
    u_sedikit, u_banyak = persediaan._sedikit(y), persediaan._banyak(y)
    print(u_turun, u_naik, u_sedikit, u_banyak)
    rules.rule_1(u_turun, u_banyak)
    rules.rule_2(u_turun, u_sedikit)
    rules.rule_3(u_naik, u_banyak)
    rules.rule_4(u_naik, u_sedikit)

    apred_list, r_list = rules.aggregasi()
    print(apred_list, r_list)
    deffuz = deffuzifikasi(apred_list, r_list)
    print(deffuz)


if __name__ == "__main__":
    main()
