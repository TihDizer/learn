from datetime import date
from typing import List, Callable, Optional
from shop.models import User, Item, PromoCode
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


class DiscountCalculator:
    # time_provider по умолчанию возвращает реальное "сегодня", но в тестах мы его подменим
    def __init__(self, time_provider: Callable[[], date] = date.today):
        args = [time_provider]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDiscountCalculatorǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁDiscountCalculatorǁ__init____mutmut_mutants'), args, kwargs, self)
    # time_provider по умолчанию возвращает реальное "сегодня", но в тестах мы его подменим
    def xǁDiscountCalculatorǁ__init____mutmut_orig(self, time_provider: Callable[[], date] = date.today):
        self._time_provider = time_provider
    # time_provider по умолчанию возвращает реальное "сегодня", но в тестах мы его подменим
    def xǁDiscountCalculatorǁ__init____mutmut_1(self, time_provider: Callable[[], date] = date.today):
        self._time_provider = None
    
    xǁDiscountCalculatorǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDiscountCalculatorǁ__init____mutmut_1': xǁDiscountCalculatorǁ__init____mutmut_1
    }
    xǁDiscountCalculatorǁ__init____mutmut_orig.__name__ = 'xǁDiscountCalculatorǁ__init__'

    def calculate_discount(self, user: User, total_amount: float) -> float:
        args = [user, total_amount]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDiscountCalculatorǁcalculate_discount__mutmut_orig'), object.__getattribute__(self, 'xǁDiscountCalculatorǁcalculate_discount__mutmut_mutants'), args, kwargs, self)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_orig(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_1(self, user: User, total_amount: float) -> float:
        if total_amount <= 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_2(self, user: User, total_amount: float) -> float:
        if total_amount < 1:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_3(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError(None)

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_4(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("XXTotal amount cannot be negativeXX")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_5(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_6(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("TOTAL AMOUNT CANNOT BE NEGATIVE")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_7(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = None

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_8(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 1.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_9(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage = 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_10(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage -= 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_11(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 1.1

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_12(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount > 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_13(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5001.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_14(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage = 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_15(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage -= 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_16(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 1.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_17(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage >= 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_18(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 1.15:
            discount_percentage = 0.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_19(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = None

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_20(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 1.15

        return total_amount - (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_21(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount + (total_amount * discount_percentage)

    def xǁDiscountCalculatorǁcalculate_discount__mutmut_22(self, user: User, total_amount: float) -> float:
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        discount_percentage = 0.0

        if user.is_vip:
            discount_percentage += 0.10

        if total_amount >= 5000.0:
            discount_percentage += 0.05

        if discount_percentage > 0.15:
            discount_percentage = 0.15

        return total_amount - (total_amount / discount_percentage)
    
    xǁDiscountCalculatorǁcalculate_discount__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDiscountCalculatorǁcalculate_discount__mutmut_1': xǁDiscountCalculatorǁcalculate_discount__mutmut_1, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_2': xǁDiscountCalculatorǁcalculate_discount__mutmut_2, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_3': xǁDiscountCalculatorǁcalculate_discount__mutmut_3, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_4': xǁDiscountCalculatorǁcalculate_discount__mutmut_4, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_5': xǁDiscountCalculatorǁcalculate_discount__mutmut_5, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_6': xǁDiscountCalculatorǁcalculate_discount__mutmut_6, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_7': xǁDiscountCalculatorǁcalculate_discount__mutmut_7, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_8': xǁDiscountCalculatorǁcalculate_discount__mutmut_8, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_9': xǁDiscountCalculatorǁcalculate_discount__mutmut_9, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_10': xǁDiscountCalculatorǁcalculate_discount__mutmut_10, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_11': xǁDiscountCalculatorǁcalculate_discount__mutmut_11, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_12': xǁDiscountCalculatorǁcalculate_discount__mutmut_12, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_13': xǁDiscountCalculatorǁcalculate_discount__mutmut_13, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_14': xǁDiscountCalculatorǁcalculate_discount__mutmut_14, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_15': xǁDiscountCalculatorǁcalculate_discount__mutmut_15, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_16': xǁDiscountCalculatorǁcalculate_discount__mutmut_16, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_17': xǁDiscountCalculatorǁcalculate_discount__mutmut_17, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_18': xǁDiscountCalculatorǁcalculate_discount__mutmut_18, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_19': xǁDiscountCalculatorǁcalculate_discount__mutmut_19, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_20': xǁDiscountCalculatorǁcalculate_discount__mutmut_20, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_21': xǁDiscountCalculatorǁcalculate_discount__mutmut_21, 
        'xǁDiscountCalculatorǁcalculate_discount__mutmut_22': xǁDiscountCalculatorǁcalculate_discount__mutmut_22
    }
    xǁDiscountCalculatorǁcalculate_discount__mutmut_orig.__name__ = 'xǁDiscountCalculatorǁcalculate_discount'

    def apply_promo_code(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        args = [current_total, promo_code]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDiscountCalculatorǁapply_promo_code__mutmut_orig'), object.__getattribute__(self, 'xǁDiscountCalculatorǁapply_promo_code__mutmut_mutants'), args, kwargs, self)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_orig(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_1(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_2(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = None
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_3(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today >= promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_4(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError(None)

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_5(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("XXPromo code expiredXX")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_6(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("promo code expired")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_7(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("PROMO CODE EXPIRED")

        return max(0.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_8(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(None, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_9(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, None)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_10(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_11(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, )

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_12(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(1.0, current_total - promo_code.discount_amount)

    def xǁDiscountCalculatorǁapply_promo_code__mutmut_13(self, current_total: float, promo_code: Optional[PromoCode]) -> float:
        if not promo_code:
            return current_total

        today = self._time_provider()
        if today > promo_code.expiry_date:
            raise ValueError("Promo code expired")

        return max(0.0, current_total + promo_code.discount_amount)
    
    xǁDiscountCalculatorǁapply_promo_code__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDiscountCalculatorǁapply_promo_code__mutmut_1': xǁDiscountCalculatorǁapply_promo_code__mutmut_1, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_2': xǁDiscountCalculatorǁapply_promo_code__mutmut_2, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_3': xǁDiscountCalculatorǁapply_promo_code__mutmut_3, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_4': xǁDiscountCalculatorǁapply_promo_code__mutmut_4, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_5': xǁDiscountCalculatorǁapply_promo_code__mutmut_5, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_6': xǁDiscountCalculatorǁapply_promo_code__mutmut_6, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_7': xǁDiscountCalculatorǁapply_promo_code__mutmut_7, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_8': xǁDiscountCalculatorǁapply_promo_code__mutmut_8, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_9': xǁDiscountCalculatorǁapply_promo_code__mutmut_9, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_10': xǁDiscountCalculatorǁapply_promo_code__mutmut_10, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_11': xǁDiscountCalculatorǁapply_promo_code__mutmut_11, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_12': xǁDiscountCalculatorǁapply_promo_code__mutmut_12, 
        'xǁDiscountCalculatorǁapply_promo_code__mutmut_13': xǁDiscountCalculatorǁapply_promo_code__mutmut_13
    }
    xǁDiscountCalculatorǁapply_promo_code__mutmut_orig.__name__ = 'xǁDiscountCalculatorǁapply_promo_code'


class DeliveryCalculator:
    BASE_FEE = 200.0

    def calculate_delivery(self, items: List[Item], delivery_zone: str) -> float:
        args = [items, delivery_zone]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_orig'), object.__getattribute__(self, 'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_mutants'), args, kwargs, self)

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_orig(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_1(self, items: List[Item], delivery_zone: str) -> float:
        if items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_2(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 1.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_3(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = None

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_4(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone != "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_5(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "XXZONE_2XX":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_6(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "zone_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_7(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery = 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_8(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery -= 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_9(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 301.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_10(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone != "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_11(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "XXZONE_3XX":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_12(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "zone_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_13(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery = 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_14(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery -= 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_15(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 501.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_16(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight >= 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_17(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 6.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_18(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery = (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_19(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery -= (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_20(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 / item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_21(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) / 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_22(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight + 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_23(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 6.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_24(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 51 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_25(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery = 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_26(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery -= 150.0 * item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_27(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 150.0 / item.quantity

        return total_delivery

    def xǁDeliveryCalculatorǁcalculate_delivery__mutmut_28(self, items: List[Item], delivery_zone: str) -> float:
        if not items:
            return 0.0

        total_delivery = self.BASE_FEE

        if delivery_zone == "ZONE_2":
            total_delivery += 300.0
        elif delivery_zone == "ZONE_3":
            total_delivery += 500.0

        for item in items:
            if item.weight > 5.0:
                total_delivery += (item.weight - 5.0) * 50 * item.quantity
            if item.is_fragile:
                total_delivery += 151.0 * item.quantity

        return total_delivery
    
    xǁDeliveryCalculatorǁcalculate_delivery__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_1': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_1, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_2': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_2, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_3': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_3, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_4': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_4, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_5': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_5, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_6': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_6, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_7': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_7, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_8': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_8, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_9': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_9, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_10': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_10, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_11': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_11, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_12': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_12, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_13': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_13, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_14': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_14, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_15': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_15, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_16': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_16, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_17': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_17, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_18': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_18, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_19': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_19, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_20': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_20, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_21': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_21, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_22': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_22, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_23': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_23, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_24': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_24, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_25': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_25, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_26': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_26, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_27': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_27, 
        'xǁDeliveryCalculatorǁcalculate_delivery__mutmut_28': xǁDeliveryCalculatorǁcalculate_delivery__mutmut_28
    }
    xǁDeliveryCalculatorǁcalculate_delivery__mutmut_orig.__name__ = 'xǁDeliveryCalculatorǁcalculate_delivery'
