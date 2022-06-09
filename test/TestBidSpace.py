import unittest
from core.Preference import Preference
from core.BidSpace import BidSpace


class TestBidSpace(unittest.TestCase):

    def setUp(self) -> None:
        self.p = Preference('laptop', 'laptop_buyer_utility.xml')
        self.bid_space = BidSpace(self.p)

    def test_get_all_bids(self):
        all_bids = self.bid_space.get_all_bids()
        print(all_bids)


    def test_get_all_bids_utility(self):
        self.bid_space.get_all_bids_utility()

    def test_get_sorted_all_bids_with_utility(self):
        self.bid_space.get_sorted_all_bids_with_utility()

    # def test_get_best_bid(self):
    #     print(self.bid_space.get_best_bid())
    #
    # def test_get_worst_bid(self):
    #     print(self.bid_space.get_worst_bid())

    # def test_get_number_of_bids(self):
    #     print(self.bid_space.get_number_of_bids())


if __name__ == '__main__':
    unittest.main()