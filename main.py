from qurol import qurollar
from oyinchi import Oyinchi


def dokon(oyinchi):
    print(f"DOKON: {oyinchi.nomi} | {oyinchi.puli}")
    for c, qurol in enumerate(qurollar, start=1):
        print(c)
        qurol.malumot()

    tanlov = input("Qaysi birini sotil olasiz: ")
    if tanlov:
        oyinchi.sotib_ol(qurollar[int(tanlov) - 1])


def main():
    ct_nomi = input("Counter-Terrorist nomi: ")
    t_nomi = input("Terrorist nomi: ")

    ct = Oyinchi(ct_nomi, "CT")
    t = Oyinchi(t_nomi, "T")

    print(ct.nomi, ct.jamoa, ct.puli, ct.qurol.nomi)
    print(t.nomi, t.jamoa, t.puli, t.qurol.nomi)

    dokon(ct)
    dokon(t)

    print(ct.nomi, ct.jamoa, ct.puli, ct.qurol.nomi)
    print(t.nomi, t.jamoa, t.puli, t.qurol.nomi)


main()
