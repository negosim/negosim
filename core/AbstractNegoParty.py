from abc import ABC, abstractmethod
from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.NegoTable import NegoTable
from core.Bid import Bid
from core.BidSpace import BidSpace
import random
from core.NegoPartyInterface import NegoPartyInterface


class AbstractNegoParty(NegoPartyInterface, ABC):

    def __init__(self, utility_space: AbstractUtilitySpace = None):
        if not isinstance(utility_space, AbstractUtilitySpace) and utility_space is not None:
            raise TypeError("utility_space must be an instance of AbstractUtilitySpace or None")

        self.__nego_table = None
        self.__preference = None
        self.__utility_space = None
        self.__bid_space = None
        if utility_space is not None:
            self.__preference = utility_space.get_preference()
            self.__utility_space = utility_space
            self.__bid_space = BidSpace(self.__preference)
        self.opponent_model = None

    def set_nego_table(self, nego_table: NegoTable):
        if not isinstance(nego_table, NegoTable):
            raise TypeError("nego_table must be an instance of NegoTable")
        self.__nego_table = nego_table

    def get_nego_table(self):
        return self.__nego_table

    def set_utility_space(self, utility_space: AbstractUtilitySpace):
        if not isinstance(utility_space, AbstractUtilitySpace):
            raise TypeError("utility_space must be an instance of AbstractUtilitySpace")
        self.__preference = utility_space.get_preference()
        self.__utility_space = utility_space
        self.__bid_space = BidSpace(self.__preference)

    def get_preference(self):
        return self.__preference

    def get_utility_space(self):
        return self.__utility_space

    def get_bid_space(self) -> BidSpace:
        return self.__bid_space

    def generate_random_bid(self):
        issue_items = {}
        preference_data_structure = self.get_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':
                issue_item = list((preference_data_structure[issue][1]).keys())
                issue_items[issue] = random.choice(issue_item)

        bid = Bid(issue_items)
        return bid

    def end_negotiation_bid(self):
        return EndNegotiation()

    @abstractmethod
    def send_bid(self) -> Bid:
        """
        send new bid,
        send same bid refer to accept,
        send an instance of EndNegotiation refer to end negotiation
        :return: Bid
        """
        raise NotImplementedError()

    @abstractmethod
    def get_name(self):
        """
        :return: Party Name
        """
        raise NotImplementedError()

    def get_id(self):
        return self.get_name()+str(self)

    @abstractmethod
    def get_opponent_model(self):
        """
        This method can be used for analysing purpose
        if this method returns opponent model this means the
        analysis entity should analyze the opponent model otherwise
        if it returns None means the analysis entity would not analyze
        the opponent modeling
        :return: opponent model
        """
        raise NotImplementedError()

    @abstractmethod
    def get_user_model(self):
        """
        This method can be used for analysing purpose
        if this method returns user model this means the
        analysis entity should analyze the user model otherwise
        if it returns None means the analysis entity would not analyze
        the opponent modeling
        :return: user model
        """
        raise NotImplementedError()


class EndNegotiation(Bid):
    def __init__(self):
        super().__init__({})
