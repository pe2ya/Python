class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance



a = Singleton()
b = Singleton()

print(a is b) #Musi vypsat true

a.moje_nova_promenna_pro_a = "Test"
print(a.moje_nova_promenna_pro_a) #Musi vypsat test
print(b.moje_nova_promenna_pro_a) #Musi vypsat take test


