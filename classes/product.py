class Product:
    """
    Класс Product
    Этот класс представляет товар в интернет-магазине.
    """

    def __init__(self, name: str, price: float):
        """
        Конструктор инициализирует объект Product
        :param name: название товара
        :param price: цена товара
        """
        if not name:
            raise ValueError("Название товара не может быть пустым.")
        if price <= 0:
            raise ValueError("Цена товара не может быть отрицательной.")
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        else:
            return False

    def __gt__(self, other):
        return not (self < other)

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"

    def __repr__(self):
        return f"Product ({self.name!r}, {self.price!r})"