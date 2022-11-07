import re

class Zbozi:
    def __init__(self, nazev, cena):
        """
        Nastavi cenu a nazev zbozi
        :param nazev: str Nazev jen znaky anglicke abecedy 2-50
        :param cena: float 0 az 1mio, kladne cislo
        """
        assert type(nazev) == str and re.match(r"[a-zA-Z]{2,50}", nazev)
        assert (type(cena) == float or type(cena) == int) and cena > 0 and cena < 1000000
        self._nazev = nazev
        self._cena = cena

    def get_cena(self):
        """
        Vrati cenu
        :return: int
        """
        return self._cena



class ZlevneneZbozi(Zbozi):
    def __init__(self, name: str, price: int, discount: float):
        Zbozi.__init__(self, name, price)
        self._discount = None

        self.disc = discount

    @property
    def disc(self):
        return self._discount

    @disc.setter
    def disc(self, value):
        try:
            if (value < 0 or value > 0.5) or not isinstance(value, float):
                raise Exception("discount number must be in range <0; 0.5>")

            self._discount = value
        except Exception as e:
            print(e)


    def get_cena(self):
        try:
            return self._cena - (self._cena * self._discount)

        except Exception as e:
            print(e)



apple = ZlevneneZbozi("apple", 100, 0.7)

print(apple.get_cena())




