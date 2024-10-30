class Discount:
    """
    Класс Discount
    Этот класс определяет тип скидки и ее процент.
    """

    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price: float, discount: 'Discount') -> float:
        """
        Вычисляет цену товара со скидкой
        :param price: цена товара
        :param discount: скидка
        :return: цена товара с учётом скидки
        """
        return price * (1 - discount.discount_percent / 100)

    def __str__(self):
        return f"Скидка (Вид={self.description}, Размер={self.discount_percent}%)"

    def __repr__(self):
        return f"Discount ({self.description!r}, {self.discount_percent!r})"