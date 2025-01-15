import doctest

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

if __name__ == "__main__":
    doctest.testmod()