from abc import ABC

from core.AbstractNegoParty import AbstractNegoParty
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.Bid import Bid
import random


class StupidParty1(AbstractNegoParty, ABC):

    def send_bid(self, protocol) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        utility_space = self.get_utility_space()

        parties = protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponent_offer = protocol.get_offers_on_table(opponent)

        def make_random_bid():
            issue_item = {}
            for issue, item_value in self.get_preference().get_preference_data_structure().items():
                issue_item[issue] = random.choice(list(item_value[1]))
            bid1 = Bid(issue_item)
            return bid1

        bid = make_random_bid()
        if len(opponent_offer) > 0:
            # print(self.utility_space.get_utility(opponen_offer[len(opponen_offer) - 1].get_bid()), '>=', self.utility_space.get_utility(bid) )
            if utility_space.get_utility(opponent_offer[len(opponent_offer) - 1].get_bid()) >= utility_space.get_utility(bid):
                # print(self.get_name(), opponen_offer[len(opponen_offer) - 1].get_bid().get_issues_items())
                return opponent_offer[len(opponent_offer) - 1].get_bid()
        # print(self.get_name(), bid.get_issues_items())
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