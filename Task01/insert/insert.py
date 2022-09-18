try:
    list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22, None]

    tpl = tuple(list_list)

    st = set(list_list)

    string = str(list_list)

    d2 = {1: "one", 2: "two", 3: None, None: "None"}

    print(f"list: {list_list}")
    print("tuple: " + str(tpl))
    print(f"string: {string}")
    print(f"dictionary: {d2}")
    print(f"set: {st}")

except Exception as e:
    print(e)
else:
    print("\n\nProgram executed correctly")




