from core.AbstractOpponentModel import AbstractOpponentModel
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.Preference import Preference
from core.Offer import Offer
from core.Bid import Bid


class DefaultOpponentModel(AbstractOpponentModel):

    def __init__(self, preference: Preference):
        super(DefaultOpponentModel, self).__init__(preference=preference)
        self.__utility_space = AdditiveUtilitySpace(preference=preference)

    def update_preference(self, offer: Offer) -> Preference:
        return self.get_preference()

    def get_utility(self, bid: Bid):
        return self.__utility_space.get_utility(bid)

    def get_utility_distinct(self, offer: Offer):
        return self.__utility_space.get_utility_distinct(offer)

    def get_name(self) -> str:
        return "DefaultOpponentModel"
