from abc import abstractmethod

from core.Offer import Offer
from core.UserInterface import UserInterface
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace


class AbstractUser(UserInterface):

    def __init__(self, preference: Preference, bothering: float):
        """
        this class simulate the real user
        :param preference: real preference
        :param bothering: amount of bothering per one asking question
        """
        if not isinstance(preference, Preference):
            raise TypeError('preference argument must be an instance of Preference')
        if not isinstance(bothering, float):
            raise TypeError('bothering argument must be a float')
        self.__bothering = bothering
        self.__preference = preference
        self.__utility_space = UtilitySpace(preference)
        self.__total_bothering = 0.0

    def get_bothering(self):
        """
        this method returns (first) bothering amount (e.g. 0.1 for first question)
        :return: bothering
        """
        return self.__bothering

    def set_total_bothering(self, new_total_bothering):
        self.__total_bothering = new_total_bothering

    def get_preference(self):
        return self.__preference

    def get_utility_space(self):
        return self.__utility_space

    def get_total_bothering(self):
        """
        this method returns total bothering amount for all question till now
        :return: total bothering
        """
        return self.__total_bothering

    @abstractmethod
    def update_total_bothering(self) -> float:
        """
        this method updates total bothering amount
        :return: new total bothering amount
        """
        raise NotImplementedError()

    @abstractmethod
    def get_initial_bids_rank(self) -> list:
        """This method returns list of ranked bids in uncertain situation.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_initial_preference(self) -> Preference:
        """This method returns initial preference in certain situation.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_offer_rank(self, offer: Offer) -> list:
        """This method returns a list of bids that exist special bid which has been sent
        to it.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, offer: Offer) -> float:
        """This method returns exact utility of an offer
        """
        raise NotImplementedError()
