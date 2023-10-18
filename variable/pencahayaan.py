from variable.var import Variable


class Pencahayaan(Variable):
    def __init__(self) -> None:
        self.var = Variable()

    def redup(self, cahaya):
        return self.var.kondisi(mins=0, median=150, maks=300, x=cahaya)

    def agakterang(self, cahaya):
        return self.var.kondisi(mins=150, median=300, maks=500, x=cahaya)

    def terang(self, cahaya):
        return self.var.kondisi(mins=300, median=500, maks=700, x=cahaya)
