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
                 weapon_list: List['Weapon'], weapon_max_amount: int, x: int, y: int,
                 installed_upgrade: Dict[str, int]|None):
        super().__init__()
        self.__max_health = max_health # Максимальное здоровье
        self.__health = health # Текущее здоровье

        self.__weapon_max_amount = weapon_max_amount # Макисмальное кол-во оружия
        self.__max_capacity = max_capacity # Вместительность корабля
        self.__used_capacity = 0 # Использовано вместительности
        self.__weapon_list: List[Weapon] = [] # Список установленного оружия
        for i in weapon_list:
            self.install_weapon(i)

        self.__x = x # Положение в пространстве по оси x
        self.__y = y # Положение в пространстве по оси y

        self.install_upgrade(installed_upgrade)

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def health(self) -> int:
        return self.__health

    def get_weapon(self, slot: int) -> 'Weapon | None':
        if slot >= len(self.__weapon_list) or slot < 0:
            return None
        return self.__weapon_list[slot]

    def fly_to(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def repair(self, repair_value: int) -> None:
        if self.__health + repair_value >= self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += repair_value

    def take_damage(self, damage_value: int) -> None:
        if damage_value >= self.__health:
            self.die()
        else:
            self.__health -= damage_value
            for i in self.__weapon_list:
                i.take_damage(damage_value)

    def give_damage(self, target: 'Ship') -> int:
        total_damage: int = 0
        for i in self.__weapon_list:
            if (i.is_target_in_radius(self, target) and
                    i.health!= 0):
                total_damage += i.attack_damage
        return total_damage

    def install_weapon(self, new_weapon: 'Weapon') -> None:
        if (self.__weapon_max_amount == len(self.__weapon_list)
                or self.__used_capacity + new_weapon.weight > self.__max_capacity):
            return None
        self.__weapon_list.append(new_weapon)
        self.__used_capacity += new_weapon.weight

    def remove_weapon(self, slot: int) -> None:
        if slot >= len(self.__weapon_list) or slot < 0:
            return None
        self.__used_capacity -= self.__weapon_list[slot].weight
        self.__weapon_list.pop(slot)

    def die(self) -> None:
        self.__health = 0
        for i in self.__weapon_list:
            i.make_broken()

    def install_upgrade(self, improvement_characteristics: Dict[str, int]|None) -> None:
        if improvement_characteristics is None:
            return None
        if self._installed_upgrade is not None:
            self.remove_upgrade()
        for key, value in improvement_characteristics.items():
            if key == "max_health":
                self.__max_health += value
            elif key == "max_capacity":
                self.__max_capacity += value
        self._installed_upgrade = improvement_characteristics

    def remove_upgrade(self) -> None:
        if self._installed_upgrade is None:
            return None
        for key, value in self._installed_upgrade.items():
            if key == "max_health":
                self.__max_health -= value
            elif key == "max_capacity":
                self.__max_capacity -= value
        self._installed_upgrade = None


class Weapon(CommonEntity):

    def __init__(self, max_health: int, health: int, attack_damage: int,
                 attack_radius: int, weight: int, installed_upgrade: Dict[str, int]|None):
        super().__init__()
        self.__max_health = max_health # Макс. здоровье
        self.__health = health # Текущее здоровье
        self.__attack_damage = attack_damage # Урон оружия
        self.__attack_radius = attack_radius # Радиус атаки
        self.__weight = weight # Вес оружия
        self.install_upgrade(installed_upgrade)

    @property
    def attack_damage(self) -> int:
        return self.__attack_damage

    @property
    def attack_radius(self) -> int:
        return self.__attack_radius

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, damage_value: int) -> None:
        damage_value_for_weapon: int = damage_value // 100 + 1 # Урон по оружию
        if damage_value_for_weapon >= self.__health:
            self.make_broken()
        else:
            self.__health -= damage_value_for_weapon

    def repair(self, repair_value: int) -> None:
        if self.__health + repair_value >= self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += repair_value

    def make_broken(self) -> None:
        self.__health = 0

    def is_target_in_radius(self, shooter: Ship, target: Ship) -> bool:
        return ((target.x - shooter.x)**2 +
                (target.y - shooter.y)**2) <= self.__attack_radius**2

    def install_upgrade(self, improvement_characteristics: Dict[str, int]|None) -> None:
        if improvement_characteristics is None:
            return None
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

    def remove_upgrade(self) -> None:
        if self._installed_upgrade is None:
            return None
        for key, value in self._installed_upgrade.items():
            if key == "max_health":
                self.__max_health -= value
            elif key == "attack_damage":
                self.__attack_damage -= value
            elif key == "attack_radius":
                self.__attack_radius -= value
        self._installed_upgrade = None

# Создание улучшения оружия для игрока и его установка
player_upgrade = {"attack_damage": 100, "attack_radius": 100}

# Создание оружия игрока
player_weapon_1 = Weapon(100, 100, 100, 100, 100, player_upgrade)
print("Оружие игрока имеет силу атаки", player_weapon_1.attack_damage,
       "и радиус атаки", player_weapon_1.attack_radius)

# Создание корабля игрока
player_ship = Ship(400, 300, 1000, [player_weapon_1], 3, 100, 100, None)

# Создание оружия противника
enemy_weapon_1 = Weapon(100, 1, 200, 200, 100, None)

# Создание корабля противника
enemy_ship = Ship(400, 400, 1000, [enemy_weapon_1], 1, 1000, 1000, None)


# Противник пытается выстрелить, но находится слишком далеко
print("Противник попытался выстрелить.")
print("Урон равен", enemy_ship.give_damage(player_ship))
player_ship.take_damage(enemy_ship.give_damage(player_ship))
print("Здоровье игрока осталось прежним: ", player_ship.health)

# Игрок приблежается к врагу и пытается выстрелить
player_ship.fly_to(1020, 1020)
print("Игрок подлетел к противнику.")
print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.health)
print("Также сломалось оружие противника. Оно теперь имеет",
        enemy_ship.get_weapon(0).health, "здоровья")

# Противник чинится
print("Противник пытается починиться.")
enemy_ship.repair(100)
print("Теперь здоровье противника", enemy_ship.health)

# Противник снимает сломанное оружие
enemy_ship.remove_weapon(0)

# Игрок снимает улучшение с оружия и стреляет в противника 3 раза
print("Игрок снимает улучшение с оружия.")
player_ship.get_weapon(0).remove_upgrade()
print("Оружие игрока после снятия улучшения имеет силу атаки",
        player_weapon_1.attack_damage, "и радиус атаки",
        player_weapon_1.attack_radius)

print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.health)
print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.health)
print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.health)
