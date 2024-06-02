# Логи
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='task1.log', level=logging.INFO,
                    format="[%(asctime)s]%(levelname)s - %(funcName)s%(message)s")

class Robot:

    def __init__(self, max_health, health, max_speed, x, y, temperature):
        self.__max_health = max_health # Максимальное здоровье
        self.__health = health # Здоровье
        self.__max_speed = max_speed # Максимальная скорость робота
        self.__speed = 0 # Скорость робота
        self.__noise = 0 # текущий шум робота
        self.__temperature = temperature
        self.__x = x # Положение в пространстве по оси x
        self.__y = y # Положение в пространстве по оси y

    def get_x(self):
        logger.info('() Вызываем метод. Вернем значение %s', self.__x)
        return self.__x

    def get_y(self):
        logger.info('() Вызываем метод. Вернем значение %s', self.__y)
        return self.__y

    def get_temperature(self):
        logger.info('() Вызываем метод. Вернем значение %s', self.__temperature)
        return self.__temperature

    def get_noise(self):
        logger.info('() Вызываем метод. Вернем значение %s', self.__noise)
        return self.__noise

    def get_health(self):
        logger.info('() Вызываем метод. Вернем значение %s', self.__health)
        return self.__health

    def set_noise(self, value):
        logger.info('(%s) Вызываем метод.', value)
        if value < 0:
            logger.warning('(%s) Значение параметра меньше 0. Метод будет прерван.',
                            value)
            return
        self.__noise = value
        logger.info('(%s) Уровень шума установлен %s', value, self.__noise)
        logger.info('(%s) Метод завершен.', value)

    def set_temperature(self, value):
        logger.info('(%s) Вызываем метод.',value)
        if value < 0 or self.__temperature > 1000:
            logger.warning('(%s) Значение параметра вне допустимого диапазона. Метод будет прерван.',
                            value)
            return
        self.__temperature = value
        logger.info('(%s) Температура робота установлена %s',
                    value, self.__temperature)
        logger.info('(%s) Метод завершен.', value)

    def set_speed(self, value):
        logger.info('(%s) Вызываем метод.', value)
        if value < 0:
            logger.warning('(%s) Параметр не может быть < 0. Метод будет прерван.',
                            value)
            return
        self.__speed = value 
        if self.__speed > self.__max_speed:
            self.__speed = self.__max_speed
        logger.info('(%s) Скорость робота установлена %s',
                     value, self.__speed)
        logger.info('(%s) Метод завершен.', value)

    def run(self, speed):
        logger.info('(%s) Вызываем метод.', speed)
        self.set_speed(speed)
        self.set_noise(self.__speed * 2)
        self.set_temperature(self.__speed * 3)
        logger.info('(%s) Метод завершен.', speed)

    def stop(self):
        logger.info('() Вызываем метод.')
        self.set_speed(0)
        self.set_noise(0)
        self.set_temperature(0)
        logger.info('() Метод завершен.')
        
    def die(self):
        logger.info('() Вызываем метод.')
        self.stop()
        self.__health = 0
        logger.info('() Метод завершен.')

    def move_to(self, new_x, new_y):
        logger.info('(%s, %s) Вызываем метод.',
                    new_x, new_y)
        if self.__speed == 0:
            logger.warning('(%s, %s) Атрибут робота speed == 0. Метод будет прерван.',
                           new_x, new_y)
            return
        elif new_x > 1000 or new_x < -1000 or new_y > 1000 or new_y < -1000:
            logger.warning('(%s, %s) Параметры не входят в допустимый диапазон. Метод будет прерван.',
                           new_x, new_y)
            return
        self.__x = new_x
        self.__y = new_y
        logger.info('(%s, %s) Координаты x, y уставнолены: %s, %s',
                    new_x, new_y, self.__x, self.__y)
        logger.info('(%s, %s) Метод завершен.',
                    new_x, new_y)

    def increase_health(self, inc_value):
        logger.info('(%s) Вызываем метод.', inc_value)
        logger.info('(%s) Начальное значение атрибута health: %s',
                    inc_value, self.__health)
        if inc_value < 0:
            logger.info('(%s), Значение параметра < 0. Метод будет прерван.',
                        inc_value)
            return
        self.__health += inc_value
        if self.__health > self.__max_health:
            self.__health = self.__max_health
        assert self.__health >= 0
        logger.info('(%s) Атрибут health установлен %s',
                    inc_value, self.__health)
        logger.info('(%s) Метод завершен.', inc_value)

    def decrease_health(self, dec_value):
        logger.info('(%s) Вызываем метод.', dec_value)
        logger.info('(%s) Начальное значение атрибута health: %s',
                    dec_value, self.__health)
        if dec_value < 0 or self.__health == 0:
            logger.warn('(%s) Параметр < 0 или атрибут health цели равен 0. Метод будет прерван.',
                        dec_value)
            return
        self.__health -= dec_value
        if self.__health <= 0:
            self.die()
        assert self.__health >= 0
        logger.info('(%s) Значение атрибута health установлено %s',
                    dec_value, self.__health)
        logger.info('(%s) Метод завершен.', dec_value)

