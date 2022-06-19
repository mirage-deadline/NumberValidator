import pytest
from validation_items.card_validator import CardValidator


@pytest.mark.parametrize('card_number,is_exists', [
    (5486732058864471, True),
    (3566002020360505, True),
    (3530111333300000, True),
    (5105105105105100, True),
    (4300000000000777, True),
    (4300000000000771, False),
    (4300001000000777, False),
    (4300200000000777, False),
    (3566002020360515, False),
    (4111111111111112, False),
])
def test_card_for_real_card_number(card_number, is_exists):
    assert CardValidator.is_valid(card_number) == is_exists, 'Tests going wrong'


@pytest.mark.parametrize('card_number,payment_system', [
    (1986732058864471, 'Unknown payment system.'),
    (2086732058864471, 'Мир payment system.'),
    (2886732058864471, 'Мир payment system.'),
    (2986732058864471, 'Мир payment system.'),
    (3086732058864471, 'Diners Club payment system.'),
    (3186732058864471, 'JCB International payment system.'),
    (3286732058864471, 'Unknown payment system.'),
    (3386732058864471, 'Unknown payment system.'),
    (3486732058864471, 'American Express payment system.'),
    (3586732058864471, 'JCB International payment system.'),
    (3686732058864471, 'Diners Club payment system.'),
    (3786732058864471, 'American Express payment system.'),
    (3886732058864471, 'Diners Club payment system.'),
    (3986732058864471, 'Unknown payment system.'),
    (4686732058864471, 'Visa payment system.'),
    (4786732058864471, 'Visa payment system.'),
    (4886732058864471, 'Visa payment system.'),
    (4986732058864471, 'Visa payment system.'),
    (5086732058864471, 'Maestro payment system.'),
    (5186732058864471, 'MasterCard payment system.'),
    (5286732058864471, 'MasterCard payment system.'),
    (5386732058864471, 'MasterCard payment system.'),
    (5486732058864471, 'MasterCard payment system.'),
    (5586732058864471, 'MasterCard payment system.'),
    (5686732058864471, 'Maestro payment system.'),
    (5786732058864471, 'Maestro payment system.'),
    (5886732058864471, 'Maestro payment system.'),
    (5986732058864471, 'Unknown payment system.'),
    (6086732058864471, 'Discover payment system.'),
    (6186732058864471, 'Unknown payment system.'),
    (6286732058864471, 'China UnionPay payment system.'),
    (6386732058864471, 'Maestro payment system.'),
    (6486732058864471, 'Unknown payment system.'),
    (6586732058864471, 'Unknown payment system.'),
    (6686732058864471, 'Unknown payment system.'),
    (6786732058864471, 'Maestro payment system.'),
    (6886732058864471, 'Unknown payment system.'),
    (6986732058864471, 'Unknown payment system.'),
    (7086732058864471, 'УЭК payment system.'),
    (7186732058864471, 'УЭК payment system.')
])
def test_card_payment_system(card_number, payment_system):
    assert CardValidator(card_number).payment_system == payment_system, 'Payment system not correct'
