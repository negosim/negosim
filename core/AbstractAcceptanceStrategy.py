from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.Offer import Offer
from abc import abstractmethod
from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.OpponentModelInterface import OpponentModelInterface
from core.Bid import Bid


class AbstractAcceptanceStrategy(AcceptanceStrategyInterface):

    def __init__(self, utility_space: AbstractUtilitySpace):
        if not isinstance(utility_space, AbstractUtilitySpace):
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
