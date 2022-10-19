from abc import ABC, abstractmethod, abstractclassmethod
from core.Preference import Preference
from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.ProtocolInterface import ProtocolInterface
from core.Bid import Bid
from core.BidSpace import BidSpace
import random


class AbstractNegoParty(ABC):

    def __init__(self, utility_space: AbstractUtilitySpace):
        self.__preference = utility_space.get_preference()
        self.__utility_space = utility_space
        self.__bid_space = BidSpace(self.__preference)
        # self.opponent_model = None

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

    @abstractmethod
    def send_bid(self, protocol: ProtocolInterface) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        raise NotImplementedError()

    @abstractmethod
    def get_name(self):
        """
        :return: Party Name
        """
        raise NotImplementedError()

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
