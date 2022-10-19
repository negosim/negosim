#######################################################
#
# AbstractUtilitySpace.py
# Python implementation of the Class AdditiveUtilitySpace
# Created on:
# Original author: Arash Ebrahimnezhad
#
#######################################################
from abc import ABC, abstractmethod

from core.Bid import Bid
from core.Offer import Offer
from core.Preference import Preference


class AbstractUtilitySpace(ABC):

    def __init__(self, preference: Preference):
        if not isinstance(preference, Preference):
            raise TypeError('preference argument must be an instance of Preference')
        self.__preference = preference

    def get_preference(self) -> Preference:
        return self.__preference

    def get_discount_factor(self):
        '''
        :return: discount_factor
        '''
        return self.__preference.get_discount_factor()

    def get_reservation(self):
        '''
        :return: reservation
        '''
        return self.__preference.get_reservation()

    @abstractmethod
    def get_utility(self, bid: Bid) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_utility_distinct(self, offer: Offer) -> float:
        """
        If there is time pressure
        :param offer:
        :return: distinct utility (a float number between [0, 1]
        """
        raise NotImplementedError
