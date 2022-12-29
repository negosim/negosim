from abc import ABC, abstractmethod
from core.Preference import Preference
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.Bid import Bid
from core.BidSpace import BidSpace
from core.UserInterface import UserInterface
import random
from core.Preference import Preference


class AbstractNegoPartyUncertainCondition(ABC):

    def __init__(self, preference: Preference, user: UserInterface):
        self.__preference = preference
        self.__initial_preference = self.__preference.__copy__()
        self.__user = user
        self.__bid_space = BidSpace(self.__initial_preference)

    def get_user(self) -> UserInterface:
        return self.__user

    def get_initial_preference(self):
        return self.__initial_preference

    # def get_utility_space(self):
    #     return self.__utility_space

    def get_bid_space(self) -> BidSpace:
        return self.__bid_space

    # def get_opponent_model(self):
    #     return self.opponent_model

    def generate_random_bid(self):
        issue_items = {}
        preference_data_structure = self.get_initial_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':
                issue_item = list((preference_data_structure[issue][1]).keys())
                issue_items[issue] = random.choice(issue_item)

        bid = Bid(issue_items)
        return bid

    @abstractmethod
    def send_bid(self, protocol) -> Bid:
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

    @abstractmethod
    def get_preference(self):
        raise NotImplementedError()