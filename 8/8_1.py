import re


class Ikea:
    def __init__(self, number_sh: int, number_st: str, name: str, price: int):
        self.number_sh = None
        self.number_st = None
        self.name = name
        self.price = price

        self.number_street = number_st
        self.number_shelf = number_sh

    @property
    def number_shelf(self):
        return self.number_sh

    @number_shelf.setter
    def number_shelf(self, value):
        try:
            if value < 0 or value > 100:
                raise Exception("shelf number must be in range <0; 100>")

            self.number_sh = value
        except Exception as e:
            print(e)

    @property
    def number_street(self):
        return self.number_st

    @number_street.setter
    def number_street(self, value):
        exp = "^[A-K]{1}$"

        try:
            x = re.search(exp, value)

            if not x:
                raise Exception("street number must be in range A-K")

            else:
                self.number_st = value

        except Exception as e:
            print(e)

    def __str__(self):
        return str(vars(self))


class MeasureableIkeaItem:
    def __init__(self, width: int, height: int, length: int):
        self.width = width
        self.height = height
        self.length = length


class PlasticWasteIkeaItem:
    def __init__(self, used_plastic: int):
        self.used_plastic = used_plastic


class Lack(Ikea, MeasureableIkeaItem):
    def __init__(self, number_sh: int, number_st: str, name: str, price: int,
                 width: int, height: int, length: int,
                 color: str):

        Ikea.__init__(self, number_sh, number_st, name, price)
        MeasureableIkeaItem.__init__(self, width, height, length)
        self.color = color


class SamlaBox(Ikea, MeasureableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, number_sh: int, number_st: str, name: str, price: int,
                 width: int, height: int, length: int,
                 used_plastic: int,
                 volume: float):

        Ikea.__init__(self, number_sh, number_st, name, price)
        MeasureableIkeaItem.__init__(self, width, height, length)
        PlasticWasteIkeaItem.__init__(self, used_plastic)
        self.volume = volume


class Sjorapport(Ikea, PlasticWasteIkeaItem):
    def __init__(self, number_sh: int, number_st: str, name: str, price: int,
                 used_plastic: int,
                 expire: float, weight: float):

        Ikea.__init__(self, number_sh, number_st, name, price)
        PlasticWasteIkeaItem.__init__(self, used_plastic)
        self.expire = expire
        self.weight = weight



ikea = Ikea(1, "A", "name", 2)
lack = Lack(2, "C", "name", 4, 100, 200, 300, "red")
samla_box = SamlaBox(3, "F", "name", 3, 150, 250, 350, 122, 23.5)
sjorapport = Sjorapport(4, "D", "name", 45, 122, 1.5, 32)

print(ikea)
print(lack)
print(samla_box)
print(sjorapport)


