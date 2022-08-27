from core.BiddingStrategyInterface import BiddingStrategyInterface
from abc import abstractmethod
from core.Bid import Bid
from core.OpponentModelInterface import OpponentModelInterface
from core.TimeLine import TimeLine
from core.Preference import Preference
import random


class AbstractBiddingStrategy(BiddingStrategyInterface):

    def __init__(self, opponent_model: OpponentModelInterface, preference: Preference):
        if not isinstance(opponent_model, OpponentModelInterface):
            raise TypeError('opponent_model argument must be an instance of OpponentModelInterface')
        if not isinstance(preference, Preference):
            raise TypeError('preference argument must be an instance of Preference')

        self.__opponent_model = opponent_model
        self.__preference = preference

    @abstractmethod
    def send_bid(self, timeline: TimeLine) -> Bid:
        raise NotImplementedError()

    def get_opponent_model(self):
        return self.__opponent_model

    def get_preference(self):
        return self.__preference

    def generate_random_bid(self):
        issue_items = {}
        preference_data_structure = self.get_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':
                issue_item = list((preference_data_structure[issue][1]).keys())
                issue_items[issue] = random.choice(issue_item)

        bid = Bid(issue_items)
        return bid