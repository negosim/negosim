import unittest
from core.Preference import Preference


class TestPreference(unittest.TestCase):

    def setUp(self) -> None:
        self.preference = Preference('laptop', 'laptop_buyer_utility.xml')
        # self.preference = Preference('partydomain', 'party6_utility.xml')

    # def test_get_preference_data_structure(self):
    #     print(self.preference.get_preference_data_structure())
    #
    # def test_get_issue_weight(self):
    #     print(self.preference.get_issue_weight('Laptop'))
    #
    # def test_get_issue_item_value(self):
    #     self.assertEqual((1, 3), self.preference.get_issue_item_value('Laptop', 'Dell'))

    # def test_get_issue_item_value(self):
    #     print(self.preference.get_weights())

    def test_get_issue_ItemValue(self):
        # print(self.preference.get_issue_ItemValue('Laptop'))
        print(self.preference)
        # print(self.preference.get_initial_preference())
        # print(self.preference.get_worst_bid())

if __name__ == '__main__':
    unittest.main()
