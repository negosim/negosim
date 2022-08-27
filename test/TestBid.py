import unittest
from core.Bid import Bid


class TestBid(unittest.TestCase):

    def test_get_issues_items1(self):
        issue_item = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid = Bid(issue_item)
        self.assertIsInstance(bid.get_issues_items(), dict)

    def test_get_issues_items2(self):
        self.assertRaises(TypeError, Bid, [])

    def test_is_equal1(self):
        issue_item1 = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid1 = Bid(issue_item1)
        issue_item2 = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid2 = Bid(issue_item2)
        self.assertTrue(bid1.is_equal(bid2))

    def test_is_equal2(self):
        issue_item1 = {'Brand': 'Lenov', 'Monitor': '15', 'HDD': '1T'}
        bid1 = Bid(issue_item1)
        issue_item2 = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid2 = Bid(issue_item2)
        self.assertFalse(bid1.is_equal(bid2))

    def test_is_equal3(self):
        issue_item1 = {'Brand': '', 'Monitor': '15', 'HDD': '1T'}
        bid1 = Bid(issue_item1)
        issue_item2 = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid2 = Bid(issue_item2)
        self.assertFalse(bid1.is_equal(bid2))

    def test_is_equal4(self):
        issue_item1 = {'Brand': None, 'Monitor': '15', 'HDD': '1T'}
        bid1 = Bid(issue_item1)
        issue_item2 = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid2 = Bid(issue_item2)
        self.assertFalse(bid1.is_equal(bid2))

    def test_is_equal5(self):
        issue_item1 = {'Monitor': '15', 'HDD': '1T'}
        bid1 = Bid(issue_item1)
        issue_item2 = {'Brand': 'Lenovo', 'Monitor': '15', 'HDD': '1T'}
        bid2 = Bid(issue_item2)
        self.assertFalse(bid1.is_equal(bid2))

    def test_is_equal6(self):
        issue_item1 = {'Monitor': '15', 'HDD': '1T'}
        bid1 = Bid(issue_item1)
        self.assertRaises(TypeError, bid1.is_equal, None)


if __name__ == '__main__':
    unittest.main()
