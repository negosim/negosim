import unittest
from core.Preference import Preference
from users.DefaultUser import DefaultUser
from core.BidSpace import BidSpace
import random
from core.Offer import Offer
from core.AdditiveUtilitySpace import AdditiveUtilitySpace


class TestDefaultUser(unittest.TestCase):

    def setUp(self) -> None:
        self.preference = Preference('laptop', 'laptop_buyer_utility.xml')
        self.u_space = AdditiveUtilitySpace(self.preference)
        self.user = DefaultUser(self.preference)

    def test_get_initial_bids_rank(self):
        self.user.get_initial_bids_rank()

    def test_get_offer_rank(self):
        sorted_bids = self.user.get_initial_bids_rank()
        bid_space = BidSpace(self.preference)
        bids = bid_space.get_all_bids()
        bid = random.choice(bids)
        while bid in sorted_bids:
            bid = random.choice(bids)
        offer = Offer(bid=bid, time=0.1)

        sorted_bids2 = self.user.get_offer_rank(offer=offer)
        print(sorted_bids2)
        for b in sorted_bids2:
            print(self.u_space.get_utility(b))



if __name__ == '__main__':
    unittest.main()
