from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.Offer import Offer
from abc import abstractmethod
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.OpponentModelInterface import OpponentModelInterface
from core.Bid import Bid


class AbstractAcceptanceStrategy(AcceptanceStrategyInterface):

    def __init__(self, utility_space: AdditiveUtilitySpace):
        if not isinstance(utility_space, AdditiveUtilitySpace):
            raise TypeError('utility_space argument must be an instance of AdditiveUtilitySpace')
        self.__utility_space = utility_space

    @abstractmethod
    def is_acceptable(self, offer: Offer, my_next_bid: Bid, opponent_model: OpponentModelInterface) -> int:
        """this method returns 0 refer to reject opponent's offer or 1 refer to accept
        opponent offer.
        """
        raise NotImplementedError()

    def get_utility_space(self):
        return self.__utility_space
