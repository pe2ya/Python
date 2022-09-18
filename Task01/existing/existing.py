list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]

tpl = tuple(list_list)

st = set(list_list)

string = str(list_list)

d2 = {1: "one", 2: "two"}

if 2 in list_list:
    print("list is yeap")

if 2 in tpl:
    print("tpl is yeap")

if 2 in st:
    print("st is yeap")

if "2" in string:
    print("string yeap")

if 2 in d2:
    print("d2 is yeap")
