import unittest
from search import Search
import dateutil.parser


class Testing(unittest.TestCase):
    def test_amount_spent(self):
        search = Search()
        tests = {
            "Electronics": 2801.71,
            "Tools": 2254.08,
            "Computers": 1559.44,
            "Clothing": 2149.10,
            "Baby": 1867.75,
            "Automotive": 2583.19
        }
        for key in tests:
            self.assertAlmostEqual(tests[key], search.amount_spent(
                key), msg="amount_spent('" + key + "') incorrect", delta=0.01)

    def test_all_categories(self):
        search = Search()
        expected = {'Automotive': 2583.19,
                    'Baby': 1867.75,
                    'Beauty': 2610.36,
                    'Books': 2202.92,
                    'Clothing': 2149.1,
                    'Computers': 1559.44,
                    'Electronics': 2801.71,
                    'Games': 2104.78,
                    'Garden': 2135.05,
                    'Grocery': 2584.62,
                    'Health': 2327.3,
                    'Home': 2547.92,
                    'Industrial': 2530.89,
                    'Jewelery': 2627.25,
                    'Kids': 2062.8,
                    'Movies': 2496.55,
                    'Music': 2394.53,
                    'Outdoors': 2785.54,
                    'Shoes': 2235.54,
                    'Sports': 1975.91,
                    'Tools': 2254.08,
                    'Toys': 2054.75}
        actual = search.all_categories()
        self.assertEqual(
            expected, actual, 'all_categories() did not return the correct dictionary')

    def test_spent_between_dates(self):
        search = Search()
        tests = []
        tests.append(('2020-01-01T00:00:00Z', '2020-01-31T23:59:59Z', 4146.31))
        tests.append(('2020-02-01T00:00:00Z', '2020-05-01T00:00:00Z', 10184.34))
        tests.append(('2019-08-01T00:00:00Z', '2019-12-31T23:59:59Z', 21852.46))
        tests.append(('2020-04-01T00:00:00Z', '2020-04-30T23:59:59Z', 3976.97))
        for test in tests:
            start = dateutil.parser.parse(test[0])
            end = dateutil.parser.parse(test[1])
            exp = test[2]
            self.assertAlmostEqual(exp, search.spent_between(start, end), msg="spent_between('" + test[0] + "', '" + test[1] + "') incorrect", delta=0.01)

    def test_spent_by_gender(self):
        search = Search()
        expected = {"M": 26554.34, "F": 24337.64} 
        actual = search.spent_by_gender()
        self.assertEqual(expected, actual, 'spent_by_gender() did not return the correct dictionary')


if __name__ == '__main__':
    unittest.main()
