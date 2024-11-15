from unittest import TestCase


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    a % b
    if a % b == 0:
        return True
    else:
        return False


def mo8(a):
    if len(a) <= 8:
        return True
    else:
        return False


class MyTest(TestCase):
    def test1(self):
        return self.assertEqual(multiplication(3, 5), 15, 'bruh')

    def test2(self):
        return self.assertEqual(multiplication(2, 2), 5, 'bruh')

    def test3(self):
        return self.assertEqual(division(10, 2), 5, 'bruh')

    def test4(self):
        return self.assertEqual(division(40, 10), 3, 'bruh')

    def test5(self):
        return self.assertEqual(remainder(6, 4), False, 'bruh')

    def test6(self):
        return self.assertEqual(remainder(51, 50), True, 'bruh')

    def test7(self):
        return self.assertEqual(mo8('cheburek'), True, 'bruh')

    def test8(self):
        return self.assertEqual(mo8('나는 먹고 싶다!!!'), True, 'bruh')