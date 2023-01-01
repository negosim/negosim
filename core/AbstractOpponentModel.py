from core.OpponentModelInterface import OpponentModelInterface
from core.Preference import Preference
from core.Offer import Offer
from core.Bid import Bid
from abc import ABC, abstractmethod
import copy


class AbstractOpponentModel(OpponentModelInterface):

    def __init__(self, preference: Preference = None):
        """
        opponent model needs an initial preference (an initial preference is the preference that the weights are equal
        to 1/n and all evaluation of values are 1)
        :param preference: an initial preference
        """
        if not isinstance(preference, Preference) and preference is not None:
            raise TypeError('preference must be an instance of Preference or None')
        self.__preference = None
        if preference is not None:
            self.__preference = copy.copy(preference)
            self.__preference_data_structure = self.__preference.get_preference_data_structure()
            for issue in self.__preference_data_structure:
                if issue != 'discount_factor' and issue != 'reservation':  # don't count in discount_factor and reservation
                    t = 0
                    if 'discount_factor' in self.__preference_data_structure:
                        t += 1
                    if 'reservation' in self.__preference_data_structure:
                        t += 1
                    self.__preference_data_structure[issue][0] = 1.0 / (len(self.__preference_data_structure) - t)
                    for key in self.__preference_data_structure[issue][1]:
                        self.__preference_data_structure[issue][1][key] = 1

    def set_preference(self, preference: Preference):
        if not isinstance(preference, Preference):
            raise TypeError("preference must be an instance of Preference")
        # if self.__preference is None:
        self.__preference = copy.copy(preference)
        self.__preference_data_structure = self.__preference.get_preference_data_structure()
        for issue in self.__preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':  # don't count in discount_factor and reservation
                t = 0
                if 'discount_factor' in self.__preference_data_structure:
                    t += 1
                if 'reservation' in self.__preference_data_structure:
                    t += 1
                self.__preference_data_structure[issue][0] = 1.0 / (len(self.__preference_data_structure) - t)
                for key in self.__preference_data_structure[issue][1]:
                    self.__preference_data_structure[issue][1][key] = 1
        # else:
        #     raise ValueError("preference was set before!")

    def get_initial_opponent_preference(self) -> Preference:
        return self.__preference_data_structure

    def get_preference(self) -> Preference:
        return self.__preference

    @abstractmethod
    def update_preference(self, offer: Offer) -> Preference:
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, bid: Bid) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_utility_distinct(self, offer: Offer) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        """
        This method must return the name of opponent model
        :return: the name of opponent model
        """
        raise NotImplementedError()
