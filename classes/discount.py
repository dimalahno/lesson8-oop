class Discount:
    """
    Класс Discount
    Этот класс определяет тип скидки и ее процент.
    """

    def __init__(self, description: str, discount_percent: float):
        """
        Конструктор инициализирует объект Discount
        :param description: тип скидки
        :param discount_percent: размер скидки
        """
        if not description:
            raise ValueError("Название скидки не может быть пустым.")
        if discount_percent <= 0:
            raise ValueError("Размер скидки не может быть отрицательной.")
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
        # Проверка на валидность цены.
        if price <= 0:
            print("Ошибка: неверно указана цена.")

        # Проверка на валидность скидки.
        if discount and isinstance(discount, Discount):
            return price * (1 - discount.discount_percent / 100)
        else:
            print("Ошибка: передана невалидный тип скидки.")


    def __str__(self):
        return f"Скидка (Вид={self.description}, Размер={self.discount_percent}%)"


    def __repr__(self):
        return f"Discount ({self.description!r}, {self.discount_percent!r})"