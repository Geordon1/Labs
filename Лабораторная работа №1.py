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

if __name__ == "__main__":
    doctest.testmod()