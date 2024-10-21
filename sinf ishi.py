#start
#1 vazifa
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def salomlashish(self):
        print(f"Salom {self.ism}")

ism = input("Ismingizni kiriting: ")

odam = Odam(ism)

odam.salomlashish()

#2 vazifa
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def kuylash(self):
        print(f"{self.ism} kuylamoqda... 🎶")

    def eshitish(self):
        print(f"{self.ism} kuy eshitmoqda...")

    def gapirish(self, boshqa_ism):
        print(f"{self.ism}: Juda yaxshi kuylading, {boshqa_ism}!")

odam1 = Odam("Azamjon")
odam2 = Odam("Javlonbek")

odam1.kuylash()

odam2.eshitish()
odam2.gapirish(odam1.ism)
#end code

#heloo
#nyreuge

print("Hello world")