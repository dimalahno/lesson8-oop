from classes.customer import Customer
from classes.discount import Discount
from classes.order import Order
from classes.product import Product

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Keyboard", 45)

print(product1)
print(product2)
print(product3)

# Создаем скидки
discount1 = Discount("Holiday Discount", 20)
discount2 = Discount("Promo-code Discount", 10)

# Применяем скидку к товару
discounted_price1 = discount1.apply_discount(product1.price, discount1)
print(f"Цена {product1.name} после скидки Holiday Discount: {discounted_price1}")

discounted_price2 = discount2.apply_discount(product1.price, discount2)
print(f"Цена {product2.name} после скидки Promo-code Discount: {discounted_price2}")

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product3])
order3 = Order([product2])
order4 = Order([product3])
# Выводим информацию о заказах
print(order1)  # Вывод: Заказ (Общая цена = 1000)
print(order2)  # Вывод: Заказ (Общая цена = 1500)

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")
# Выводим общую сумму заказов
print(f"Всего сумма заказов: {Order.total_amount()}")



# Создаем клиента и добавляем заказы
customer1 = Customer("Дима")
# Проверка передачи невалидного заказ. -> Ошибка.
customer1.add_order("Заказ")
customer1.add_order(order1)
customer1.add_order(order2)

customer2 = Customer("Полина")
customer2.add_order(order3)
customer2.add_order(order4)

print(customer1)
print(customer2)

# Сравнение товаров по цене
print(product1 == product2)
print(product3 < product2)