import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='task1.log', level=logging.INFO,
                    format="[%(asctime)s]%(levelname)s %(funcName)s - %(message)s")

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
    
    def Get_x(self):
        logger.info('Возвращаем значение положения x.')
        logger.info(self.__x)
        return self.__x

    def Get_y(self):
        logger.info('Возвращаем значение положения y.')
        logger.info(self.__y)
        return self.__y

    def Get_temperature(self):
        logger.info('Возвращаем значение температуры.')
        logger.info(self.__temperature)
        return self.__temperature

    def Get_noise(self):
        logger.info('Возвращаем значение уровня шума.')
        logger.info(self.__noise)
        return self.__noise

    def Get_health(self):
        logger.info('Возвращаем значение здоровья.')
        logger.info(self.__health)
        return self.__health

    def Set_noise(self, value):
        logger.info('Пытаемся изменить уровень шума робота. Новое значение:')
        logger.info(value)
        if value < 0:
            logger.warning('Значение меньше 0. Операция не будет выполнена.')
            return
        self.__noise = value
        logger.info('Уровень шума установлен. Значение:')
        logger.info(self.__noise)
        assert self.__noise >= 0
    
    def Set_temperature(self, value):
        logger.info('Пытаемся изменить температуру робота. Новое значение:')
        logger.info(value)
        if value < 0 or self.__temperature > 1000:
            logger.warning('Новое значение вне допустимого диапазона. Операция не будет выполнена.')
            return
        self.__temperature = value
        logger.info('Температура робота установлена. Значение:')
        logger.info(self.__temperature)
        assert self.__temperature >= 0 and self.__temperature <=1000

    def Set_speed(self, value):
        logger.info('Пытаемся установить новую скорость роботу. Новое значение:')
        logger.info(value)
        if value < 0:
            logger.warning('Значение скорости не может быть < 0.')
            return
        self.__speed = value 
        if self.__speed > self.__max_speed:
            self.__speed = self.__max_speed
        logger.info('Скорость робота установлена. Значение:')
        logger.info(self.__speed)
        assert self.__speed >= 0 and self.__speed <= self.__max_speed

    def Run(self, speed):
        logger.info('Пытаемся выполнить метод бега робота.')
        self.Set_speed(speed)
        self.Set_noise(self.__speed * 2)
        self.Set_temperature(self.__speed * 3)
        logger.info('Метод бега робота выполнен.')

    def Stop(self):
        logger.info('Пытаемся остановить робота.')
        self.Set_speed(0)
        self.Set_noise(0)
        self.Set_temperature(0)
        logger.info('Робот остановлен.')
        
    def Die(self):
        logger.info('Пытаемся сделать робота мертвым.')
        self.Stop()
        self.__health = 0
        logger.info('Робот мёртв.')
        assert self.__health == 0

    def Move_to(self, new_x, new_y):
        logger.info('Пытаемся переместить робота на координаты x, y:')
        logger.info(new_x)
        logger.info(new_y)
        if self.__speed == 0:
            logger.warning('Робот стоит и не может быть перемещен.')
            return
        elif new_x > 1000 or new_x < -1000 or new_y > 1000 or new_y < -1000:
            logger.warning('Робот не может быть перемещен за пределы карты.')
            return
        self.__x = new_x
        self.__y = new_y
        logger.info('Робот перемещен. Его координаты x, y:')
        logger.info(self.__x)
        logger.info(self.__y)
        assert self.__x <= 1000 and self.__x >= -1000
        assert self.__y <= 1000 and self.__y >= -1000
  
    def Increase_health(self, inc_value):
        logger.info('Пытаемся увеличить здоровье робота. Текущее значение:')
        logger.info(self.__health)
        logger.info('Значение увелечения:')
        logger.info(inc_value)
        if inc_value < 0:
            logger.info('Значение увелечения меньше 0. Операция не будет выполнена')
            return
        self.__health += inc_value
        if self.__health > self.__max_health:
            self.__health = self.__max_health
        logger.info('Здоровье робота установлено. Значение:')
        logger.info(self.__health)
        assert self.__health > 0 and self.__health <= self.__max_health

    def Decrease_health(self, dec_value):
        logger.info('Пытаемся уменьшить здоровье робота. Текущее значение:')
        logger.info(self.__health)
        logger.info('Знаечние уменьшения:')
        logger.info(dec_value)
        if dec_value < 0 or self.__health == 0:
            logger.warn('Значение изменения меньше 0 или здоровье цели равно 0. Операция не будет выполнена.')
            return
        self.__health -= dec_value
        if self.__health <= 0:
            self.Die()
        logger.info('Здоровье робота установлено. Значение:')
        logger.info(self.__health)
        assert self.__health >= 0 and self.__health <= self.__max_health 