class Healer(Robot):

    def __init__(self, max_health, health, max_speed, x, y, temperature,
                 heal_power, resurrect_ablility):
        super().__init__(max_health, health, max_speed, x, y, temperature)
        self.__heal_power = heal_power # Сила лечения
        self.__resurrect_ablility = resurrect_ablility # Количество доступных воскрешений

    def heal(self, target):
        logger.info('(%s) Вызываем метод', target)
        if isinstance(target, type(None)) or target.get_health() == 0:
            logger.warning('(%s) Цель не передана или атрибут health цели равен 0. Метод будет прерван.',
                           target)
            return
        target.increase_health(self.__heal_power)
        logger.info('(%s) Метод heal выполнен.', target)

    def resurrect(self, target):
        logger.info('(%s) Вызываем метод resurrect', target)
        logger.info('(%s) Значение атрибута resurrect_ablility %s',
                    target, self.__resurrect_ablility)
        if isinstance(target, type(None)):
            logger.warning('(%s)Цель не передана. Метод будет прерван.', target)
        elif self.__resurrect_ablility == 0: 
            logger.warning('(%s) Атрибут resurrect_ablility равен 0. Метод будет прерван.',
                           target)
            return
        elif target.get_health() != 0:
            logger.warning('(%s) Здоровье цели не равно 0. Метод будет прерван.',
                           target)
            return
        target.increase_health(self.__heal_power)
        self.__resurrect_ablility -= 1
        logger.info('(%s) Атрибут resurrect_ablility установлен %s',
                    target, self.__resurrect_ablility)
        logger.info('(%s) Метод завершен.', target)

class Destroyer(Robot):

    def __init__(self, max_health, health, max_speed, x, y, temperature,
                attack_power):
        super().__init__(max_health, health, max_speed, x, y, temperature)
        self.__attack_power = attack_power # Сила атаки

    def attack(self, target):
        logger.info('(%s) Вызываем метод.', target)
        if isinstance(target, type(None)):
            logger.warning('(%s) Цель не передана. Метод будет прерван.', target)
            return
        target.decrease_health(self.__attack_power)
        logger.info('(%s) Метод завершен.', target)

    def can_kill_one_shot(self, target):
        logger.info('(%s) Вызываем метод.', target)
        logger.info('(%s) Атрибут attack_power атакующего %s',
                    target, self.__attack_power)
        if isinstance(target, type(None)):
            logger.warning('(%s) Цель не передана. Метод будет прерван.',
                           target)
            return
        result = target.get_health() <= self.__attack_power
        logger.info('(%s) Результат выполнения метода %s', target, result)
        logger.info('(%s) Метод завершен.', target)
        return result

robot_healer = Healer(100, 100, 100, 0, 0, 100, 50, 1)
robot_destroyer = Destroyer(100, 100, 100, 0, 10, 200, 50)

robot_destroyer_enemy = Destroyer(100, 100, 100, 0, 10, 200, 50)

robot_destroyer.attack(robot_destroyer_enemy)
robot_destroyer.can_kill_one_shot(robot_destroyer_enemy)

robot_healer.run(100)
robot_healer.move_to(1001, 101)
robot_healer.move_to(101, 101)

robot_destroyer_enemy.attack(robot_destroyer)
robot_destroyer_enemy.attack(robot_destroyer)

robot_healer.resurrect(robot_destroyer)
robot_healer.heal(robot_destroyer)


# Ассерты
