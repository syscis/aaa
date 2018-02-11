import unittest
from Fraction import Fraction
from MixedFraction import MixedFraction

__author__ = 'Hunt Blanchat'


class TestMixed(unittest.TestCase):

    def setUp(self):
        self.f0 = Fraction(1, 8)
        self.mf1 = MixedFraction(25, 5)
        self.mf2 = MixedFraction(20, 4)
        self.mf3 = MixedFraction(15, 2)
        self.mf4 = MixedFraction(100, 800)

    def tearDown(self):
        pass

    def test_booleans(self):
        self.assertEqual(self.mf1 == self.mf2, True)
        self.assertEqual(self.mf1 == self.f0, False)
        self.assertEqual(self.f0 == self.mf4, True)
        self.assertEqual(self.mf1 > self.mf2, False)
        self.assertEqual(self.mf1 < self.mf3, True)
        self.assertEqual(self.mf1 <= self.mf2, True)
        self.assertEqual(self.mf1 >= self.mf2, True)

    def test_calculations(self):
        self.assertEqual(self.mf1 * self.mf1, Fraction(625, 25))
        self.assertEqual(self.mf1 * self.mf1, MixedFraction(625, 25))
        self.assertEqual(self.mf1 * self.f0, Fraction(25, 40))
        self.assertEqual(self.mf1 * self.f0, MixedFraction(25, 40))
        self.assertEqual(self.mf1 / self.mf3, Fraction(50, 75))
        self.assertEqual(self.mf1 / self.mf3, MixedFraction(50, 75))
        self.assertEqual(self.mf2 / self.f0, Fraction(160, 4))
        self.assertEqual(self.mf2 / self.f0, MixedFraction(160, 4))


def main():
    fraction_list = []
    mixed_fraction_list = []
    for line in open('fractions.dat', 'r'):
        line = Fraction.from_string(line)
        if line != Fraction(0):
            fraction_list.append(line)
    fraction_sum = Fraction(0)
    for item in fraction_list:
        fraction_sum += item
    mixed_sum = MixedFraction(0)
    for line in open('MixedFractions.dat', 'r'):
        line = MixedFraction.from_string(line)
        if line != MixedFraction(0):
            mixed_fraction_list.append(line)
    for item in mixed_fraction_list:
        mixed_sum += item
    holder = '{:} = {:}'.format(
        ' + '.join('{:}'.format(f) for f in fraction_list),
        fraction_sum)
    print(holder)
    holder = '{:} = {:}'.format(' + '.join('{:}'.format(f)
                                for f in mixed_fraction_list), mixed_sum)
    print(holder)
    mixed_plus = mixed_sum + fraction_sum
    print(mixed_sum, '+', fraction_sum, '=', mixed_plus, '\n')
    for item in fraction_list:
        print(mixed_plus, '-', item, '=', mixed_plus - item)
        mixed_plus -= item


if __name__ == '__main__':
    main()
    unittest.main()
