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

    def __init__(self, preference: Preference = None):
        if not isinstance(preference, Preference) and preference is not None:
            raise TypeError('preference argument must be an instance of Preference or None')
        self.__preference = preference

    def set_preference(self, preference: Preference):
        if not isinstance(preference, Preference):
            raise TypeError("preference must be an instance of Preference")
        if preference is None:
            self.__preference = preference
        else:
            raise ValueError("preference was set before!")

    def get_preference(self) -> Preference:
        return self.__preference

    def get_discount_factor(self):
        '''
        :return: discount_factor
        '''
        if self.__preference is not None:
            return self.__preference.get_discount_factor()
        else:
            raise ValueError("preference is None!")

    def get_reservation(self):
        '''
        :return: reservation
        '''
        if self.__preference is not None:
            return self.__preference.get_reservation()
        else:
            raise ValueError("preference is None!")

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
