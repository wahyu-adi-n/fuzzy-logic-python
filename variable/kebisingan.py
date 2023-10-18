from variable.var import Variable


class Kebisingan(Variable):
    def __init__(self) -> None:
        self.var = Variable()

    def tenang(self, bising):
        return self.var.kondisi(mins=35, median=55, maks=75, x=bising)

    def agakbising(self, bising):
        return self.var.kondisi(mins=55, median=75, maks=90, x=bising)

    def bising(self, bising):
        return self.var.kondisi(mins=75, median=90, maks=105, x=bising)
