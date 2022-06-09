from abc import abstractmethod
from core.UserModelInterface import UserModelInterface
from core.Preference import Preference
from core.Offer import Offer


class AbstractUserModel(UserModelInterface):

    def __init__(self, initial_preference: Preference):
        if not isinstance(initial_preference, Preference):
            raise TypeError('initial_preference must be instance of Preference class')
        self.__initial_preference = initial_preference
        self.__preference = initial_preference
        self.__must_be_asked_offers = []  # user model can ask one or more than one bid

    @abstractmethod
    def generate_initial_preference(self, initial_ranked_bids) -> Preference:
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, offer: Offer) -> float:
        raise NotImplementedError()

    @abstractmethod
    def update_preference(self, ranked_bids: list) -> Preference:
        raise NotImplementedError()

    def get_must_be_asked_offers(self) -> list:
        return self.__must_be_asked_offers

    def set_must_be_asked_offers(self, offers: list):
        self.__must_be_asked_offers = offers

    def get_preference(self):
        return self.__preference

    def get_initial_preference(self):
        return self.__initial_preference



