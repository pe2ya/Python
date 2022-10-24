class KonfiguraceKonference(int):

    _maximalni_pocet_ucastniku = 0

    def __new__(cls, *args, **kwargs):
        try:
            if cls is KonfiguraceKonference:
                raise Exception("You cannot create an object of this class")

        except Exception as e:
            print(e)

    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        cls._maximalni_pocet_ucastniku = max

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        return cls._maximalni_pocet_ucastniku


print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

KonfiguraceKonference.set_maximalni_pocet_ucastniku(212)
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

mojeKonfigurace = KonfiguraceKonference()
# mojeKonfigurace.set_maximalni_pocet_ucastniku(300)
print(mojeKonfigurace.get_maximalni_pocet_ucastniku())
