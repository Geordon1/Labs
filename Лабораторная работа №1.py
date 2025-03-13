import doctest

class Library:
    """
    Абстрактный класс, описывающий библиотеку.
    """

    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValueError("Вместимость библиотеки должна быть больше нуля.")
        self.name = name
        self.capacity = capacity

    def add_book(self, book_title: str) -> None:
        """
        Добавить книгу в библиотеку.

        Args:
            book_title (str): Название книги.

        Returns:
            None

        Пример использования:
         library.add_book("1984")
        """
        pass

    def lend_book(self, book_title: str, borrower_name: str) -> None:
        """
         Выдать книгу читателю.

        Args:
            book_title (str): Название книги.
            borrower_name (str): Имя читателя.

        Returns:
            None

        Пример использования:
         library.lend_book("1984", "Alex")
        """
        pass

    def return_book(self, book_title: str) -> None:
        """
        Принять возврат книги в библиотеку.

        Args:
            book_title (str): Название книги.

        Returns:
            None

        Пример использования:
         library.return_book("1984")
        """
        pass



class Car:
    """
    Абстрактный класс, описывающий автомобиль.
    """

    def __init__(self, brand: str, fuel_capacity: float):
        if fuel_capacity <= 0:
            raise ValueError("Ёмкость топливного бака должна быть больше нуля.")
        self.brand = brand
        self.fuel_capacity = fuel_capacity

    def start_engine(self) -> None:
        """
        Запустить двигатель автомобиля.

        Returns:
            None

        Пример использования:
         car.start_engine()
        """
        pass

    def drive(self, distance: float) -> None:
        """
        Поехать на определённое расстояние.

        Args:
            distance (float): Расстояние в километрах.

        Returns:
            None

        Пример использования:
         car.drive(50)
        """
        pass

    def refuel(self, amount: float) -> None:
        """
        Заправить автомобиль.

        Args:
            amount (float): Количество топлива для заправки.

        Returns:
            None

        Пример использования:
         car.refuel(20)
        """
        pass



class Smartphone:
    """
    Абстрактный класс, описывающий смартфон.
    """

    def __init__(self, model: str, storage_capacity: int):
        if storage_capacity <= 0:
            raise ValueError("Объём памяти должен быть больше нуля.")
        self.model = model
        self.storage_capacity = storage_capacity

    def make_call(self, phone_number: str) -> None:
        """
        Совершить звонок.

        Args:
            phone_number (str): Номер телефона для вызова.

        Returns:
            None

        Пример использования:
         smartphone.make_call("+79999999999")
        """
        pass

    def install_app(self, app_name: str) -> None:
        """
         Установить приложение.

        Args:
            app_name (str): Название приложения для установки.

        Returns:
            None

        Пример использования:
         smartphone.install_app("Telegram")
        """
        pass

    def take_photo(self) -> None:
        """
         Сделать фотографию.

        Returns:
            None

        Пример использования:
         smartphone.take_photo()
        """
        pass

if __name__ == "__main__":
    doctest.testmod()