from abc import abstractmethod
from core.UserModelInterface import UserModelInterface
from core.Preference import Preference
from core.Offer import Offer
from core.Bid import Bid


class AbstractUserModel(UserModelInterface):

    def __init__(self, initial_preference: Preference = None):
        if not isinstance(initial_preference, Preference) and initial_preference is not None:
            raise TypeError('initial_preference must be instance of Preference class or None')
        # if initial_preference is not None:
        self.__initial_preference = initial_preference
        self.__preference = initial_preference
        self.__must_be_asked_offers = []  # user model can ask one or more than one bid

    def set_initial_preference(self, initial_preference: Preference):
        if not isinstance(initial_preference, Preference):
            raise TypeError('initial_preference must be instance of Preference class')
        # if self.__initial_preference is None:
        self.__initial_preference = initial_preference
        self.__preference = initial_preference
        # else:
        #     raise ValueError("initial_preference was set before!")

    @abstractmethod
    def generate_initial_preference(self, initial_ranked_bids) -> Preference:
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, bid: Bid) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_utility_distinct(self, offer: Offer) -> float:
        raise NotImplementedError()

    @abstractmethod
    def update_preference(self, ranked_bids: list) -> Preference:
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        """
        this method must return the name of user_model
        :return: the name of user_model
        """
        raise NotImplementedError()

    def get_must_be_asked_offers(self) -> list:
        return self.__must_be_asked_offers

    def set_must_be_asked_offers(self, offers: list):
        self.__must_be_asked_offers = offers

    def get_preference(self):
        return self.__preference

    def get_initial_preference(self):
        return self.__initial_preference



