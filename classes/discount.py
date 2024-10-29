class Discount:

    def __init__(self, description: str, discount_percent: int):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price: float, discount: 'Discount') -> float:
        """

        :param price:
        :param discount:
        :return:
        """
        return price * (1 - discount.discount_percent / 100)

    def __str__(self):
        return f"Скидка (Вид={self.description}, Размер={self.discount_percent}%)"

    def __repr__(self):
        return f"Discount ({self.description!r}, {self.discount_percent!r})"