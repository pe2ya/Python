class Rectangle:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __new__(cls, a, b):
        try:
            if a < 0 or b < 0:
                raise Exception("You cannot set length below zero")
            obj = super(Rectangle, cls).__new__(cls)
            obj._a = a
            obj._b = b

            return obj
        except Exception as e:
            print(e)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        try:
            if value < 0:
                raise Exception("You cannot set length below zero")

            self._a = value

        except Exception as e:
            print(e)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        try:
            if value < 0:
                raise Exception("You cannot set length below zero")

            self._b = value

        except Exception as e:
            print(e)


z = Rectangle(-1, 1)
x = Rectangle(12, 2)
print(x.a)
print(x.b)
x.a = -1
x.b = -1



