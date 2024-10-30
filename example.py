from classes.customer import Customer
from classes.discount import Discount
from classes.order import Order
from classes.product import Product

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Keyboard", 45)
product4 = Product("Mouse", 45)

print(product1)
print(product2)
print(product3)
print(product4)

# Сравнение товаров по цене
print(f"{product1.price} == {product2.price}:", product1 == product2)
print(f"{product3.price} < {product2.price}:", product3 < product2)
print(f"{product3.price} == {product4.price}:", product3 == product4)
print(f"{product1.price} > {product2.price}:", product1 > product2)

# Создаем скидки
discount1 = Discount("Holiday", 20)
discount2 = Discount("Promo-code", 10)

print(discount1)
print(discount2)

# Применяем скидку к товару
discounted_price1 = discount1.apply_discount(product1.price, discount1)
print(f"Цена {product1.name} после скидки {discount1.description}: {discounted_price1}")

discounted_price2 = discount2.apply_discount(product1.price, discount2)
print(f"Цена {product2.name} после скидки{discount2.description}: {discounted_price2}")

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product3])
order3 = Order([product2])
order4 = Order([product3, product4])

# Выводим информацию о заказах
print(order1)
print(order2)
print(order3)
print(order4)

# Создаем клиента и добавляем заказы
customer1 = Customer("Дима")
customer1.add_order(order1)
customer1.add_order(order2)

customer2 = Customer("Полина")
customer2.add_order(order3)
customer2.add_order(order4)

print(customer1)
print(customer2)

# Выводим общее количество всех заказов для всех клиентов
print(f"Количество всех заказов для всех клиентов: {Order.total_orders()}")
# Выводим общую сумму всех заказов для всех клиентов
print(f"Сумма всех заказов для всех клиентов: {Order.total_amount()}")

