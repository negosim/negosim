from abc import abstractmethod

from core.AbstractNegoParty import AbstractNegoParty
from core.AbstractUtilitySpace import AbstractUtilitySpace
from configurations import *
import CreateObjectByPath
from core.Bid import Bid


class BOAParty(AbstractNegoParty):
    def __init__(self, utility_space: AbstractUtilitySpace,
                 opponent_model: str,
                 bidding_strategy: str,
                 acceptance_strategy: str):
        super().__init__(utility_space=utility_space)

        preference = utility_space.get_preference()
        self.initial_preference_opponent_model = preference.get_initial_preference()
        self.__opponent_model = CreateObjectByPath.get_object(OPPONENT_MODEL_PATH, opponent_model,
                                                              self.initial_preference_opponent_model)
        self.__bidding_strategy = CreateObjectByPath.get_object(BIDDING_STRATEGIES_PATH, bidding_strategy,
                                                                self.__opponent_model, utility_space, None)
        self.__acceptance_strategy = CreateObjectByPath.get_object(ACCEPTANCE_STRATEGIES_PATH, acceptance_strategy,
                                                                   utility_space, None)

    def send_bid(self, protocol) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        parties = protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponent_offers = protocol.get_offers_on_table(opponent)
        timeline = protocol.get_time_line()
        bid = self.__bidding_strategy.send_bid(timeline)
        if len(opponent_offers) > 0:
            op_offer = opponent_offers[len(opponent_offers) - 1]
            self.__opponent_model.update_preference(op_offer)
            if self.__acceptance_strategy.is_acceptable(offer=op_offer, my_next_bid=bid,
                                                        opponent_model=self.__opponent_model):
                return op_offer.get_bid()
        return bid

    @abstractmethod
    def get_name(self):
        """
        :return: Party Name
        """
        raise NotImplementedError()

    def get_opponent_model(self):
        """
        :return: opponent model
        """
        return self.__opponent_model

    def get_user_model(self):
        """
        :return: user model
        """
        return None