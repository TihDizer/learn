import pytest
from shop.pricing import DeliveryCalculator, DiscountCalculator
from shop.models import Item, User

@pytest.fixture
def basic_item():
    return Item(id="test", price=100.0, quantity=1, weight=1.0, is_fragile=False)

@pytest.fixture
def fragile_item():
    return Item(id="test", price=50000.0, quantity=1, weight=1.0, is_fragile=True)

@pytest.mark.parametrize("zone, expected_fee", [
    ("ZONE_1", 200.0),
    ("ZONE_2", 500.0),
    ("ZONE_3", 700.0),
    ("ZONE_4", 200.0),
    ("RUSSIA", 200.0)
])
def test_delivery_by_zones(zone, expected_fee, basic_item):
    calculator = DeliveryCalculator()
    item = basic_item

    result = calculator.calculate_delivery([item], zone)
    assert result == expected_fee

@pytest.mark.parametrize("zone", [
    "ZONE_1",
    "ZONE_2",
    "ZONE_3",
    "ZONE_4",
    "RUSSIA"
])
def test_delivery_by_zones_empty(zone):
    calculator = DeliveryCalculator()
    result = calculator.calculate_delivery([], zone)
    assert result == 0.0

def test_delivery_fragile_item(basic_item, fragile_item):
    calculator = DeliveryCalculator()
    result = calculator.calculate_delivery([basic_item, fragile_item], "ZONE_1")
    assert result == 350.0

@pytest.fixture
def vip_user():
    return User(id="user-vip", is_vip=True)

def test_discount(vip_user):
    calculator = DiscountCalculator()
    result = calculator.calculate_discount(vip_user, 50000.0)
    assert result == 42500.0
