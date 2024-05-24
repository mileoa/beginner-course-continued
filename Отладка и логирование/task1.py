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
        return self.__x

    def Get_y(self):
        return self.__y

    def Get_temperature(self):
        return self.__temperature

    def Get_noise(self):
        return self.__noise

    def Get_health(self):
        return self.__health

    def Run(self, new_speed):
        if new_speed <= 0:
            return
        self.__speed = new_speed
        if self.__speed > self.__max_speed:
            self.__speed = self.__max_speed
        self.__noise = self.__speed * 2
        self.__temperature = self.__speed * 3
        assert self.__noise >= 0
        assert self.__speed > 0 and self.__speed <= self.__max_speed
        assert self.__temperature >= 0 and self.__temperature <=1000
        
    def Stop(self):
        self.__speed = 0
        self.__noise = 0
        self.__temperature = 0
        assert self.__speed = 0
        assert self.__noise >= 0
        assert self.__temperature >= 0 and self.__temperature <=1000
        
    def Die(self):
        self.Stop()
        self.__health = 0
        assert self.__health == 0

    def Move_to(self, new_x, new_y):
        if self.__speed == 0:
            return
        self.__x = new_x
        self.__y = new_y
  
    def Increase_health(self, inc_value):
        if inc_value <= 0:
            return
        self.__health += inc_value
        if self.__health > self.__max_health:
            self.__health = self.__max_health
        assert self.__health > 0 and self.__health <= self.__max_health

    def Decrease_health(self, dec_value):
        if dec_value <= 0 or self.__health == 0:
            return
        self.__health -= dec_value
        if self.__health <= 0:
            self.Die()
        assert self.__health >= 0 and self.__health <= self.__max_health 

class Healer(Robot):
    
    def __init__(self, max_health, health, max_speed, x, y, temperature,
                 heal_power, resurrect_ablility):
        super().__init__(max_health, health, max_speed, x, y, temperature)
        self.__heal_power = heal_power # Сила лечения
        self.__resurrect_ablility = resurrect_ablility # Количество доступных воскрешений
        
    def Heal(self, target):
        if instanceof(target, type(None)) or target.Get_health() == 0:
            return
        target.Increase_health(self.__heal_power)

    def Resurrect(self, target):
        if (target.Get_health() != 0 or self.__resurrect_ablility == 0 or
                instanceof(target, type(None))):
            return
        target.Increase_health(self.__heal_power)
    
class Destroyer(Robot):

    def __init__(self, max_health, health, max_speed, x, y, temperature,
                attack_power):
        super().__init__(max_health, health, max_speed, x, y, temperature)
        self.__attack_power = attack_power # Сила атаки

    def Attack(self, target):
        if instanceof(target, type(None)):
            return
        target.Decrease_health(self.__attack_power)

    def Can_kill_one_shot(self, target):
        if instanceof(target, type(None)):
           return
        return target.Get_health() <= self.__attack_power
        

