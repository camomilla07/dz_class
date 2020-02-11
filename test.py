class Animals:
    '''Животные'''
    interaction = "не кормить"
    weight = 0  # кг
    weight_max = 0  # кг
    voice = "!"
    emp_count = 0
    weight_sum = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight += weight
        Animals.emp_count += 1
        Animals.weight_sum += weight
        if self.weight > Animals.weight_max:
            Animals.weight_max = self.weight
            Animals.name_max_weight = self.name
        print(f'{self.name}, {self.weight} кг')

    def feed(self):
        self.interaction = "покормить"
        return self.interaction


class Poultry:
    eggs = "none"

    def collect_eggs(self):
        self.eggs = "собрать яйца"
        return self.eggs


class Gouse(Poultry, Animals):
    '''Гусь'''

    def speak(self, voice="Га-га-га"):
        print("Гусь-", voice)


class Duck(Poultry, Animals):
    '''Утка'''

    def speak(self, voice="Га-га"):
        print("Утка-", voice)


class Chicken(Poultry, Animals):
    '''Курица'''

    def speak(self, voice="Ко-Ко-ко"):
        print("Курица-", voice)


class Sheep(Animals):
    '''Овца'''
    wool = "not"

    def speak(self, voice="Бее"):
        print("Овца-", voice)

    def shearning(self):
        self.wool = "Постричь овцу"


class MilkAnimals:
    milk = "none"

    def milk(self):
        self.milk = "Подоить"
        return self.milk


class Cow(MilkAnimals, Animals):
    '''Корова'''

    def speak(self, voice="Муу"):
        print("Корова-", voice)


class Goat(MilkAnimals, Animals):
    '''Коза'''

    def speak(self, voice="Мее"):
        print("Коза-", voice)


gouse0 = Gouse("Серый ", 6)
gouse1 = Gouse("Белый", 7)
cow0 = Cow("Манька", 500)
sheep0 = Sheep("Барашек", 90)
sheep1 = Sheep("Кудрявый", 85)
chicken0 = Chicken("Ко-ко", 1)
chicken1 = Chicken("Кукареку", 2)
goat0 = Goat("Рога", 6)
goat1 = Goat("Копыта", 7)
duck0 = Duck("Кряква", 3)

gouse0.speak()
cow0.speak()
sheep0.speak()
chicken0.speak()
goat0.speak()
duck0.speak()

print("Всего животных: %d" % Animals.emp_count)
print("Вес всех животных: %d" % Animals.weight_sum, "кг")
print(f'Самое тяжелое животное - {Animals.name_max_weight},{Animals.weight_max} кг')






