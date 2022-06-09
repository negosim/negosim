from core.AbstractBiddingStrategy import AbstractBiddingStrategy
from core.TimeLine import TimeLine
from core.Bid import Bid


class RandomStrategy(AbstractBiddingStrategy):

    def send_bid(self, timeline: TimeLine) -> Bid:
        return self.generate_random_bid()
