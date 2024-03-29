#######################################################
#
# UserModel.py
# Python implementation of the Interface UserModelInterface
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: Arash Ebrahimnezhad
#
#######################################################
from core.Preference import Preference
from abc import ABC, abstractmethod
from core.Offer import Offer
from core.Bid import Bid


class UserModelInterface(ABC):

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
    def get_must_be_asked_offers(self) -> list:
        raise NotImplementedError()

    @abstractmethod
    def set_must_be_asked_offers(self, offers: list):
        raise NotImplementedError()

    @abstractmethod
    def get_preference(self):
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        """
        this method must return the name of user_model
        :return: the name of user_model
        """
        raise NotImplementedError()

    @abstractmethod
    def set_initial_preference(self, initial_preference: Preference):
        raise NotImplementedError()