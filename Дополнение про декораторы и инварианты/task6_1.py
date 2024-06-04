from typing import Dict, List

class CommonEntity:

    def __init__(self) -> None:
        self._installed_upgrade: Dict[str, int]|None = None

    def install_upgrade(self, improvement_characteristics: Dict[str, int]) -> None:
        if self._installed_upgrade is not None:
            self.remove_upgrade()
        self._installed_upgrade = improvement_characteristics

    def remove_upgrade(self) -> None:
        self._installed_upgrade = None


class Ship(CommonEntity):

    def __init__(self, max_health: int, health: int, max_capacity: int,
                 weapon_list: List[Weapon]|None, weapon_max_amount: int, x: int, y: int,
                 installed_upgrade: Dict[str, int]|None):
        super().__init__()
        self.__max_health = max_health # Максимальное здоровье
        self.__health = health # Текущее здоровье

        self.__weapon_max_amount = weapon_max_amount # Макисмальное кол-во оружия
        self.__max_capacity = max_capacity # Вместительность корабля
        self.__used_capacity = 0 # Использовано вместительности
        self.__weapon_list = [] # Список установленного оружия
        for i in weapon_list:
            self.install_weapon(i)

        self.__x = x # Положение в пространстве по оси x
        self.__y = y # Положение в пространстве по оси y

        self.install_upgrade(installed_upgrade)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def health(self):
        return self.__health

    @property
    def weapon(self, slot):
        if slot >= len(self.__weapon_list) or slot < 0:
            return None
        return self.__weapon_list[slot]

    def fly_to(self, x, y):
        self.__x = x
        self.__y = y

    def repair(self, repair_value):
        if self.__health + repair_value >= self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += repair_value

    def take_damage(self, damage_value):
        if damage_value >= self.__health:
            self.die()
        else:
            self.__health -= damage_value
            for i in self.__weapon_list:
                i.take_damage(damage_value)

    def give_damage(self, target):
        total_damage = 0
        for i in self.__weapon_list:
            if (i.is_target_in_radius(self, target) and
                    i.get_health() != 0):
                total_damage += i.get_attack_damage()
        return total_damage

    def install_weapon(self, new_weapon):
        if (self.__weapon_max_amount == len(self.__weapon_list)
                or self.__used_capacity + new_weapon.get_weight() > self.__max_capacity):
            return
        self.__weapon_list.append(new_weapon)
        self.__used_capacity += new_weapon.get_weight()

    def remove_weapon(self, slot):
        if slot >= len(self.__weapon_list) or slot < 0:
            return
        self.__used_capacity -= self.__weapon_list[slot].get_weight()
        self.__weapon_list.pop(slot)

    def die(self):
        self.__health = 0
        for i in self.__weapon_list:
            i.make_broken()

    def install_upgrade(self, improvement_characteristics):
        if improvement_characteristics is None:
            return
        if self._installed_upgrade is not None:
            self.remove_upgrade()
        for key, value in improvement_characteristics.items():
            if key == "max_health":
                self.__max_health += value
            elif key == "max_capacity":
                self.__max_capacity += value
        self._installed_upgrade = improvement_characteristics

    def remove_upgrade(self):
        if self._installed_upgrade is None:
            return
        for key, value in self._installed_upgrade.items():
            if key == "max_health":
                self.__max_health -= value
            elif key == "max_capacity":
                self.__max_capacity -= value
        self._installed_upgrade = None


class Weapon(CommonEntity):

    def __init__(self, max_health, health, attack_damage,
                 attack_radius, weight, installed_upgrade):
        super().__init__()
        self.__max_health = max_health # Макс. здоровье
        self.__health = health # Текущее здоровье
        self.__attack_damage = attack_damage # Урон оружия
        self.__attack_radius = attack_radius # Радиус атаки
        self.__weight = weight # Вес оружия
        self.install_upgrade(installed_upgrade)

    def get_attack_damage(self):
        return self.__attack_damage

    def get_attack_radius(self):
        return self.__attack_radius

    def get_weight(self):
        return self.__weight

    def get_health(self):
        return self.__health

    def take_damage(self, damage_value):
        damage_value_for_weapon = damage_value // 100 + 1 # Урон по оружию
        if damage_value_for_weapon >= self.__health:
            self.make_broken()
        else:
            self.__health -= damage_value_for_weapon

    def repair(self, repair_value):
        if self.__health + repair_value >= self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += repair_value

    def make_broken(self):
        self.__health = 0

    def is_target_in_radius(self, shooter, target):
        return ((target.x() - shooter.x())**2 +
                target.y() - shooter.y())**2 <= self.__attack_radius**2

    def install_upgrade(self, improvement_characteristics):
        if improvement_characteristics is None:
            return
        if self._installed_upgrade is not None:
            self.remove_upgrade()
        for key, value in improvement_characteristics.items():
            if key == "max_health":
                self.__max_health += value
            elif key == "attack_damage":
                self.__attack_damage += value
            elif key == "attack_radius":
                self.__attack_radius += value
        self._installed_upgrade = improvement_characteristics

    def remove_upgrade(self):
        if self._installed_upgrade is None:
            return
        for key, value in self._installed_upgrade.items():
            if key == "max_health":
                self.__max_health -= value
            elif key == "attack_damage":
                self.__attack_damage -= value
            elif key == "attack_radius":
                self.__attack_radius -= value
        self._installed_upgrade = None
