class VazitelneInterface:

    def get_vaha_v_kg(self) -> float:
        raise NotImplemented(":(")

    def get_cena_za_kg(self) -> float:
        raise NotImplemented(":(")



class KusoveInterface:

    def get_pocet_kusu_v_baleni(self) -> int:
        raise NotImplemented(":(")

    def get_cena_za_kus(self) -> float:
        raise NotImplemented(":(")

    def get_cena_za_baleni(self) -> float:
        raise NotImplemented(":(")


class ZlevnitelneInterface:

    def set_sleva(self, value) -> float:
        raise NotImplemented(":(")

    def get_cena_po_sleve(self) -> float:
        raise NotImplemented(":(")