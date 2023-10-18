from variable.var import Variable


class Suhu(Variable):
    def __init__(self) -> None:
        self.var = Variable()

    def rendah(self, suhu):
        return self.var.kondisi(mins=18, median=22, maks=26, x=suhu)

    def normal(self, suhu):
        return self.var.kondisi(mins=22, median=26, maks=32, x=suhu)

    def tinggi(self, suhu):
        return self.var.kondisi(mins=26, median=32, maks=38, x=suhu)
