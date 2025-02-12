class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f'"{self.name}" by {self.author}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r})'

    def name(self):
        return self._name

    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f'{super().__str__()}, {self.pages} pages'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})'

    def pages(self):
        return self._pages

    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Страницы должны быть положительным целым числом.")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f'{super().__str__()}, {self.duration:.2f} hours'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})'

    def duration(self):
        return self._duration

    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом.")
        self._duration = float(value)
