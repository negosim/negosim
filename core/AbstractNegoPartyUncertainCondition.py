from abc import ABC, abstractmethod
from core.Preference import Preference
from core.NegoTable import NegoTable
from core.Bid import Bid
from core.BidSpace import BidSpace
from core.UserInterface import UserInterface
import random
from core.Preference import Preference


class AbstractNegoPartyUncertainCondition(ABC):

    def __init__(self, nego_table: NegoTable, preference: Preference = None, user: UserInterface = None):
        """
        :param nego_table:
        :param preference: initial preferences with equal weights and values
        :param user:
        """
        if not isinstance(nego_table, NegoTable):
            raise TypeError("nego_table must be an instance of NegoTable")
        if not isinstance(preference, Preference) and preference is not None:
            raise TypeError("preference must be an instance of Preference or None")
        if not isinstance(user, UserInterface) and user is not None:
            raise TypeError("user must be an instance of UserInterface or None")

        self.__nego_table = nego_table
        self.__preference = preference

        self.__initial_preference = None
        if preference is not None:
            self.__initial_preference = self.__preference.__copy__()

        self.__user = user

        self.__bid_space = None
        if preference is not None:
            self.__bid_space = BidSpace(self.__initial_preference)

    def get_p(self):
        """
        an uncertain agent needs an initial preference
        (an initial preference is the preference with weights equal to 1/n and evaluation of value is equal to 1)
        this method returns None if the initial preference was not set and returns the initial preference if it was set
        :return: None if the initial preference was not set | returns the initial preference if it was set
        """
        return self.__preference

    def set_preference(self, preference: Preference):
        if self.__preference is None:
            self.__preference = preference
            self.__initial_preference = self.__preference.__copy__()

    def set_user(self, user):
        # if self.__user is None:
        self.__user = user
        # else:
        #     raise ValueError("user was not set!")

    def get_user(self) -> UserInterface:
        return self.__user

    def get_initial_preference(self):
        if self.__initial_preference is not None:
            return self.__initial_preference
        else:
            if self.__preference is not None:
                self.__initial_preference = self.__preference.__copy__()
                return self.__initial_preference
            else:
                raise ValueError("the preference was not set!")

    # def get_utility_space(self):
    #     return self.__utility_space

    def get_bid_space(self) -> BidSpace:
        if self.__bid_space is not None:
            return self.__bid_space
        else:
            if self.__preference is not None:
                self.__bid_space = BidSpace(self.__initial_preference)
                return self.__bid_space
            else:
                raise ValueError("the preference was not set!")

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
