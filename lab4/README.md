# First iteration

![mutmut results](.mutmut1.md)

Выжило много мутаций, так как тесты проверяют логику поверхностно

Посмотрим первую выжившую
```bash
❯❯ mutmut show shop.order_processor.xǁOrderProcessorǁprocess_order__mutmut_3
# shop.order_processor.xǁOrderProcessorǁprocess_order__mutmut_3: survived
--- shop/order_processor.py
+++ shop/order_processor.py
@@ -1,7 +1,7 @@
 def process_order(self, user: User, items: List[Item], delivery_zone: str,
                   promo_code: Optional[PromoCode] = None) -> Order:
     if not items:
-        raise ValueError("Order must contain at least one item")
+        raise ValueError("XXOrder must contain at least one itemXX")

     # 1. Проверяем наличие
     raw_total = 0.0
❯❯
```

Мутант изменил строку ошибки, но тест всё равно завершился успешно для фикса необходимо проверять строку строго

```python
with pytest.raises(ValueError, match="^Order must contain at least one item$"):
        order_processor.process_order(
            user=standard_user,
            items=[],
            delivery_zone="ZONE_1"
        )
```

После этого этот мутант умер

Посмотрим 9

```bash
# shop.order_processor.xǁOrderProcessorǁprocess_order__mutmut_9: survived
--- shop/order_processor.py
+++ shop/order_processor.py
@@ -6,7 +6,7 @@
     # 1. Проверяем наличие
     raw_total = 0.0
     for item in items:
-        if not self.inventory_service.in_stock(item.id, item.quantity):
+        if not self.inventory_service.in_stock(None, item.quantity):
             raise RuntimeError(f"Item {item.id} is out of stock")
         raw_total += item.price * item.quantity

❯❯
```

Мок всегда возвращает in_stock=FaLse

Фикс: `mock_inventory.in_stock.assert_called_once_with("item-macbook", 1)` - проверяет вызвали ли мы ту корзину

После этого:

![mutmut results](.mutmut2.md)

Количество выживших уменьшилось

Посмотрев еще мутантов, добавил проверку на негативеую корзину:


```python
def test_calculate_discount_negative_amount(vip_user):
    calculator = DiscountCalculator()
    
    with pytest.raises(ValueError, match="^Total amount cannot be negative$"):
        calculator.calculate_discount(vip_user, total_amount=-100.0)
```

еще 4 мутанта погибло `⠼ 150/150  🎉 88 🫥 15  ⏰ 0  🤔 0  🙁 47  🔇 0  🧙 0`

Для отмены заказа тестов нет) 

```python
❯❯ mutmut show shop.order_processor.xǁOrderProcessorǁcancel_order__mutmut_9
# shop.order_processor.xǁOrderProcessorǁcancel_order__mutmut_9: no tests
--- shop/order_processor.py
+++ shop/order_processor.py
@@ -3,7 +3,7 @@
         raise RuntimeError("Cannot cancel a shipped order")

     if order.status == OrderStatus.PAID:
-        self.payment_gateway.refund(order.user, order.final_price)
+        self.payment_gateway.refund(order.final_price)

     for item in order.items:
         self.inventory_service.return_item(item.id, item.quantity)
```

Добавим тесты -> `150/150  🎉 102 🫥 0  ⏰ 0  🤔 0  🙁 48  🔇 0  🧙 0`

Не проверяю граничные условия:

```python
❯❯ mutmut show shop.pricing.xǁDeliveryCalculatorǁcalculate_delivery__mutmut_16
# shop.pricing.xǁDeliveryCalculatorǁcalculate_delivery__mutmut_16: survived
--- shop/pricing.py
+++ shop/pricing.py
@@ -10,7 +10,7 @@
         total_delivery += 500.0

     for item in items:
-        if item.weight > 5.0:
+        if item.weight >= 5.0:
             total_delivery += (item.weight - 5.0) * 50 * item.quantity
         if item.is_fragile:
             total_delivery += 150.0 * item.quantity
```

Результат ->
