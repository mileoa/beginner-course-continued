class Cat:

    def __init__(self, name, weight, frequency):
        self.__name = name
        self.__weight = weight
        self.__frequency = frequency

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight
    
    def get_frequency(self):
        return self.__frequency

cats = []

try:
    fi = open("cats.txt", 'rt')
    for s in fi:
        try:
            attributes = (s.rstrip()).split(" ")
            if len(attributes) != 3:
                raise Exception
            elif float(attributes[1]) <= 0:
                raise Exception
            elif int(attributes[2]) <= 0:
                raise Exception
            cats.append(Cat(attributes[0], attributes[1], attributes[2]))
        except Exception:
            print('Ошибка. Неверные параметры')
except Exception:
    print("Ошибка.")
finally:
    fi.close()

for i in range(len(cats)):
    print(cats[i].get_name(), "весит", cats[i].get_weight(), "и мурлыкает на частоте", cats[i].get_frequency())