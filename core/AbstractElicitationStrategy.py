from abc import ABC, abstractmethod
from core.ElicitationStrategyInterface import ElicitationStrategyInterface
from core.UserInterface import UserInterface
from core.Offer import Offer
from core.StateInfo import StateInfo
from core.UserModelInterface import UserModelInterface


class AbstractElicitationStrategy(ElicitationStrategyInterface):

    def __init__(self, user: UserInterface, user_model: UserModelInterface):
        if not isinstance(user, UserInterface):
            raise TypeError('user argument must be an instance of UserInterface')
        if not isinstance(user_model, UserModelInterface):
            raise TypeError('user_model argument must be an instance of UserModelInterface')
        self.__user = user
        self.__user_model = user_model
        self.__initial_ranked_bids = None
        self.__ranked_bids = None
        self.__initial_preference = None
        self.__preference = None

    # def set_user_model(self, user_model: UserModelInterface):
    #     if not isinstance(user_model, UserModelInterface):
    #         raise TypeError('user_model argument must be an instance of UserModelInterface')
    #     self.__user_model = user_model

    def get_user_model(self) -> UserModelInterface:
        return self.__user_model

    def get_initial_ranked_bids(self) -> list:
        return self.__initial_ranked_bids

    def get_ranked_bids(self) -> list:
        return self.__ranked_bids

    def get_initial_preference(self):
        return self.__initial_preference

    def get_preference(self):
        return self.__preference

    def ask_initial_ranked_bids_from_user(self):
        self.__initial_ranked_bids = self.__user.get_initial_bids_rank()
        self.__ranked_bids = self.__initial_ranked_bids.copy()
        return self.__initial_ranked_bids

    def ask_initial_preference_from_user(self):
        self.__initial_preference = self.__user.get_initial_preference()
        self.__preference = self.__initial_preference.__copy__()
        return self.__initial_preference

    @abstractmethod
    def is_asking_time_from_user(self, state_info: StateInfo):
        """
        This method decides about when and which bid elicit from user
        :param state_info:
        Cal ask_offer_rank_from_user method
        """
        raise NotImplementedError()

    def ask_offer_rank_from_user(self, offer: Offer) -> list:
        """This method returns a list of ranked bids
        """
        self.__ranked_bids = self.__user.get_offer_rank(offer=offer)
        return self.__ranked_bids

    def ask_offer_utility_from_user(self, offer: Offer) -> float:
        return self.__user.get_utility(offer=offer)

    def get_user(self) -> UserInterface:
        return self.__user
