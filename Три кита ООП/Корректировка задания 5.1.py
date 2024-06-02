def pow2(x):
    return x * x

class CommonEntity:

    def __init__(self):
        self._installed_upgrade = None

    def install_upgrade(self, improvement_characteristics):
        if self._installed_upgrade is not None:
            self.remove_upgrade()
        self._installed_upgrade = improvement_characteristics

    def remove_upgrade(self):
        self._installed_upgrade = None


class Ship(CommonEntity):

    def __init__(self, max_health, health, max_capacity,
                 weapon_list, weapon_max_amount, x, y,
                 installed_upgrade):
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

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_health(self):
        return self.__health

    def get_weapon(self, slot):
        if slot >= len(self.__weapon_list):
            return
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
        return (pow2(target.get_x() - shooter.get_x()) +
                pow2(target.get_y() - shooter.get_y())) <= pow2(self.__attack_radius)

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


# Создание улучшения оружия для игрока и его установка
player_upgrade = {"attack_damage": 100, "attack_radius": 100}

# Создание оружия игрока
player_weapon_1 = Weapon(100, 100, 100, 100, 100, player_upgrade)
print("Оружие игрока имеет силу атаки", player_weapon_1.get_attack_damage(),
       "и радиус атаки", player_weapon_1.get_attack_radius())

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
print("Здоровье игрока осталось прежним: ", player_ship.get_health())

# Игрок приблежается к врагу и пытается выстрелить
player_ship.fly_to(1020, 1020)
print("Игрок подлетел к противнику.")
print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.get_health())
print("Также сломалось оружие противника. Оно теперь имеет",
        enemy_ship.get_weapon(0).get_health(), "здоровья")

# Противник чинится
print("Противник пытается починиться.")
enemy_ship.repair(100)
print("Теперь здоровье противника", enemy_ship.get_health())

# Противник снимает сломанное оружие
enemy_ship.remove_weapon(0)

# Игрок снимает улучшение с оружия и стреляет в противника 3 раза
print("Игрок снимает улучшение с оружия.")
player_ship.get_weapon(0).remove_upgrade()
print("Оружие игрока после снятия улучшения имеет силу атаки",
        player_weapon_1.get_attack_damage(), "и радиус атаки",
        player_weapon_1.get_attack_radius())

print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.get_health())
print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.get_health())
print("Игрок попытался выстрелить.")
print("Урон равен", player_ship.give_damage(enemy_ship))
enemy_ship.take_damage(player_ship.give_damage(enemy_ship))
print("Здоровье противника уменьшилось до", enemy_ship.get_health())
