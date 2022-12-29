from abc import ABC
from core.EUBOAParty import EUBOAParty
from core.Preference import Preference
from core.UserInterface import UserInterface


class RandomAgentEUBOA2(EUBOAParty, ABC):

    def __init__(self, preference: Preference, user: UserInterface):
        super(RandomAgentEUBOA2, self).__init__(preference=preference, user=user,
                                                user_model="DefaultUserModel",
                                                elicitation_strategy="DefaultElicitationStrategy",
                                                opponent_model="DefaultOpponentModel",
                                                bidding_strategy="RandomStrategy",
                                                acceptance_strategy="ACNext")

    def get_name(self):
        return "RandomAgentEUBOA2"