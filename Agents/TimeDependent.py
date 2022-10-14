from core.Preference import Preference
from core.AbstractNegoParty import AbstractNegoParty
from core.Bid import Bid
from core.Offer import Offer
from core.TimeLine import TimeLine


class TimeDependent(AbstractNegoParty):
    """
    Bilateral TimeDependent Agent (linear conceder)
    """

    def __init__(self, preference: Preference):
        AbstractNegoParty.__init__(self, preference)
        self.__p_min = 0.0
        self.__p_max = 1.0
        self.__k = 0.0
        self.__e = 1.0

    def send_bid(self, protocol) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        parties = protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponen_offer = protocol.get_offers_on_table(opponent)

        t = protocol.get_time()

        target_utility = self.get_target_utility(p_min=self.__p_min, p_max=self.__p_max, t=t, k=self.__k, e=self.__e)
        count = 500
        bid = None
        while count > 0:
            bid = self.generate_random_bid()
            if self.get_utility_space().get_utility_distinct(Offer(bid=bid, time=t)) >= target_utility:
                break
            count -= 1
            bid = None

        if bid is None:
            bid = self.get_preference().get_best_bid()

        if len(opponen_offer) > 0:
            op_bid = opponen_offer[len(opponen_offer) - 1].get_bid()
            if self.get_utility_space().get_utility(op_bid) >= self.get_utility_space().get_utility(
                    bid) and self.get_utility_space().get_utility(op_bid) > 0.7:
                return op_bid
        return bid

    def get_target_utility(self, p_min, p_max, t, k, e):
        # u(t) = Pmin + (Pmax − Pmin) · (1 − F(t)),
        # F(t) = k + (1 − k) · t **1/e
        u_t = p_min + (p_max - p_min) * (1 - self.f(t, k, e))
        return u_t

    def f(self, t, k, e):
        return k + (1 - k) * (t ** (1.0 / e))

    def set_values(self, p_min, p_max, k, e):
        self.__p_min = p_min
        self.__p_max = p_max
        self.__k = k
        self.__e = e

    def get_name(self):
        """
        :return: Party Name
        """
        return "Time Dependent"

    def get_opponent_model(self):
        """
        :return: opponent model
        """
        return None

    def get_user_model(self):
        """
        :return: user model
        """
        return None
