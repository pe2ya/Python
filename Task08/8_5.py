class A:

    def __init__(self):
        self.a_variable = True

    def test(self) -> None:
        print("A class")


class B:

    def __init__(self):
        self.b_variable = True

    def test(self) -> None:
        print("B class")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()
c.test()

print(vars(c))
