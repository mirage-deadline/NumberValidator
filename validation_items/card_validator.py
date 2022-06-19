from errors import CardMinLengthError
from typing import Union


class CardValidator:

    def __init__(self, card_number: Union[str, int]) -> None:
        if isinstance(card_number, int):
            self.card_number = str(card_number)
        else: 
            self.card_number = card_number
        self.card_len = len(str(card_number))
        if self.card_len < 12:
            raise CardMinLengthError('Minimal card number length should be more or equal than 12 digits.')

    @classmethod
    def is_valid(cls, card_number: Union[int, list[int]]):
        return cls(card_number)._check_for_existing_card()

    def _check_for_existing_card(self) -> bool:
        even = False
        if self.card_len % 2 == 0:
            even = True
        return self._calc_digit_sum(even)

    def _calc_digit_sum(self, is_even: bool) -> bool:
        """Method to check card possible number

        Args:
            is_even (bool): if card have even numbers count -> True

        Returns:
            bool
        """
        start_step = 1 if is_even else 0
        control_sum = 0
        for idx, digit in enumerate(reversed(self.card_number)):
            digit = int(digit)
            if idx % 2 == start_step:
                pre_sum = 2 * digit
                control_sum += pre_sum if pre_sum < 9 else pre_sum - 9
            else:
                control_sum += digit
        if control_sum % 10 == 0:
            return True
        return False
    
    @property
    def payment_system(self):
        _payment_system_pool = {
            '2': 'Мир',
            '3': {
                ('30', '36', '38'): 'Diners Club',
                ('31', '35'): 'JCB International',
                ('34', '37'): 'American Express',
            },
            '4': 'Visa',
            '5': {
                ('50', '56', '57', '58'): 'Maestro',
                ('51', '52', '53', '54', '55'): 'MasterCard'
            },
            '6': {
                '60': 'Discover',
                '62': 'China UnionPay',
                ('63', '67'): 'Maestro'
            },
            '7': 'УЭК' 
        }
        first_number = self.card_number[0]
        if first_number not in _payment_system_pool.keys():
            return 'Unknown payment system.'
        else:
            if isinstance(_payment_system_pool[first_number], dict):
                two_first_digits = self.card_number[0:2]
                for _ in _payment_system_pool[first_number]:
                    for inner_key, bank in _payment_system_pool[first_number].items():
                        if two_first_digits in inner_key:
                            return f'{bank} payment system.'
                    return 'Unknown payment system.'
            else:
                return f'{_payment_system_pool[first_number]} payment system.'

    def __str__(self) -> str:
        if self._check_for_existing_card():
            return f'Card with number {self.card_number} is real.'
        else:
            return f"Card with number {self.card_number} isn't real."

    def __bool__(self):
        return self._check_for_existing_card()

    def __len__(self):
        return self.card_len
