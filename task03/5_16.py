class Firma:
    """ Třída reprezentuje firmu"""


    @staticmethod
    def factory_from_obchodni_nazev(string: str):
        try:

            data = string.split(", ")
            if len(data) != 2:
                raise Exception("Incorrect input")

            return Firma(data[0], data[1])

        except Exception as e:
            print(e)

    def __init__(self, nazev, pravni_forma):
        """
        Vytvoří instanci firmy
        :param nazev: Název například Maso a uzeniny od Pavlíka
        :param pravni_forma: Právní forma, například s.r.o, nebo a.s. apod.
        """
        self.jmeno = nazev
        self.pravni_forma = pravni_forma

sporka = Firma.factory_from_obchodni_nazev("Česká spořitelna, a.s.")
print(sporka.pravni_forma) #ma vypsat "a.s."
