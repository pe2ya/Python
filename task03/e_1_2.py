

def append_jecna_postfix(string : str):
    return string + "@spsejecna.cz"

def append_seznam_postfix(string : str):
    return string + "@seznam.cz"

def create_email(func, string: str):
    return func(string)


appender_postfix = append_jecna_postfix
x = create_email(appender_postfix, "novak")
#ma vratit novak@spsejecna.cz
appender_postfix = append_seznam_postfix
y = create_email(appender_postfix, "novak")
#ma vratit novak@seznam.cz

print(x, y)