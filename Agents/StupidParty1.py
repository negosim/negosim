from abc import ABC

from core.AbstractNegoParty import AbstractNegoParty
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.Bid import Bid
import random


class StupidParty1(AbstractNegoParty, ABC):

    def send_bid(self) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """

        nego_table = self.get_nego_table()

        utility_space = self.get_utility_space()

        parties = nego_table.get_party_ids()
        opponent_id = list(filter(lambda party: party is not self.get_id(), parties))[0]
        opponent_offer = nego_table.get_party_offers_on_table(opponent_id)

        bid = self.make_random_bid()

        if len(opponent_offer) > 0:
            # print(self.utility_space.get_utility(opponen_offer[len(opponen_offer) - 1].get_bid()), '>=', self.utility_space.get_utility(bid) )
            if utility_space.get_utility(opponent_offer[len(opponent_offer) - 1].get_bid()) >= utility_space.get_utility(bid):
                # print(self.get_name(), opponen_offer[len(opponen_offer) - 1].get_bid().get_issues_items())
                return opponent_offer[len(opponent_offer) - 1].get_bid()
        # print(self.get_name(), bid.get_issues_items())
        return bid

    def make_random_bid(self):
        issue_items = {}
        preference_data_structure = self.get_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':
                issue_item = list((preference_data_structure[issue][1]).keys())
                issue_items[issue] = random.choice(issue_item)

        bid = Bid(issue_items)
        return bid

    def get_name(self):
        return 'Stupid1'

    def get_opponent_model(self):
        """
        :return: opponent model
        """
        return None

    def get_user_model(self):
        """
        :return: user model
        """
        return None