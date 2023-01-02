from core.BOAParty import BOAParty
from core.AbstractUtilitySpace import AbstractUtilitySpace


class CreateAllAgentsUsingBOAComponents:
    def __init__(self,
                 bidding_strategies: list,
                 opponent_models: list,
                 acceptance_strategies: list):

        self.__bidding_strategies = bidding_strategies
        self.__opponent_models = opponent_models
        self.__acceptance_strategies = acceptance_strategies

        if len(self.__bidding_strategies) == 0:
            raise TypeError("Please select at least one bidding strategies")
        if len(self.__opponent_models) == 0:
            raise TypeError("Please select at least one opponent models")
        if len(self.__acceptance_strategies) == 0:
            raise TypeError("Please select at least one acceptance strategies")

    def create_agents(self) -> list:
        boa_parties = []
        for b in self.__bidding_strategies:
            for o in self.__opponent_models:
                for a in self.__acceptance_strategies:
                    boa_party = AgentBOA(opponent_model=o,
                                         bidding_strategy=b,
                                         acceptance_strategy=a,
                                         utility_space=None)
                    boa_parties.append(boa_party)
        return boa_parties


class AgentBOA(BOAParty):

    def __init__(self,
                 opponent_model: str,
                 bidding_strategy: str,
                 acceptance_strategy: str,
                 utility_space: AbstractUtilitySpace = None):
        super(AgentBOA, self).__init__(opponent_model=opponent_model,
                                       bidding_strategy=bidding_strategy,
                                       acceptance_strategy=acceptance_strategy,
                                       utility_space=utility_space)
        self.__party_name = "(" + bidding_strategy + "_" + opponent_model + "_" + acceptance_strategy + ")"

    def get_name(self):
        return self.__party_name
