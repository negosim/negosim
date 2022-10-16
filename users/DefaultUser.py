from core.Offer import Offer
from core.Preference import Preference
from core.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.AbstractUser import AbstractUser
from core.BidSpace import BidSpace
import math
import random

PERCENT = 0.1  # Initial percent of ranked bids
BOTHERING = 0.1


class DefaultUser(AbstractUser):
    """
    DefaultUser returns 10 percent bids as ordered bids
    which exists minimum and maximum bids
    """

    def __init__(self, preference: Preference):
        super().__init__(preference, bothering=BOTHERING)
        self.__sorted_bids = []
        self.__utility_space = self.get_utility_space()

    def get_initial_bids_rank(self) -> list:
        """This method returns list of ranked bids in uncertain situation.
        """

        bid_space = BidSpace(self.get_preference())
        num_of_bids = bid_space.get_number_of_bids()
        ten_percent = math.ceil(num_of_bids * PERCENT)

        all_bids = bid_space.get_all_bids()

        self.__sorted_bids.append(bid_space.get_best_bid())
        for i in range(ten_percent - 2):
            random_bid = random.choice(all_bids)
            while random_bid in self.__sorted_bids:
                random_bid = random.choice(all_bids)
            self.__sorted_bids.append(random_bid)
        self.__sorted_bids.append(bid_space.get_worst_bid())

        self.__sorted_bids.sort(key=lambda bid: self.__utility_space.get_utility(bid))

        return self.__sorted_bids

    def get_initial_preference(self):
        """This method returns initial preference in certain situation.
        """
        return None

    def get_offer_rank(self, offer: Offer) -> list:
        """This method returns a list of bids that exist special bid which has been sent
        to it.
        """
        bid = offer.get_bid()
        if not bid in self.__sorted_bids:
            self.__sorted_bids.append(bid)
            self.__sorted_bids.sort(key=lambda bid: self.__utility_space.get_utility(bid))
        return self.__sorted_bids

    def get_utility(self, offer: Offer) -> float:
        """This method should returns exact utility of an offer
        but DefaultUser instead of returning exact utility returns -1.0
        """
        # utility_space = AdditiveUtilitySpace(self.preference)
        # return utility_space.get_utility(offer.get_bid())
        return -1.0

    def update_total_bothering(self) -> float:
        """
        this method updates total bothering amount
        :return: new total bothering amount
        """
        new_total_bothering = self.get_total_bothering() + self.get_bothering()
        self.set_total_bothering(new_total_bothering)