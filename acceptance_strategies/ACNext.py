from core.AbstractAcceptanceStrategy import AbstractAcceptanceStrategy
from core.Offer import Offer
from core.OpponentModelInterface import OpponentModelInterface
from core.Bid import Bid


class ACNext(AbstractAcceptanceStrategy):

    def is_acceptable(self, offer: Offer, my_next_bid: Bid, opponent_model: OpponentModelInterface) -> int:
        """this method returns 0 refer to reject opponent's offer or 1 refer to accept
        opponent offer.
        """
        utility = self.get_utility_space().get_utility(offer.get_bid())
        next_utility = self.get_utility_space().get_utility(my_next_bid)
        if utility >= next_utility and utility > 0.7:
            return 1
        return 0