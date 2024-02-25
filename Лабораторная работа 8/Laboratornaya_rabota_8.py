class Building:
    """Базовый класс здание."""
    HIGH_FLOOR = 3  # Переменная, высота этажа, м.
    FOUNDATION_HIGH = 1 # Переменная, толщина фундаментной плиты, м.
    PRICE_KOEF = 50000 # Переменная, цена здания за 1 м3
    """Переменные, которые имеют одинаковые значения для все хэкземпляров класса"""

    def __init__(self, floor: int, square_floor: int, construction: str):
        """
        Создание и подготовка к работе объекта "Здание"

        :param floor: Количество этажей.
        :param square_floor: Площадь этажа, м2.
        :param construction: Вид конструкции, из которой сделано здание.

        Пример:
        building = Building(12, 1500, "Metal")  # инициализация экземпляра класса
        """
        self._floor = floor
        self._square_floor = square_floor
        self._construction = construction

    def __str__(self):
        return f"Здание этажностью {self._floor}. Площадь этажа {self._square_floor} м2. Вид конструкции {self._construction}."

    def __repr__(self):
        return f"{self.__class__.__name__}(floor={self._floor!r}, square_floor={self._square_floor!r}, construction={self._construction!r})"

    """Проверка атрибута floor"""
    @property
    def floor(self) -> int:
        return self._floor

    @floor.setter
    def floor(self, new_floor: int) -> None:
        if not isinstance(new_floor, int):
            raise TypeError("Этажность должна быть типа int")
        if new_floor <= 0:
            raise ValueError("Этажность должна быть положительным числом")
        self._floor = new_floor

    """Проверка атрибута square_floor"""
    @property
    def square_floor(self) -> float:
        return self._square_floor

    @square_floor.setter
    def square_floor(self, new_square_floor: float) -> None:
        if not isinstance(new_square_floor, float):
            raise TypeError("Площадь этажа должно быть типа float")
        if new_square_floor <= 0:
            raise ValueError("Площадь этажа должна быть положительным числом")
        self.square_floor = new_square_floor

    """Проверка атрибута construction"""
    @property
    def construction(self) -> str:
        return self._construction

    @construction.setter
    def construction(self, new_construction: str) -> None:
        if not isinstance(new_construction, str):
            raise TypeError("Конструкция должно быть типа str")
        self._construction = new_construction


    def square_building(self) -> float:
        """Метод, который считает общую площадь всего здания"""
        return self.floor * self.square_floor

    def volume_building(self) -> float:
        """Метод, который считает объем всего здания"""
        return self.floor * self.square_floor * self.HIGH_FLOOR

    def volume_foundation(self) -> float:
        """Метод, который считает объем фундамента здания"""
        return self.square_floor * self.FOUNDATION_HIGH

    def price(self) -> float:
        """Метод, который считает цену здания"""
        return self.floor * self.square_floor * self.HIGH_FLOOR * self.PRICE_KOEF

class ResidentialBuilding(Building):
    """Дочерний класс жилое здание."""
    PEOPLE_APARTMENT = 4 #Переменная, количество жильцов на квартиру.
    HIGH_FLOOR = 3  # Переменная, высота этажа, м.
    FOUNDATION_HIGH = 1.2  # Переменная, толщина фундаментной плиты, м.
    PRICE_KOEF = 150000 #Переменная цена здания за 1 м3
    """Переменные, которые имеют одинаковые значения для всех экземпляров класса, 
    изменены под новые условия дочернего класса.
    Добавлена новая переменная, присущая данному дочернему классу."""

    def __init__(self, floor: int, square_floor: int, construction: str, num_apartments: int):
        """
        Создание и подготовка к работе объекта "Жилое здание"

        :param floor: Количество этажей.
        :param square_floor: Площадь этажа, м2.
        :param construction: Вид конструкции, из которой сделано здание
        :param num_apartments: Количество квартир в здании, шт.

        Пример:
        building = Building(12, 1500, "Metal", 120)  # инициализация экземпляра класса
        """
        super().__init__(floor, square_floor, construction)
        self._num_apartments = num_apartments

    def __str__(self):
        return f"Здание этажностью {self._floor}. Площадь этажа {self._square_floor} м2. Вид конструкции {self._construction}. Количество квартир {self._num_apartments}."
    def __repr__(self):
        return f"{self.__class__.__name__}(floor={self._floor!r}, square_floor={self._square_floor!r}, construction={self._construction!r}, num_apartments={self._num_apartments!r})"

    """Проверка атрибута num_apartments"""
    @property
    def num_apartments(self) -> int:
        return self._num_apartments

    @num_apartments.setter
    def num_apartments(self, new_num_apartments: int) -> None:
        if not isinstance(new_num_apartments, int):
            raise TypeError("Количество квартир должно быть типа int")
        if new_num_apartments <= 0:
            raise ValueError("Количество квартир должно быть положительным числом")
        self._num_apartments = new_num_apartments

    """Метод square_building является наследуемым методом"""

    """Метод volume_building является наследуемым методом"""

    """Метод volume_foundation является наследуемым методом"""

    def quolity_people(self) -> float:
        """Метод, который считает количество жильцов в здании
            Является новым методом"""
        return self.floor * self.num_apartments * self.PEOPLE_APARTMENT

    def price(self) -> float:
        """Метод, который считает цену здания
            Является перегруженным методом"""
        return self.floor * self.num_apartments * self.PRICE_KOEF

class IndustrialBuilding(Building):
    """Дочерний класс промышленное здание."""
    HIGH_FLOOR = 4.5  # Переменная, высота этажа, м.
    FOUNDATION_HIGH = 1.5 #Толщина фундаментной плиты.
    PRICE_KOEF = 50000  # Переменная, цена здания за 1 м3
    """Переменные, которые имеют одинаковые значения для всех экземпляров класса, 
    изменены под новые условия дочернего класса."""

    def __init__(self, floor: int, square_floor: int, construction: str, type: str):
        """
        Создание и подготовка к работе объекта "Жилое здание"

        :param floor: Количество этажей.
        :param square_floor: Площадь этажа, м2.
        :param construction: Вид конструкции, из которой сделано здание.
        :param type: Тип промышленного здания.

        Пример:
        building = Building(12, 1500, "Metal", "Sewing")  # инициализация экземпляра класса
        """
        super().__init__(floor, square_floor, construction)
        self._type = type

    def __str__(self):
        return f"Здание этажностью {self._floor}. Площадь этажа {self._square_floor} м2. Вид конструкции {self._construction}. Тип здания {self._type}."

    def __repr__(self):
        return f"{self.__class__.__name__}(floor={self._floor!r}, square_floor={self._square_floor!r}, construction={self._construction!r}, type={self._type!r})"

    """Проверка атрибута type"""
    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str) -> None:
        if not isinstance(new_type, str):
            raise TypeError("Тип пормышленного здания должно быть типа str")
        self._type = new_type

    """Метод square_building является наследуемым методом"""

    """Метод volume_foundation является наследуемым методом"""

    """Метод price является наследуемым методом"""

    def volume_building(self) -> float:
        """Метод, который считает объем всего здания с учетом дополнительного технического этажа
            Является перегруженным методом."""
        return (self.floor + 1) * self.square_floor * self.HIGH_FLOOR

building_1 = Building(12, 1500, "Metal")
building_2 = ResidentialBuilding(8, 500, "Concrete", 80)
building_3 = IndustrialBuilding(2, 3000, "Metal", "Sawmill")
