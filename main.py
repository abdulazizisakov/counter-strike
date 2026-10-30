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


def oyin_boshlash(ct, t):
    navbat = ct
    dushman = t

    while ct.tirimi() and t.tirimi():
        print(f"Navbat: {navbat.nomi}, {navbat.joni}, {navbat.qurol.nomi}")

        print("1) otish 2) oqlash 3) dokon")
        tanlov = input("tanlang: ")

        if tanlov == "1":
            navbat.otish(dushman)
        elif tanlov == "2":
            navbat.qurol.qayta_oqlash()
        elif tanlov == "3":
            dokon(navbat)

        navbat, dushman = dushman, navbat

    if ct.tirimi():
        print(ct.nomi, "yutti joni", ct.joni, ct.puli)
    if t.tirimi():
        print(t.nomi, "yutti joni", t.joni, t.puli)


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

    oyin_boshlash(ct, t)


main()
