from classes.order import Order


class Customer:
    """
    Класс Customer
    Этот класс представляет клиента в интернет-магазине
    """

    def __init__(self, name: str):
        """
        Конструктор принимает имя клиента(name) список заказов (orders)
        и инициализирует объект Customer.
        :param name: имя клиента
        """
        self.name = name
        self.orders = []

    def add_order(self, order: Order):
        """
        Добавляет заказ клиенту.
        :param order: Заказ
        :return:
        """
        # Проверка на валидность заказа.
        if order and isinstance(order, Order):
            self.orders.append(order)
        else:
            print("Ошибка: передан невалидный заказ.")

    def __str__(self):
        order_details = ", ".join(str(order) for order in self.orders)
        return f"Клиент (Имя = {self.name}, Заказы = [{order_details}])"

    def __repr__(self):
        return f"Customer ({self.name!r}, {self.orders!r})"
