import pytest
from unittest.mock import MagicMock
from datetime import date

from src.shop.models import User, Item, PromoCode
from src.shop.order_processor import OrderProcessor
from src.shop.pricing import DiscountCalculator, DeliveryCalculator


# =====================================================================
# 🛠 ФИКСТУРЫ (Замена @BeforeEach из Java)
# Pytest автоматически создаст эти объекты и передаст их в тесты.
# =====================================================================

@pytest.fixture
def mock_inventory():
    """Создает и возвращает "чистый" мок склада для каждого теста."""
    return MagicMock()


@pytest.fixture
def mock_payment():
    """Создает и возвращает "чистый" мок банка для каждого теста."""
    return MagicMock()


@pytest.fixture
def order_processor(mock_inventory, mock_payment):
    """
    Магия Pytest: эта фикстура сама запрашивает две предыдущие фикстуры!
    Мы собираем реальный OrderProcessor, подсовывая ему моки и реальные калькуляторы.
    """
    fake_today = lambda: date(2024, 1, 1)  # Фиксируем время для стабильности
    discount_calc = DiscountCalculator(time_provider=fake_today)
    delivery_calc = DeliveryCalculator()

    return OrderProcessor(
        inventory_service=mock_inventory,
        payment_gateway=mock_payment,
        discount_calculator=discount_calc,
        delivery_calculator=delivery_calc
    )


@pytest.fixture
def standard_user():
    """Готовый тестовый пользователь."""
    return User(id="user-123", is_vip=False)


@pytest.fixture
def standard_cart():
    """Готовая тестовая корзина с одним ноутбуком."""
    return [Item(id="item-macbook", price=2000.0, quantity=1, weight=2.0, is_fragile=True)]


# =====================================================================
# 🧪 САМ ТЕСТ
# =====================================================================

def test_should_throw_exception_and_not_charge_when_out_of_stock(
        order_processor, mock_inventory, mock_payment, standard_user, standard_cart
):
    """
    Обратите внимание на аргументы функции!
    Pytest сам найдет фикстуры с такими именами и передаст их сюда.
    Тест получается ОЧЕНЬ коротким и сфокусированным только на логике.
    """

    # 1. ARRANGE (Настраиваем поведение мока для КОНКРЕТНО ЭТОГО теста)
    mock_inventory.in_stock.return_value = False

    # 2. ACT & ASSERT (Проверяем, что вылетает правильная ошибка)
    with pytest.raises(RuntimeError, match="Item item-macbook is out of stock"):
        order_processor.process_order(
            user=standard_user,
            items=standard_cart,
            delivery_zone="ZONE_1"
        )

    # 3. VERIFY (Проверяем побочные эффекты)
    # Гарантируем, что процессор упал до того, как попытался снять деньги
    mock_payment.charge.assert_not_called()


@pytest.fixture
def standart_promo_code():
    fake_today = date(2024, 1, 1)
    return PromoCode(code="STANDARD", discount_amount=100, expiry_date=fake_today)


def test_should_throw_exception_when_no_items(
        order_processor, mock_inventory, mock_payment, standard_user, standard_cart
):
    with pytest.raises(ValueError, match="Order must contain at least one item"):
        order_processor.process_order(
            user=standard_user,
            items=[],
            delivery_zone="ZONE_1"
        )

    mock_inventory.in_stock.assert_not_called()
    mock_payment.charge.assert_not_called()

def test_final_price(
        order_processor, mock_inventory, mock_payment, standard_user, standard_cart, standart_promo_code
):
    mock_inventory.in_stock.return_value = True
    mock_payment.charge.return_value = True

    order = order_processor.process_order(
        user=standard_user,
        items=standard_cart,
        delivery_zone="ZONE_1",
        promo_code=standart_promo_code
    )

    mock_payment.charge.assert_called_with(standard_user, 2250.0)
    assert order.final_price == 2250.0
