import unittest
from functools import reduce
import time
from main import *
from random import randint


class TestingValues(unittest.TestCase):
    def setUp(self):
        with open('testing_values_data.txt', 'w') as file:
            self.testing_data = [randint(-10, 10) for i in range(10)]
            for i in self.testing_data:
                file.write(str(i) + ' ')

    def test_min(self):
        self.assertEqual(my_min(self.testing_data), min(self.testing_data), "Неверный минимальный элемент")

    def test_max(self):
        self.assertEqual(my_max(self.testing_data), max(self.testing_data), "Неверный максимальный элемент")

    def test_sum(self):
        self.assertEqual(my_sum(self.testing_data), sum(self.testing_data), "Неверная сумма элементов")

    def test_product(self):
        self.assertEqual(my_product(self.testing_data), reduce(lambda x, y: x * y, self.testing_data), "Неверное произведение элементов")


class TestingTime(unittest.TestCase):
    def test_time(self):
        for i in range(1, 11):
            with self.subTest(i=i):
                with open('testing_time_data.txt', 'w') as file:
                    testing_data = [randint(0, 100) for j in range(10**5 * i)]
                    for j in testing_data:
                        file.write(str(j) + ' ')
                    file.write('\n')
                start_time = time.time()
                main_func('testing_time_data.txt')
                end_time = time.time()
                self.assertTrue(end_time - start_time < 0.1, "Превышен лимит времени работы программы")


class TestingCustom1(unittest.TestCase):
    def setUp(self):
        with open('testing_custom_data.txt', 'w') as file:
            self.testing_data = [randint(-10, 10) for i in range(10)]
            for i in self.testing_data:
                file.write(str(i) + ' ')
        with open('testing_custom_data.txt', 'r') as file:
            self.testing_data = list(map(int, file.read().split()))

    def test_case_1(self):
        if 0 in self.testing_data:
            self.assertEqual(my_product(self.testing_data), 0)

    def test_case_2(self):
        if any([x < 0 for x in self.testing_data]):
            self.assertTrue(my_min(self.testing_data) < 0)


class TestingCustom2(unittest.TestCase):
    def test_min(self):
        self.assertEqual(my_min([1, 2, 3, 4, 5]), 1, "Неверный минимальный элемент")

    def test_max(self):
        self.assertEqual(my_max([1, 2, 3, 4, 5]), 5, "Неверный максимальный элемент")

    def test_sum(self):
        self.assertEqual(my_sum([1, 2, 3, 4, 5]), 15, "Неверная сумма элементов")

    def test_product(self):
        self.assertEqual(my_product([1, 2, 3, 4, 5]), 120, "Неверное произведение элементов")


if __name__ == '__main__':
    unittest.main()
