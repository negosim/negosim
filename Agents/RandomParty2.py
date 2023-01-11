from core.AbstractNegoParty import AbstractNegoParty
from core.Bid import Bid


class RandomParty2(AbstractNegoParty):
    """
    Bilateral Random Agent
    """

    def send_bid(self) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """

        nego_table = self.get_nego_table()

        utility_space = self.get_utility_space()



        parties = nego_table.get_party_ids()
        opponent_id = list(filter(lambda party: party is not self.get_id(), parties))[0]
        opponent_offer = nego_table.get_party_offers_on_table(opponent_id)

        bid = self.generate_random_bid()
        if len(opponent_offer) > 0:
            op_bid = opponent_offer[len(opponent_offer) - 1].get_bid()
            if utility_space.get_utility(op_bid) >= utility_space.get_utility(
                    bid) and utility_space.get_utility(op_bid) > 0.7:
                return op_bid
        return bid

    def get_name(self):
        return 'Random1'

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
