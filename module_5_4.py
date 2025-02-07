class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):
        return f'Название : {self.name}, количество этажей : {self.number_of_floors}'
    def __eq__(self, other : int):
        return self.number_of_floors == other
    def __lt__(self, other : int):
        return self.number_of_floors < other
    def __le__(self, other : int):
        return self.number_of_floors <= other
    def __gt__(self, other : int):
        return self.number_of_floors > other
    def __ge__(self, other : int):
        return self.number_of_floors >= other
    def __ne__(self, other : int):
        return self.number_of_floors != other
    def __add__(self, value):
        self.number_of_floors= self.number_of_floors + value
        return self.number_of_floors
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)


