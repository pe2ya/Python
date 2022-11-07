class VazitelneInterface:

    def get_vaha_v_kg(self):
        raise NotImplemented(":(")

    def get_cena_za_kg(self):
        raise NotImplemented(":(")



class KusoveInterface:

    def get_pocet_kusu_v_baleni(self):
        raise NotImplemented(":(")

    def get_cena_za_kus(self):
        raise NotImplemented(":(")

    def get_cena_za_baleni(self):
        raise NotImplemented(":(")


class ZlevnitelneInterface:

    def set_sleva(self, value):
        raise NotImplemented(":(")

    def get_cena_po_sleve(self):
        raise NotImplemented(":(")