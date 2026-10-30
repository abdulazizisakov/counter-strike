from random import choice

from qurol import qurollar, Qurol


class Oyinchi:
    def __init__(self, nomi, jamoa):
        self.nomi = nomi
        self.jamoa = jamoa
        self.joni = 100
        self.puli = 1000
        self.qurol = choice(qurollar)

    def sotib_ol(self, qurol):
        if self.puli >= qurol.narxi:
            self.qurol = qurol
            self.puli -= qurol.narxi
        else:
            print("mablag yetarli emas.")

    def zarar_ol(self, qurol):
        self.joni -= qurol.zarar

        if self.joni < 0:
            self.joni = 0
            self.puli += 1500

        if self.joni == 0:
            print(f"{self.nomi} oldi.")

    def tirimi(self):
        return self.joni > 0
