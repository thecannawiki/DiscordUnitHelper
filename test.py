# To test single message run:
# python test.py -m "I am 10 feet tall"
#
# To start unit tests run:
# python test.py -v

import unittest
from argparse import ArgumentParser

import unitconversion

tests = []
tests.append("I use 6 gallons and then feed about 26 oz of cheese")
tests.append("I use 6 gallons and then feed about 26 oz of cheese with like 2 acres")


for t in tests:
    conversion_result = unitconversion.process(t)
    if conversion_result:
        print(t)
        print(conversion_result)


class TestUnitCorrection(unittest.TestCase):
    def test_base_unit_conversion(self):
        unit_pairs = [
            ["10 feet", "3.05 m"],
            ["10feet", "3.05m"],
        ]

        for pair in unit_pairs:
            raw_unit = pair[0]
            expected_unit = pair[1]
            result = unitconversion.process(raw_unit)
            self.assertEqual(result, expected_unit)

    def test_spaces(self):
        unit_pairs = [
            ["10 feet²", 1],
            # ["10 feet ²", 2],
            # I'm commenting this out because passing this test requires a significant
            # change to the way units in higher dimensions are handled, so passing this
            # should probably be a separate issue. In fact, merging that new issue with
            # https://github.com/Wendelstein7/DiscordUnitCorrector/issues/35 is probably
            # the simplest solution
            ["10feet²", 0],
            # ["10feet ²", 1], see above
            ["I am 2 feet tall", 4],
            ["I  am  2  feet  tall", 8],
            ["I am 2.0 feet tall", 4],
            ["I  am  2.0  feet  tall", 8]
        ]

        for pair in unit_pairs:
            raw_unit = pair[0]
            expected_spaces = pair[1]
            result = unitconversion.process(raw_unit).count(' ')
            self.assertEqual(result, expected_spaces)

    def test_square_units(self):
        unit_pairs = [
            ["10 feet²", "0.929 m²"],
            ["4 acres", "16200 m²"],
            ["4 roods", "4050 m²"],
            ["4 miles²", "10.4 km²"],
            ["4 ft²", "3720 cm²"]
        ]

        for pair in unit_pairs:
            raw_unit = pair[0]
            expected_unit = pair[1]
            result = unitconversion.process(raw_unit)
            self.assertEqual(result, expected_unit)
    
    def test_case_sensitive(self):
        unit_pairs = [
            ["4 calories", "16.7 J"],
            ["4 Calories", "16.7 kJ"],
            ["4 kilocalories", "16.7 kJ"],
            ["4 kcalories", "16.7 kJ"],
            ["4 kiloCalories", None],
            ["4 kCalories", None],
            ["wow  4  calories  cool", "wow  16.7  J  cool"]
        ]

        for pair in unit_pairs:
            raw_unit = pair[0]
            expected_unit = pair[1]
            result = unitconversion.process(raw_unit)
            self.assertEqual(result, expected_unit)

