import unittest
from unittest.mock import Mock
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.Preference import Preference
from core.Bid import Bid


class TestUtilitySpace(unittest.TestCase):

    def test_get_utility(self):
        """
            preference = {
                'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
                'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
                'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
            }
        """
        bid_dict = {
                    'Brand': 'Mac',
                    'Monitor': '15',
                    'HDD': '3T'
                    }

        bid = Mock(spec_set=Bid)
        bid.get_issues_items = Mock(return_value=bid_dict)

        def get_issue_weight_func(args):
            if args == 'Brand':
                return 0.4
            if args == 'Monitor':
                return 0.35
            if args == 'HDD':
                return 0.25

        def get_issue_item_value_func(issue, item):
            if issue == 'Brand' and item == 'Mac':
                return 30, 30
            if issue == 'Monitor' and item == '15':
                return 30, 30
            if issue == 'HDD' and item == '3T':
                return 35, 35

        preference = Mock(spec_set=Preference)
        preference.get_issue_weight = Mock(side_effect=get_issue_weight_func)
        preference.get_issue_item_value = Mock(side_effect=get_issue_item_value_func)

        utility_space = AdditiveUtilitySpace(preference)
        self.assertEqual(1, utility_space.get_utility(bid))


if __name__ == '__main__':
    unittest.main()