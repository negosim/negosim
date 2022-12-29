from abc import ABC
from core.EUBOAParty import EUBOAParty
from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.UserInterface import UserInterface


class RandomAgentEUBOA2(EUBOAParty, ABC):

    def __init__(self, utility_space: AbstractUtilitySpace, user: UserInterface):
        super(RandomAgentEUBOA2, self).__init__(utility_space=utility_space, user=user,
                                                user_model="DefaultUserModel",
                                                elicitation_strategy="DefaultElicitationStrategy",
                                                opponent_model="DefaultOpponentModel",
                                                bidding_strategy="RandomStrategy",
                                                acceptance_strategy="ACNext")

    def get_name(self):
        return "RandomAgentEUBOA2"