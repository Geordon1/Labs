money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0

while spend < money_capital + salary:
    month += 1
    spend += spend * increase
    money_capital += salary
    money_capital -= spend



print("Количество месяцев, которое можно протянуть без долгов:", month)
