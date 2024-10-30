from classes.product import Product


class Order:
    """
    Класс Order
    Этот класс представляет заказ в интернет-магазине.

    Атрибут класса _total_orders:
        Счетчик всех созданных заказов.
    Атрибут класса _total_amount:
        Сумма всех созданных заказов.
    """
    _total_orders = 0
    _total_amount = 0

    def __init__(self, products: list[Product]):
        self.products = products
        Order._total_orders += 1
        Order._total_amount += self.total_price()

    def total_price(self):
        """
        Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
        :return: Общая стоимость
        """
        return sum(product.price for product in self.products)

    @classmethod
    def total_orders(cls):
        """
        Возвращает общее количество созданных заказов.
        :return: Общее количество
        """
        return cls._total_orders

    @classmethod
    def total_amount(cls):
        """
        Возвращает общую стоимость всех товаров в заказе.
        :return: Общая стоимость
        """
        return cls._total_amount


    def __str__(self):
        product_details = ", ".join(str(product) for product in self.products)
        return f"Заказ (Продукты = [{product_details}], Общая цена = {self.total_price()})"