
class Plane:

    def __init__(self, appointment: str, model: str, weight: int):

        self.appointment = appointment  # Приватный атрибут для предотвращения изменения напрямую
        self.model = model
        self.weight = weight

    def start_engine(self) -> str:

    def stop_engine(self) -> str:

    def __str__(self) -> str:
        return f"{self.weight} {self.appointment} {self.model}"

    def __repr__(self) -> str:
        return f"Vehicle('{self.appointment}', '{self.model}', {self.weight})"


class Aircraft(Plane):

    def __init__(self, appointment: str, model: str, weight: int, chassis: str):
        super().__init__(appointment, model, weight)
        self.chassis = chassis

    def radio_signal(self) -> str:
        return "Принято!"

    def start_engine(self) -> str:
        return f"Самолёт {self.appointment} {self.model} готов к взлёту."

    def __str__(self) -> str:
        return f"{self.weight} {self.appointment} {self.model} ({self.chassis})"

    def __repr__(self) -> str:
        return f"Aircraft('{self.appointment}', '{self.model}', {self.weight}, '{self.chassis}')"


if __name__ == "__main__":
    # Тестовые примеры
    plane1 = Plane("Passenger", "Airbus", "30 ton")
    plane2 = Aircraft("Transport", "Boeing", "70 ton", "Wheeled")

    print(plane1)
    print(plane1.start_engine())
    print(plane1.stop_engine())

    print(plane2)
    print(plane2.start_engine())
    print(plane2.radio_signal())