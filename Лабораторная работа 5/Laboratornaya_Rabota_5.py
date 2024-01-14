import doctest

class Album:
    def __init__(self, pages: int, photos: int, text: str):
        """
        Создание и подготовка к работе объекта "Альбом"

        :param pages: Количество страниц
        :param photos: Количество фотографий
        :param text: Написанный текст

        Примеры:
        >>> album = Album(25, 13, "I Love YOU")  # инициализация экземпляра класса
        """
        self.text = text

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(photos, int):
            raise TypeError("Количество фотографий должно быть типа int")
        if photos <= 0:
            raise ValueError("Количество фотографий должно быть положительным числом")
        self.photos = photos

    def empty_album_photo(self) -> bool:
        """
        Функция которая проверяет есть ли в альбоме фотографии

        :return: Есть ли фотографии в альбоме

        Примеры:
        >>> album = Album(25, 13, "I Love YOU")
        >>> album.empty_album_photo()
        """
        ...

    def empty_album_text(self) -> bool:
        """
        Функция которая проверяет есть ли в альбоме текст

        :return: Есть ли текст в альбоме

        Примеры:
        >>> album = Album(25, 13, "I Love YOU")
        >>> album.empty_album_text()
        """
        ...


class Calendar:
    def __init__(self, year: int):
        """
        Создание и подготовка к работе объекта "Календарь"

        :param year: Какой год в календаре

        Примеры:
        >>> calendar = Calendar(2012)  # инициализация экземпляра класса
        """

        if not isinstance(year, int):
            raise TypeError("Число года должно быть типа int")
        self.year = year

    def leap_year(self) -> bool:
        """
        Функция которая проверяет високосный год или нет

        :return: ВИсокосный год или нет

        Примеры:
        >>> calendar = Calendar(2012)
        >>> calendar.leap_year()
        """
        ...

    def holydays(self) -> int:
        """
        Функция которая проверяет сколько выходных дней в году

        :return: Количество выходных дней в году

        Примеры:
        >>> calendar = Calendar(2012)
        >>> calendar.holydays()
        """
        ...

class Circle:
    def __init__(self, radius: (int, float)):
        """
        Создание и подготовка к работе объекта "Круг"

        :param radius: Радиус круга

        Примеры:
        >>> circle = Circle(5.5)  # инициализация экземпляра класса
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if radius <=0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def perimeter(self):
        """
        Функция которая считает периметр круга

        :return: ЧИсло равное периметру круга

        Примеры:
        >>> circle = Circle(5.5)
        >>> circle.perimeter()
        """
        ...

    def square(self):
        """
        Функция которая считает площадь круга

        :return: ЧИсло равное площади круга

        Примеры:
        >>> circle = Circle(5.5)
        >>> circle.square()
        """
        ...

    def diametr(self):
        """
        Функция которая считает диаметр круга

        :return: ЧИсло равное диаметру круга

        Примеры:
        >>> circle = Circle(5.5)
        >>> circle.diametr()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации