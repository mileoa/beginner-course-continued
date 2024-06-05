from functools import wraps

def invariant(predicate):
    def invariant_decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            assert predicate(self), f"Invariant condition failed {method.__name__}"
            return result
        return wrapper
    return invariant_decorator

class Sensor:

    def __init__(self, radius, error, x, y, noise, temperature,
                low_measurement_limit, up_measurement_limit):
        self.__radius = radius # Радиус работы дачтика
        self._error = error # Погрешность датчика в процентах
        self.__noise = noise # Шум от датчика
        self.__temperature = temperature # Температура датчика

        # Нижняя и верхняя граница диапазона измерения
        self.__low_measurement_limit = low_measurement_limit
        self.__up_measurement_limit = up_measurement_limit

        self.__x = x # Положение в пространстве по оси x
        self.__y = y # Положение в пространстве по оси y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def temperature(self):
        return self.__temperature

    @property
    def noise(self):
        return self.__noise

    def Move(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y

    @invariant(lambda self: self._error >= 0)
    def Tune(self):
        self._error -= int(self._error * 0.5)

    def Is_target_in_radius(self, target):
        return ((target.x - self.__x)**2 +
                (target.y - self.__y)**2
                ) <= self.__radius**2

    def Is_in_measurement_range(self, value):
        return (value <= self.__up_measurement_limit and
                value >= self.__low_measurement_limit)

check = Sensor(100, -1, 1, 1, 1, 1, 1, 2)
check.Tune()