class Healer(Robot):
    
    def __init__(self, max_health, health, max_speed, x, y, temperature,
                 heal_power, resurrect_ablility):
        super().__init__(max_health, health, max_speed, x, y, temperature)
        self.__heal_power = heal_power # Сила лечения
        self.__resurrect_ablility = resurrect_ablility # Количество доступных воскрешений
        
    def Heal(self, target):
        logger.info('Пытаемся выпонить метод лечения. Сила лечения:')
        logger.info(self.__heal_power)
        if isinstance(target, type(None)) or target.Get_health() == 0:
            logger.warning('Цель не передана или здоровье цели 0. Операция не будет выполнена.')
            return
        target.Increase_health(self.__heal_power)
        logger.info('Метод лечения выполнен.')

    def Resurrect(self, target):
        logger.info('Пытаемся выполнить метод воскрешения.')
        if isinstance(target, type(None)):
            logger.warning('Цель не передана. Операция не будет выполнена.')
        elif self.__resurrect_ablility == 0: 
            logger.warning('Способность к воскршению 0. Операция не будет выполнена.')
            return
        elif target.Get_health() != 0:
            logger.warning('Здоровье цели не равно 0. Операция не будет выполнена.')
            return
        target.Increase_health(self.__heal_power)
        logger.info('Метод воскрешения завершен.')
    
class Destroyer(Robot):

    def __init__(self, max_health, health, max_speed, x, y, temperature,
                attack_power):
        super().__init__(max_health, health, max_speed, x, y, temperature)
        self.__attack_power = attack_power # Сила атаки

    def Attack(self, target):
        logger.info('Пытаемся выполнить метод атаки цели. Сила атаки:')
        logger.info(self.__attack_power)
        if isinstance(target, type(None)):
            logger.warning('Цель не передана. Операция будет прервана.')
            return
        target.Decrease_health(self.__attack_power)
        logger.info('Метод атаки завершен.')

    def Can_kill_one_shot(self, target):
        logger.info('Пытаемся выполнить метод проверки возможности убить цель одним выстрелом.')
        logger.info('Сила атаки:')
        logger.info(self.__attack_power)
        if isinstance(target, type(None)):
            logger.warning('Цель не передана. Операция будет прервана.')
            return
        logger.info('Здоровье цели:')
        result = target.Get_health() <= self.__attack_power
        assert isinstance(result, bool)
        logger.info('Метод проверки возможности убить цель одним выстрелом завершен.')
        logger.info('Результат:')
        logger.info(result)
        return result

robot_healer = Healer(100, 100, 100, 0, 0, 100, 50, 1)
robot_destroyer = Destroyer(100, 100, 100, 0, 10, 200, 50)

robot_destroyer_enemy = Destroyer(100, 100, 100, 0, 10, 200, 50)

robot_destroyer.Attack(robot_destroyer_enemy)
robot_destroyer.Can_kill_one_shot(robot_destroyer_enemy)

robot_healer.Run(100)
robot_healer.Move_to(1001, 101)
robot_healer.Move_to(101, 101)

robot_destroyer_enemy.Attack(robot_destroyer)
robot_destroyer_enemy.Attack(robot_destroyer)

robot_healer.Resurrect(robot_destroyer)
robot_healer.Heal(robot_destroyer)