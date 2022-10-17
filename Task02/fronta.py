class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        prev = ""
        nxt = ""
        if self.next is not None:
            nxt = str(self.next) + " <- "

        if self.previous is not None:
            prev = "<- " + str(self.previous)

        return f"{nxt}{self.value} {prev}"


class MyList:
    def __init__(self):
        self.ls = list()

    def count(self):
        result = 0
        for _ in self.ls:
            result += 1

        return result

    def add(self, node_value) -> None:
        new_node = Node(node_value)

        length = len(self.ls)
        if length > 0:
            self.ls[-1].previous = node_value
            last_node_value = self.ls[-1].value
            new_node.next = last_node_value

        self.ls.append(new_node)

    def pop(self) -> Node:

        length = len(self.ls)
        if length > 0:
            el = self.ls[0]
            del self.ls[0]

            if length > 1:
                self.ls[0].next = None
        else:
            raise Exception("List is Empty")

        return el

    def clear(self):
        self.ls = []

    def pop_all(self) -> list:
        result = self.ls
        self.clear()

        return result

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
        result = ""
        count = 0
        for _ in test.ls:
            result += str(test.ls[count]) + "\n"
            count += 1

        return result


test = MyList()
test.add(1)
test.add(2)
test.add(3)
test.add(4)
test.add(5)

print(test)

x = test.pop()
print(x)

print(test)
