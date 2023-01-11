from abc import abstractmethod

from core.AbstractNegoParty import AbstractNegoParty
from core.AbstractUtilitySpace import AbstractUtilitySpace
from configurations import *
import CreateObjectByPath
from core.Bid import Bid
from core.OpponentModelInterface import OpponentModelInterface
from core.BiddingStrategyInterface import BiddingStrategyInterface
from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.NegoTable import NegoTable


class BOAParty(AbstractNegoParty):
    def __init__(self,
                 opponent_model: str,
                 bidding_strategy: str,
                 acceptance_strategy: str,
                 utility_space: AbstractUtilitySpace = None):
        super().__init__(utility_space=utility_space)

        if utility_space is not None:
            preference = utility_space.get_preference()
            self.initial_preference_opponent_model = preference.get_initial_preference()
            self.__opponent_model: OpponentModelInterface = CreateObjectByPath.get_object(OPPONENT_MODEL_PATH, opponent_model, self.initial_preference_opponent_model)
            self.__bidding_strategy: BiddingStrategyInterface = CreateObjectByPath.get_object(BIDDING_STRATEGIES_PATH, bidding_strategy, self.__opponent_model, utility_space, None)
            self.__acceptance_strategy: AcceptanceStrategyInterface = CreateObjectByPath.get_object(ACCEPTANCE_STRATEGIES_PATH, acceptance_strategy, utility_space, None)
        else:
            preference = None
            self.initial_preference_opponent_model = None
            self.__opponent_model: OpponentModelInterface = CreateObjectByPath.get_object(OPPONENT_MODEL_PATH, opponent_model, self.initial_preference_opponent_model)
            self.__bidding_strategy: BiddingStrategyInterface = CreateObjectByPath.get_object(BIDDING_STRATEGIES_PATH, bidding_strategy, self.__opponent_model, utility_space, None)
            self.__acceptance_strategy: AcceptanceStrategyInterface = CreateObjectByPath.get_object(ACCEPTANCE_STRATEGIES_PATH, acceptance_strategy, utility_space, None)


    def send_bid(self) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        nego_table: NegoTable = self.get_nego_table()

        parties = nego_table.get_party_ids()
        opponent_id = list(filter(lambda party: party is not self.get_id(), parties))[0]
        opponent_offers = nego_table.get_party_offers_on_table(opponent_id)
        timeline = nego_table.get_time_line()
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

    def get_user_model(self):
        """
        :return: user model
        """
        return None

    def get_bidding_strategy(self) -> BiddingStrategyInterface:
        return self.__bidding_strategy

    def get_opponent_model(self) -> OpponentModelInterface:
        """
        :return: opponent model
        """
        return self.__opponent_model

    def get_acceptance_strategy(self) -> AcceptanceStrategyInterface:
        return self.__acceptance_strategy

    def get_preference(self):
        return self.__bidding_strategy.get_preference()

    def get_utility_space(self) -> AbstractUtilitySpace:
        return self.__bidding_strategy.get_utility_space()