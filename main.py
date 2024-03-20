# вариант 13

import random

class Generator1:
    PASSWORD_LENGTH: int = 5
    ALPHABET: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    ALPHABET_LENGTH: int = len(ALPHABET)

    @staticmethod
    def print_password(password):
        print(f'Сгенерированный пароль (задание 1): {password}')

    @staticmethod
    def hello():
        print('1 задание.')
        print('Генератор использует следующие параметры:')
        print('S* = 500000;')
        print('A = 36 (малые буквы английского алфавита и цифры от 0 до 9);')
        print('L = 5')
        print('A^L = 60`466`176')

    def generate(self):
        password = list | str
        password = [random.choice(self.ALPHABET) for _ in range(self.PASSWORD_LENGTH)]
        password = ''.join(password)
        return password
    
    @classmethod
    def start(cls):
        cls.hello()
        password = cls.generate(cls)
        cls.print_password(password=password)

class Generator2:
    PASSWORD_FIRST_PART_LENGTH: int = 3
    PASSWORD_SECOND_PART_LENGTH: int = 4
    PASSWORD_LENGTH = PASSWORD_FIRST_PART_LENGTH + PASSWORD_SECOND_PART_LENGTH
    NUMBERS: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    LETTERS: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ALPHABET: list = LETTERS + NUMBERS
    ALPHABET_LENGTH: int = len(ALPHABET)

    @staticmethod
    def print_password(password):
        print(f'Сгенерированный пароль (задание 2): {password}')

    @staticmethod
    def hello():
        print('2 задание.')
        print('Генератор использует следующие параметры:')
        print('S* = 500000;')
        print('A = 36 (малые буквы английского алфавита и цифры от 0 до 9);')
        print('L = 7 (увеличено, чтобы сохранить стойкость)')
        print('A^L = 1`679`616`000')

    def generate(self):
        password = list | str
        password_first_part = [random.choice(self.NUMBERS) for _ in range(self.PASSWORD_FIRST_PART_LENGTH)]
        password_second_part = [random.choice(self.ALPHABET) for _ in range(self.PASSWORD_SECOND_PART_LENGTH)]
        password = password_first_part + password_second_part
        password = ''.join(password)
        return password
    
    @classmethod
    def start(cls):
        cls.hello()
        password = cls.generate(cls)
        cls.print_password(password=password)

if __name__ == '__main__':
    generator1 = Generator1()
    generator1.start()
    generator2 = Generator2()
    generator2.start()
