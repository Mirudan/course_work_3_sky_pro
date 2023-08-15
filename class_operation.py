from datetime import datetime


class Operation:
    def __init__(self, date, description, to_op, amount, currency, from_op=None):
        """
        инициализация класса
        :param date: дата перевода
        :param description: описание перевода
        :param to_op: куда
        :param amount: сумма перевода
        :param currency: валюта
        :param from_op: откуда
        """
        self.from_op = from_op
        self.currency = currency
        self.amount = amount
        self.to_op = to_op
        self.description = description
        self.date = date

    def __repr__(self):
        """
        Вывод полей класса
        :return: поля класса
        """
        return f'Operation: дата перевода - {self.date}\n' \
               f'описание перевода - {self.description}\n' \
               f'откуда - {self.from_op}\n' \
               f'куда - {self.to_op}\n' \
               f'сумма перевода - {self.amount}\n' \
               f'валюта - {self.currency}\n'

    def formate_date(self):
        """
        Форматирует дату в понятный вид
        :return: дату в удобном формате
        """
        old_date = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        new_date = old_date.strftime('%d.%m.%Y')
        return new_date
