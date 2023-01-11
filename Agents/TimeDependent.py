from core.Preference import Preference
from core.AbstractNegoParty import AbstractNegoParty
from core.Bid import Bid
from core.Offer import Offer
from core.AbstractUtilitySpace import AbstractUtilitySpace


class TimeDependent(AbstractNegoParty):
    """
    Bilateral TimeDependent Agent (linear conceder)
    """

    def __init__(self, utility_space: AbstractUtilitySpace):
        super().__init__(utility_space=utility_space)
        self.__utility_space = utility_space
        self.__p_min = 0.0
        self.__p_max = 1.0
        self.__k = 0.0
        self.__e = 1.0

    def send_bid(self) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        nego_table = self.get_nego_table()
        parties = nego_table.get_party_ids()
        opponent_id = list(filter(lambda party: party is not self, parties))[0]
        opponent_offer = nego_table.get_party_offers_on_table(opponent_id)

        t = nego_table.get_time()

        target_utility = self.get_target_utility(p_min=self.__p_min, p_max=self.__p_max, t=t, k=self.__k, e=self.__e)
        count = 500
        bid = None
        while count > 0:
            bid = self.generate_random_bid()
            if self.__utility_space.get_utility_distinct(Offer(bid=bid, time=t)) >= target_utility:
                break
            count -= 1
            bid = None

        if bid is None:
            bid = self.get_preference().get_best_bid()

        if len(opponent_offer) > 0:
            op_bid = opponent_offer[len(opponent_offer) - 1].get_bid()
            if self.__utility_space.get_utility(op_bid) >= self.__utility_space.get_utility(
                    bid) and self.__utility_space.get_utility(op_bid) > 0.7:
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
