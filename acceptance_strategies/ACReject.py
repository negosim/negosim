from core.AbstractAcceptanceStrategy import AbstractAcceptanceStrategy
from core.Offer import Offer
from core.OpponentModelInterface import OpponentModelInterface
from core.Bid import Bid


class ACReject(AbstractAcceptanceStrategy):

    def is_acceptable(self, offer: Offer, my_next_bid: Bid, opponent_model: OpponentModelInterface) -> int:
        """this method can return either 0 refer to reject opponent's offer or 1 refer to accept
        opponent offer.
        AC_reject always rejects opponent offer
        """
        return 0

    def get_name(self) -> str:
        return "ACReject"
