from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.BOAParty import BOAParty


class RandomPartyBOA2(BOAParty):
    """
    Bilateral Random Agent (Using BOA framework)

    opponent_model="DefaultOpponentModel",
    bidding_strategy="RandomStrategy",
    acceptance_strategy="ACReject"
    """

    def __init__(self, utility_space: AbstractUtilitySpace):
        super().__init__(utility_space=utility_space,
                         opponent_model="DefaultOpponentModel",
                         bidding_strategy="RandomStrategy",
                         acceptance_strategy="ACReject")

    def get_name(self):
        return 'RandomPartyBOA2'

