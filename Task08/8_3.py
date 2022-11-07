class ZvysitelnaUrovenInterface:

    def zvysitUroven(self) -> None:
        raise NotImplemented()


class Bojovnik(ZvysitelnaUrovenInterface):
    def __init__(self, sila):
        if type(sila) is not int or sila < 0 or sila > 3:
            raise Exception("Sila bojovnika neni dostatecne dlouhe")

        self.sila = sila

    def zvysitUroven(self) -> None:
        try:
            if self.sila == 3:
                raise Exception("You have reached limit of your power")

            self.sila += 1
        except Exception as e:
            print(e)


class Mag(ZvysitelnaUrovenInterface):
    def __init__(self, bilaMagie, cernaMagie):
        if type(bilaMagie) is not bool:
            raise Exception("Bila magie musi byt True/False")
        if type(cernaMagie) is not bool:
            raise Exception("Cerna magie musi byt True/False")

        self.cernaMagie = cernaMagie
        self.bilaMagie = bilaMagie

    def zvysitUroven(self) -> None:
        try:
            if self.bilaMagie and self.cernaMagie:
                raise Exception("You learned all magic which you can")

            if self.bilaMagie:
                self.cernaMagie = True

            if self.cernaMagie:
                self.bilaMagie = True

        except Exception as e:
            print(e)


bobik = Bojovnik(1)
bobik.zvysitUroven()
print(bobik.sila)

martina = Mag(True, False)
martina.zvysitUroven()
print(martina.cernaMagie)
