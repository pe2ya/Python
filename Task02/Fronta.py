class MyList:
    def __init__(self, arr):
        if type(list()) == arr:
            self.ls = arr
        else:
            self.ls = [arr]

    def len(self):
        result = 0
        for _ in self.ls:
            result += 1

        return result

    def push(self, el):
        if self.check(el):
            self.ls += [el]

    def pop(self):
        el = self.ls[0]
        del self.ls[0]

        return el

    def check(self, el):
        try:
            length = self.len()
            if length == 0:
                return True
            else:
                el_type = type(self.ls[0])
                if el_type == type(el):
                    return True
                else:
                    string = str(el_type)
                    string = string.strip("<class '")
                    string = string.strip("'>")
                    raise Exception("Invalid variable type. List variable type: " + string)
        except Exception as e:
            print(e)

    def __str__(self):
        return str(self.ls)


a = MyList([1, 2, 3, 5, 6])
print(a)

print(a.len())

print(a.pop())
print(a)

a.push(4)
a.push("b")
print(a)
