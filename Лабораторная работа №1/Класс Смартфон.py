import doctest

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