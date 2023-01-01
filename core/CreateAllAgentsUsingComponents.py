from core.EUBOAParty import EUBOAParty
from core.Preference import Preference
from core.UserInterface import UserInterface


class CreateAllAgentsUsingComponents:
    def __init__(self,
                 elicitation_strategies: list,
                 user_models: list,
                 bidding_strategies: list,
                 opponent_models: list,
                 acceptance_strategies: list):

        self.__elicitation_strategies = elicitation_strategies
        self.__user_models = user_models
        self.__bidding_strategies = bidding_strategies
        self.__opponent_models = opponent_models
        self.__acceptance_strategies = acceptance_strategies
        # self.__preference = preferences
        # self.__users = users

        if len(self.__elicitation_strategies) == 0:
            raise TypeError("Please select at least one elicitation strategy")
        if len(self.__user_models) == 0:
            raise TypeError("Please select at least one user models")
        if len(self.__bidding_strategies) == 0:
            raise TypeError("Please select at least one bidding strategies")
        if len(self.__opponent_models) == 0:
            raise TypeError("Please select at least one opponent models")
        if len(self.__acceptance_strategies) == 0:
            raise TypeError("Please select at least one acceptance strategies")

    def create_agents(self) -> list:
        euboa_parties = []
        # for preference in self.__preference:
        #     for user in self.__users:
        for e in self.__elicitation_strategies:
            for u in self.__user_models:
                for b in self.__bidding_strategies:
                    for o in self.__opponent_models:
                        for a in self.__acceptance_strategies:
                            euboa_party = AgentEUBOA(preference=None, user=None,
                                                     user_model=u,
                                                     elicitation_strategy=e,
                                                     opponent_model=o,
                                                     bidding_strategy=b,
                                                     acceptance_strategy=a)
                            euboa_parties.append(euboa_party)
        return euboa_parties


class AgentEUBOA(EUBOAParty):

    def __init__(self,
                 user_model: str,
                 elicitation_strategy: str,
                 opponent_model: str,
                 bidding_strategy: str,
                 acceptance_strategy: str, preference: Preference = None, user: UserInterface = None):
        super(AgentEUBOA, self).__init__(preference=preference, user=user,
                                         user_model=user_model,
                                         elicitation_strategy=elicitation_strategy,
                                         opponent_model=opponent_model,
                                         bidding_strategy=bidding_strategy,
                                         acceptance_strategy=acceptance_strategy)
        self.__party_name = "(" + elicitation_strategy + "_" + user_model + "_" + bidding_strategy + "_" + opponent_model + "_" + acceptance_strategy + ")"

    def get_name(self):
        return self.__party_name
