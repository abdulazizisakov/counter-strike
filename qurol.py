class Qurol:
    def __init__(self, nomi, narxi, magazin, zarar):
        self.nomi = nomi
        self.narxi = narxi
        self.magazin = magazin
        self.oqlar_soni = self.magazin
        self.zarar = zarar

    def otish(self):
        if self.oqlar_soni > 0:
            self.oqlar_soni -= 1
        else:
            print("oq tugagan, qayta oqlang")

    def qayta_oqlash(self):
        self.oqlar_soni = self.magazin

    def malumot(self):
        print(
            f"Qurol: {self.nomi}, oqlar soni: {self.oqlar_soni}, zarar: {self.zarar}, {self.narxi}"
        )


qurollar = [
    Qurol("Glock-18", 200, 14, 15),
    Qurol("USP-S", 500, 16, 20),
    Qurol("P250", 300, 12, 18),
    Qurol("AK-47", 2700, 30, 40),
    Qurol("AWP", 4750, 5, 80),
]
