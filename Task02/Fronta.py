class My_list:
    def __init__(self, arr):
        self.ls = arr

    def len(self):
        result = 0
        for x in self.ls:
            result += 1

        return result

    def push(self, el):
        self.ls = [el] + self.ls

    def pop(self):
        el = self.ls[0]
        del self.ls[0]

        return el

    def __str__(self):
        return str(self.ls)


a = My_list([1, 2, 3, 5, 6])
print(a)

print(a.len())

print(a.pop())
print(a)

a.push(4)
print(a)


