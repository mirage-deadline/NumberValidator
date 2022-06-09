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