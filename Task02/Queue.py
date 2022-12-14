class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.node = None

    def count(self) -> int:
        is_none = self.node
        count = 0

        while is_none is not None:
            count += 1
            is_none = is_none.next

        return count

    def add(self, node_value) -> None:
        new_node = Node(node_value)
        node = self.node

        if self.node is None:
            self.node = new_node
        else:
            while node.next:
                node = node.next
            node.next = new_node

    def pop(self) -> Node:
        if self.node is not None:
            result = self.node.value

            if self.node.next is not None:
                self.node = self.node.next
            else:
                self.node = None
        else:
            raise Exception("Queue is empty")

        return result

    def clear(self) -> None:
        self.node = None

    def pop_all(self) -> list:
        result = list()
        node = self.node

        while node is not None:
            result.append(node.value)
            node = node.next

        self.node = None

        return result

    def __str__(self):
        result = ""
        node = self.node
        while node is not None:
            result += str(node.value) + "; "
            node = node.next

        return result

    def __len__(self):
        return self.count()

    def __getitem__(self, key) -> Node:
        try:

            node = self.node

            for _ in range(key):
                node = node.next

            if node is not None:
                return node.value
            else:
                raise AttributeError("Incorrect key")
        except AttributeError as e:
            print(e)

    def __setitem__(self, key, value) -> None:
        node = self.node
        for _ in range(key):
            node = node.next

        node.value = value

    def __contains__(self, item) -> bool:
        node = self.node
        while node is not None:
            if node.value == item:
                return True

            node = node.next

        return False

    def __int__(self):
        return self

    def __next__(self):
        try:
            node = self.node
            if node is not None:
                result = node.value
                self.node = self.node.next
                return result
            else:
                raise StopIteration("Queue is empty")
        except StopIteration as e:
            print(e)


xx = Queue()

xx.add(1)
xx.add(2)
xx.add(3)
print(xx)

retry = xx.pop()
print(xx)

xx.add(12)
xx.add(23)

print(xx)
print(xx.count())

# x = xx.pop_all()
# print(x)
print(xx)
xx[2] = 123121321
print(xx)

print(xx[1])

if 2 in xx:
    print("aa")

if 12312 in xx:
    print("asiojd")

xxx = iter(xx)

print(next(xxx))
print(next(xxx))
print(next(xxx))
print(next(xxx))
print(next(xxx))




