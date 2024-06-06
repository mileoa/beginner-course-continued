#5.1., 5.2. и 5.3
def word_count(string: str) -> int:
    word_count: int = 0
    assert word_count >= 0, "Инвариант должени быть >= 0" #5.1. и 5.3.
    if len(string) > 0 and string[0] != ' ':
        word_count = 1
        assert word_count >= 0, "Инвариант должени быть >= 0" #5.1. и 5.3.
    for i in range(len(string)-1):
        if string[i] == ' ' and string[i+1] != ' ':
            word_count += 1
            assert word_count >= 0, "Инвариант должени быть >= 0" #5.1. и 5.3.
    assert word_count >= 0, "Результат должени быть >= 0" #5.2. и 5.3.
    return word_count


#5.3.
def dog_age_to_human(dog_age: int) -> int:
    assert dog_age >= 0 and dog_age <= 100, "Возраст собаки должен быть между 0 и 100" #5.3.
    age: int = 0

    if dog_age > 0 and dog_age <= 2:
        age = dog_age * 10.5
    elif dog_age > 2:
        age = 21 + (dog_age - 2) * 4
    assert age >= 0, "Рузультат должен быть >= 0" #5.1. и 5.3.
    return age


#5.4.
class Cube:

    def __init__(self, height: int):
        if height <= 0:
            raise Exception
        self.__height = height

    def volume(self) -> int:
        assert self.__height > 0, "Сторона куба должна быть больше 0"
        return self.__height**3

#5.5.
from typing import List
from math import sqrt
def calc_square_roots(a: int, b: int, c: int) -> List[int|float] | None:
    descriminant: int = b**2 - 4*a*c
    if descriminant < 0:
        return None
    assert descriminant >=0, "На данном этапе дискриминант не может быть отрицательным."
    return [(-b+sqrt(descriminant)) / (2*a),
            (-b-sqrt(descriminant)) / (2*a)]

#5.6.
class Weapon:

    def __init__(self, improvement_characteristics):
        self._installed_upgrade = improvement_characteristics
        self.__max_health = 100
        self.__attack_damage = 100
        self.__attack_radius = 100

    def install_upgrade(self, improvement_characteristics):
        if improvement_characteristics is None:
            return
        assert improvement_characteristics is not None, "Нельзя установить None"
        for key, value in improvement_characteristics:
            assert key in ("max_health", "attack_damage", "attack_radius"), "Тип улучшения не доступен"
            assert isinstance(value, int), "Значение улучшения должно быть Int"
        if self._installed_upgrade is not None:
            #self.remove_upgrade()
            pass
        for key, value in improvement_characteristics.items():
            if key == "max_health":
                self.__max_health += value
            elif key == "attack_damage":
                self.__attack_damage += value
            elif key == "attack_radius":
                self.__attack_radius += value
        self._installed_upgrade = improvement_characteristics

#5.7.
def is_zombie(HID):
    assert HID > 0, "id должен быть положительным"
    if HID % 5 == 0 and HID % 11 == 0:
        return False
    return True