from itertools import permutations
import CreateObjectByPath
from core.BilateralSession2 import BilateralSession
from controller import Controller
from configurations import *
from core.Preference import Preference
from core.CreateAllAgentsUsingEUBOAComponents import CreateAllAgentsUsingEUBOAComponents
from core.CreateAllAgentsUsingBOAComponents import CreateAllAgentsUsingBOAComponents
from core.EUBOAParty import EUBOAParty
from core.BOAParty import BOAParty


class BilateralTournament:

    def __init__(self, protocol_name: str, analysis_man_name: str, Tournament_analysis_name: str,
                 deadline: str, deadline_type: str, agent_names: list, opponent_names: list, domain_names: list,
                 tournament_repetition: str, utility_space_names: list,
                 users: list = None,
                 elicitation_strategies: list = None,
                 user_models: list = None,
                 bidding_strategies: list = None,
                 opponent_models: list = None,
                 acceptance_strategies: list = None,
                 EUBOA_is_agent_side: bool = False, EUBOA_is_opponent_side: bool = False,
                 BOA_is_agent_side: bool = False, BOA_is_opponent_side: bool = False):

        # if not (elicitation_strategies is None
        #         and user_models is None
        #         and bidding_strategies is None
        #         and opponent_models is None
        #         and acceptance_strategies is None):
        #     raise ValueError(
        #         "You have to set all EUBOA components to None or select at least one component for each EUBOA "
        #         "components")

        if BOA_is_agent_side or BOA_is_opponent_side:
            if (bidding_strategies is None or len(bidding_strategies) < 1) or (opponent_models is None or len(opponent_models) < 1) or (acceptance_strategies is None or len(acceptance_strategies) < 1):
                raise ValueError("BOA_is_agent_side or BOA_is_opponent_side were set True, So you have to send at "
                                 "least a bidding_strategy and an opponent_models and an acceptance_strategies")
            else:
                self.__all_boa_agents = CreateAllAgentsUsingBOAComponents(bidding_strategies=bidding_strategies,
                                                                          opponent_models=opponent_models,
                                                                          acceptance_strategies=acceptance_strategies).create_agents()


        # if elicitation_strategies is not None:
        #     if len(elicitation_strategies) < 1:
        #         raise ValueError(
        #             "You have to set elicitation_strategies None or a list of strategies with at least size equal "
        #             "to 1")
        #     if len(elicitation_strategies) >= 1:
        #         if user_models is None or len(user_models) < 1:
        #             raise ValueError(
        #                 "You selected an or more elicitation strategies, so you have to set all EUBOA components or "
        #                 "set elicitation_strategies to None")
        #     if len(elicitation_strategies) >= 1:
        #         if bidding_strategies is None or len(bidding_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more elicitation strategies, so you have to set all EUBOA components or "
        #                 "set elicitation_strategies to None")
        #     if len(elicitation_strategies) >= 1:
        #         if opponent_models is None or len(opponent_models) < 1:
        #             raise ValueError(
        #                 "You selected an or more elicitation strategies, so you have to set all EUBOA components or "
        #                 "set elicitation strategies to None")
        #     if len(elicitation_strategies) >= 1:
        #         if acceptance_strategies is None or len(acceptance_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more elicitation strategies, so you have to set all EUBOA components or "
        #                 "set elicitation strategies to None")
        #
        # if user_models is not None:
        #     if len(user_models) < 1:
        #         raise ValueError(
        #             "You have to set user_models None or a list of models with at least size equal "
        #             "to 1")
        #     if len(user_models) >= 1:
        #         if elicitation_strategies is None or len(elicitation_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more user_models, so you have to set all EUBOA components or "
        #                 "set user_models to None")
        #     if len(user_models) >= 1:
        #         if bidding_strategies is None or len(bidding_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more user_models, so you have to set all EUBOA components or "
        #                 "set user_models to None")
        #     if len(user_models) >= 1:
        #         if opponent_models is None or len(opponent_models) < 1:
        #             raise ValueError(
        #                 "You selected an or more user_models, so you have to set all EUBOA components or "
        #                 "set user_models to None")
        #     if len(user_models) >= 1:
        #         if acceptance_strategies is None or len(acceptance_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more user_models, so you have to set all EUBOA components or "
        #                 "set user_models to None")
        #
        # if bidding_strategies is not None:
        #     if len(bidding_strategies) < 1:
        #         raise ValueError(
        #             "You have to set bidding_strategies None or a list of strategies with at least size equal "
        #             "to 1")
        #     if len(bidding_strategies) >= 1:
        #         if elicitation_strategies is None or len(elicitation_strategies) < 1:
        #             raise ValueError(
        #                 "You selected a or more bidding_strategies, so you have to set all EUBOA components or "
        #                 "set bidding_strategies to None")
        #     if len(bidding_strategies) >= 1:
        #         if user_models is None or len(user_models) < 1:
        #             raise ValueError(
        #                 "You selected a or more bidding_strategies, so you have to set all EUBOA components or "
        #                 "set bidding_strategies to None")
        #     if len(bidding_strategies) >= 1:
        #         if opponent_models is None or len(opponent_models) < 1:
        #             raise ValueError(
        #                 "You selected a or more bidding_strategies, so you have to set all EUBOA components or "
        #                 "set bidding_strategies to None")
        #     if len(bidding_strategies) >= 1:
        #         if acceptance_strategies is None or len(acceptance_strategies) < 1:
        #             raise ValueError(
        #                 "You selected a or more bidding_strategies, so you have to set all EUBOA components or "
        #                 "set bidding_strategies to None")
        #
        # if opponent_models is not None:
        #     if len(opponent_models) < 1:
        #         raise ValueError(
        #             "You have to set opponent_models None or a list of models with at least size equal "
        #             "to 1")
        #     if len(opponent_models) >= 1:
        #         if elicitation_strategies is None or len(elicitation_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more opponent_models, so you have to set all EUBOA components or "
        #                 "set opponent_models to None")
        #     if len(opponent_models) >= 1:
        #         if user_models is None or len(user_models) < 1:
        #             raise ValueError(
        #                 "You selected an or more opponent_models, so you have to set all EUBOA components or "
        #                 "set opponent_models to None")
        #     if len(opponent_models) >= 1:
        #         if bidding_strategies is None or len(bidding_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more opponent_models, so you have to set all EUBOA components or "
        #                 "set opponent_models to None")
        #     if len(opponent_models) >= 1:
        #         if acceptance_strategies is None or len(acceptance_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more opponent_models, so you have to set all EUBOA components or "
        #                 "set opponent_models to None")
        #
        # if acceptance_strategies is not None:
        #     if len(acceptance_strategies) < 1:
        #         raise ValueError(
        #             "You have to set acceptance_strategies None or a list of strategies with at least size equal "
        #             "to 1")
        #     if len(acceptance_strategies) >= 1:
        #         if elicitation_strategies is None or len(elicitation_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more acceptance_strategies, so you have to set all EUBOA components or "
        #                 "set acceptance_strategies to None")
        #     if len(acceptance_strategies) >= 1:
        #         if user_models is None or len(user_models) < 1:
        #             raise ValueError(
        #                 "You selected an or more acceptance_strategies, so you have to set all EUBOA components or "
        #                 "set acceptance_strategies to None")
        #     if len(acceptance_strategies) >= 1:
        #         if bidding_strategies is None or len(bidding_strategies) < 1:
        #             raise ValueError(
        #                 "You selected an or more acceptance_strategies, so you have to set all EUBOA components or "
        #                 "set acceptance_strategies to None")
        #     if len(acceptance_strategies) >= 1:
        #         if opponent_models is None or len(opponent_models) < 1:
        #             raise ValueError(
        #                 "You selected an or more acceptance_strategies, so you have to set all EUBOA components or "
        #                 "set acceptance_strategies to None")

        if (elicitation_strategies is not None and len(elicitation_strategies) >= 1) \
                and (user_models is not None and len(user_models) >= 1) \
                and (bidding_strategies is not None and len(bidding_strategies) >= 1) \
                and (opponent_models is not None and len(opponent_models) >= 1) \
                and (acceptance_strategies is not None and len(acceptance_strategies) >= 1):
            if not (EUBOA_is_agent_side or EUBOA_is_opponent_side):
                raise ValueError(
                    "if select at least one component for each EUBOA components, you have to set one or both "
                    "EUBOA_is_agent_side, EUBOA_is_opponent_side True")
            else:
                self.__all_euboa_agents = CreateAllAgentsUsingEUBOAComponents(elicitation_strategies=elicitation_strategies,
                                                                              user_models=user_models,
                                                                              bidding_strategies=bidding_strategies,
                                                                              opponent_models=opponent_models,
                                                                              acceptance_strategies=acceptance_strategies).create_agents()

        sample_preference_data_structure = {
            'Brand': ['0.45', {'Lenovo': '10', 'Assus': '20', 'Mac': '30'}],
            'Monitor': ['0.18', {'15': '30', '10': '25', '11': '20'}],
            'HDD': ['0.38', {'1T': '25', '2T': '32', '3T': '35'}],
            'discount_factor': 1.0,
            'reservation': 0.0
        }
        self.__test_preference1 = Preference(domain_name='laptop', preference_data_structure=sample_preference_data_structure)

        self.__users = users
        self.__domain_names = domain_names
        self.__agent_names = agent_names
        self.__opponent_names = opponent_names
        self.__protocol_name = protocol_name
        self.__analysis_man_name = analysis_man_name
        self.__deadline = deadline
        self.__deadline_type = deadline_type
        self.__tournament_analysis_man = CreateObjectByPath.get_object(ANALYSIS_TOURNAMENT_PATH,
                                                                       Tournament_analysis_name,
                                                                       agent_names)
        self.__utility_space_names = utility_space_names
        self.__tournament_repetition = int(tournament_repetition)
        self.__avg_all_tournament_analysis_data = {}

        # if EUBOA_is_agent_side is True then add all created euboa_agents to agents.
        # if EUBOA_is_opponent_side is True then add all created euboa_agents to opponents
        if EUBOA_is_agent_side:
            self.__agent_names += self.__all_euboa_agents
        if EUBOA_is_opponent_side:
            self.__opponent_names += self.__all_euboa_agents

        # if BOA_is_agent_side is True then add all created boa_agents to agents.
        # if BOA_is_opponent_side is True then add all created boa_agents to opponents
        if BOA_is_agent_side:
            self.__agent_names += self.__all_boa_agents
        if BOA_is_opponent_side:
            self.__opponent_names += self.__all_boa_agents

    def get_tournament_analysis_man(self):
        return self.__tournament_analysis_man

    def start_tournament(self):
        for t_num in range(self.__tournament_repetition):
            ctrl = Controller()
            for domain_name in self.__domain_names:
                preferences_of_domain = ctrl.fetch_preferences_of_domain(domain_name)
                for preference_permutations in permutations(preferences_of_domain, 2):
                    for party1_name in self.__agent_names:
                        for party2_name in self.__opponent_names:
                            if party1_name != party2_name: # this line of code does not let two same agents negotiate each other
                                count_of_utility_spaces = len(self.__utility_space_names)
                                for i in range(count_of_utility_spaces):
                                    utility_space1 = self.__utility_space_names[i]
                                    for j in range(i, count_of_utility_spaces):
                                        utility_space2 = self.__utility_space_names[j]

                                        ###############################################################################
                                        # if isinstance(party1_name, EUBOAParty) and isinstance(party2_name, EUBOAParty):
                                        #     # initial_preference1 = preference_permutations[0].get_initial_preference()
                                        #     # party1_name.set_preference(preference=initial_preference1)
                                        #     #
                                        #     # initial_preference2 = preference_permutations[1].get_initial_preference()
                                        #     # party2_name.set_preference(preference=initial_preference2)
                                        #
                                        #     count_of_users = len(self.__users)
                                        #     for i in range(count_of_users):
                                        #         user1 = self.__users[i]
                                        #         for j in range(i, count_of_users):
                                        #             user2 = self.__users[j]
                                        #             bilateral_session = BilateralSession(
                                        #                 protocol_name=self.__protocol_name,
                                        #                 analysis_man_name=self.__analysis_man_name,
                                        #                 deadline=self.__deadline,
                                        #                 deadline_type=self.__deadline_type,
                                        #                 first_preference=preference_permutations[0],
                                        #                 second_preference=preference_permutations[1],
                                        #                 party1_uncertain=None,
                                        #                 party2_uncertain=None,
                                        #                 domain_name=domain_name,
                                        #                 utility_space_name1=utility_space1,
                                        #                 utility_space_name2=utility_space2,
                                        #                 user1=user1,
                                        #                 user2=user2,
                                        #                 party1_EUBOAParty=party1_name,
                                        #                 party2_EUBOAParty=party2_name)
                                        #
                                        #             bilateral_session.start_session()
                                        #             self.__tournament_analysis_man.add_session_analysis_data(
                                        #                 bilateral_session.get_analysis_man().get_analysis_data())
                                        # elif isinstance(party1_name, EUBOAParty) and isinstance(party2_name, str):
                                        #
                                        #     # initial_preference1 = preference_permutations[0].get_initial_preference()
                                        #     # party1_name.set_preference(preference=initial_preference1)
                                        #
                                        #     uncertainty_bool_party2 = self.detect_agent_type(party2_name, utility_space2)
                                        #     if uncertainty_bool_party2:
                                        #         count_of_users = len(self.__users)
                                        #         for i in range(count_of_users):
                                        #             user1 = self.__users[i]
                                        #             for j in range(i, count_of_users):
                                        #                 user2 = self.__users[j]
                                        #                 bilateral_session = BilateralSession(
                                        #                     protocol_name=self.__protocol_name,
                                        #                     analysis_man_name=self.__analysis_man_name,
                                        #                     deadline=self.__deadline,
                                        #                     deadline_type=self.__deadline_type,
                                        #                     first_preference=preference_permutations[0],
                                        #                     second_preference=preference_permutations[1],
                                        #                     party1_uncertain=None,
                                        #                     party2_name=party2_name,
                                        #                     domain_name=domain_name,
                                        #                     utility_space_name1=utility_space1,
                                        #                     utility_space_name2=utility_space2,
                                        #                     user1=user1,
                                        #                     user2=user2,
                                        #                     party1_EUBOAParty=party1_name)
                                        #
                                        #                 bilateral_session.start_session()
                                        #                 self.__tournament_analysis_man.add_session_analysis_data(
                                        #                     bilateral_session.get_analysis_man().get_analysis_data())
                                        #     else:
                                        #         for user1 in self.__users:
                                        #             bilateral_session = BilateralSession(
                                        #                 protocol_name=self.__protocol_name,
                                        #                 analysis_man_name=self.__analysis_man_name,
                                        #                 deadline=self.__deadline,
                                        #                 deadline_type=self.__deadline_type,
                                        #                 first_preference=preference_permutations[0],
                                        #                 second_preference=preference_permutations[1],
                                        #                 party1_uncertain=None,
                                        #                 party2_name=party2_name,
                                        #                 domain_name=domain_name,
                                        #                 utility_space_name1=utility_space1,
                                        #                 utility_space_name2=utility_space2,
                                        #                 user1=user1,
                                        #                 user2=None,
                                        #                 party1_EUBOAParty=party1_name)
                                        #
                                        #             bilateral_session.start_session()
                                        #             self.__tournament_analysis_man.add_session_analysis_data(
                                        #                 bilateral_session.get_analysis_man().get_analysis_data())
                                        # elif isinstance(party1_name, str) and isinstance(party2_name, EUBOAParty):
                                        #
                                        #     # initial_preference2 = preference_permutations[1].get_initial_preference()
                                        #     # party2_name.set_preference(preference=initial_preference2)
                                        #
                                        #     uncertainty_bool_party1 = self.detect_agent_type(party1_name, utility_space1)
                                        #     if uncertainty_bool_party1:
                                        #         count_of_users = len(self.__users)
                                        #         for i in range(count_of_users):
                                        #             user1 = self.__users[i]
                                        #             for j in range(i, count_of_users):
                                        #                 user2 = self.__users[j]
                                        #                 bilateral_session = BilateralSession(
                                        #                     protocol_name=self.__protocol_name,
                                        #                     analysis_man_name=self.__analysis_man_name,
                                        #                     deadline=self.__deadline,
                                        #                     deadline_type=self.__deadline_type,
                                        #                     first_preference=preference_permutations[0],
                                        #                     second_preference=preference_permutations[1],
                                        #                     party1_name=party1_name,
                                        #                     party2_uncertain=None,
                                        #                     domain_name=domain_name,
                                        #                     utility_space_name1=utility_space1,
                                        #                     utility_space_name2=utility_space2,
                                        #                     user1=user1,
                                        #                     user2=user2,
                                        #                     party2_EUBOAParty=party2_name)
                                        #
                                        #                 bilateral_session.start_session()
                                        #                 self.__tournament_analysis_man.add_session_analysis_data(
                                        #                     bilateral_session.get_analysis_man().get_analysis_data())
                                        #     else:
                                        #         for user2 in self.__users:
                                        #             bilateral_session = BilateralSession(
                                        #                 protocol_name=self.__protocol_name,
                                        #                 analysis_man_name=self.__analysis_man_name,
                                        #                 deadline=self.__deadline,
                                        #                 deadline_type=self.__deadline_type,
                                        #                 first_preference=
                                        #                 preference_permutations[0],
                                        #                 second_preference=
                                        #                 preference_permutations[1],
                                        #                 party1_name=party1_name,
                                        #                 party2_uncertain=None,
                                        #                 domain_name=domain_name,
                                        #                 utility_space_name1=utility_space1,
                                        #                 utility_space_name2=utility_space2,
                                        #                 user1=None,
                                        #                 user2=user2,
                                        #                 party2_EUBOAParty=party2_name)
                                        #
                                        #             bilateral_session.start_session()
                                        #             self.__tournament_analysis_man.add_session_analysis_data(
                                        #                 bilateral_session.get_analysis_man().get_analysis_data())
                                        # elif isinstance(party1_name, str) and isinstance(party2_name, str):
                                        #     uncertainty_bool_party1 = self.detect_agent_type(party1_name, utility_space1)
                                        #     # try:
                                        #     #     test_utility_space1 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space1, self.__test_preference1)
                                        #     #     test_party1 = CreateObjectByPath.get_object(PARTY_PATH, party1_name, test_utility_space1)
                                        #     #     uncertainty_bool_party1 = False
                                        #     # except:
                                        #     #     uncertainty_bool_party1 = True
                                        #     #     if self.__users is None:
                                        #     #         raise ValueError(
                                        #     #             "You selected one or more agent with uncertainty situation but there is no user")
                                        #
                                        #     uncertainty_bool_party2 = self.detect_agent_type(party2_name,
                                        #                                                      utility_space2)
                                        #     # try:
                                        #     #     test_utility_space2 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH,
                                        #     #                                                         utility_space2,
                                        #     #                                                         self.__test_preference1)
                                        #     #     test_party2 = CreateObjectByPath.get_object(PARTY_PATH, party2_name,
                                        #     #                                                 test_utility_space2)
                                        #     #     uncertainty_bool_party2 = False
                                        #     # except:
                                        #     #     uncertainty_bool_party2 = True
                                        #     #     if self.__users is None:
                                        #     #         raise ValueError(
                                        #     #             "You selected one or more agent with uncertainty situation but there is no user")
                                        #
                                        #     if uncertainty_bool_party1 and not uncertainty_bool_party2:
                                        #         for user1 in self.__users:
                                        #             bilateral_session = BilateralSession(
                                        #                 protocol_name=self.__protocol_name,
                                        #                 analysis_man_name=self.__analysis_man_name,
                                        #                 deadline=self.__deadline,
                                        #                 deadline_type=self.__deadline_type,
                                        #                 first_preference=preference_permutations[0],
                                        #                 second_preference=preference_permutations[1],
                                        #                 party1_name=party1_name,
                                        #                 party2_name=party2_name,
                                        #                 domain_name=domain_name,
                                        #                 utility_space_name1=utility_space1,
                                        #                 utility_space_name2=utility_space2,
                                        #                 user1=user1,
                                        #                 user2=None)
                                        #
                                        #             bilateral_session.start_session()
                                        #             self.__tournament_analysis_man.add_session_analysis_data(
                                        #                 bilateral_session.get_analysis_man().get_analysis_data())
                                        #
                                        #     if not uncertainty_bool_party1 and uncertainty_bool_party2:
                                        #         for user2 in self.__users:
                                        #             bilateral_session = BilateralSession(
                                        #                 protocol_name=self.__protocol_name,
                                        #                 analysis_man_name=self.__analysis_man_name,
                                        #                 deadline=self.__deadline,
                                        #                 deadline_type=self.__deadline_type,
                                        #                 first_preference=preference_permutations[0],
                                        #                 second_preference=preference_permutations[1],
                                        #                 party1_name=party1_name,
                                        #                 party2_name=party2_name,
                                        #                 domain_name=domain_name,
                                        #                 utility_space_name1=utility_space1,
                                        #                 utility_space_name2=utility_space2,
                                        #                 user1=None,
                                        #                 user2=user2)
                                        #
                                        #             bilateral_session.start_session()
                                        #             self.__tournament_analysis_man.add_session_analysis_data(
                                        #                 bilateral_session.get_analysis_man().get_analysis_data())
                                        #
                                        #     if uncertainty_bool_party1 and uncertainty_bool_party2:
                                        #         count_of_users = len(self.__users)
                                        #         for i in range(count_of_users):
                                        #             user1 = self.__users[i]
                                        #             for j in range(i, count_of_users):
                                        #                 user2 = self.__users[j]
                                        #                 bilateral_session = BilateralSession(
                                        #                     protocol_name=self.__protocol_name,
                                        #                     analysis_man_name=self.__analysis_man_name,
                                        #                     deadline=self.__deadline,
                                        #                     deadline_type=self.__deadline_type,
                                        #                     first_preference=preference_permutations[0],
                                        #                     second_preference=preference_permutations[1],
                                        #                     party1_name=party1_name,
                                        #                     party2_name=party2_name,
                                        #                     domain_name=domain_name,
                                        #                     utility_space_name1=utility_space1,
                                        #                     utility_space_name2=utility_space2,
                                        #                     user1=user1,
                                        #                     user2=user2)
                                        #
                                        #                 bilateral_session.start_session()
                                        #                 self.__tournament_analysis_man.add_session_analysis_data(
                                        #                     bilateral_session.get_analysis_man().get_analysis_data())
                                        #
                                        #     if not uncertainty_bool_party1 and not uncertainty_bool_party2:
                                        #         bilateral_session = BilateralSession(protocol_name=self.__protocol_name,
                                        #                                              analysis_man_name=self.__analysis_man_name,
                                        #                                              deadline=self.__deadline,
                                        #                                              deadline_type=self.__deadline_type,
                                        #                                              first_preference=
                                        #                                              preference_permutations[0],
                                        #                                              second_preference=
                                        #                                              preference_permutations[1],
                                        #                                              party1_name=party1_name,
                                        #                                              party2_name=party2_name,
                                        #                                              domain_name=domain_name,
                                        #                                              utility_space_name1=utility_space1,
                                        #                                              utility_space_name2=utility_space2,
                                        #                                              user1=None,
                                        #                                              user2=None)
                                        #
                                        #         bilateral_session.start_session()
                                        #         self.__tournament_analysis_man.add_session_analysis_data(
                                        #             bilateral_session.get_analysis_man().get_analysis_data())
                                        #
                                        # else:
                                        #     raise TypeError("Something went wrong! ("
                                        #                     "BilateralTournament2.BilateralTournament)")
                                        ###############################################################################

                                        # /////////////////////////////////////////////////////////////////////////////
                                        if isinstance(party1_name, EUBOAParty) and isinstance(party2_name, EUBOAParty):
                                            count_of_users = len(self.__users)
                                            for i in range(count_of_users):
                                                user1 = self.__users[i]
                                                for j in range(i, count_of_users):
                                                    user2 = self.__users[j]
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=preference_permutations[0],
                                                        second_preference=preference_permutations[1],
                                                        party1_uncertain=None,
                                                        party2_uncertain=None,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=user1,
                                                        user2=user2,
                                                        party1_EUBOAParty=party1_name,
                                                        party2_EUBOAParty=party2_name)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())
                                        elif isinstance(party1_name, EUBOAParty) and isinstance(party2_name, BOAParty):
                                            for user1 in self.__users:
                                                bilateral_session = BilateralSession(
                                                    protocol_name=self.__protocol_name,
                                                    analysis_man_name=self.__analysis_man_name,
                                                    deadline=self.__deadline,
                                                    deadline_type=self.__deadline_type,
                                                    first_preference=preference_permutations[0],
                                                    second_preference=preference_permutations[1],
                                                    party1_uncertain=None,
                                                    party2_uncertain=None,
                                                    domain_name=domain_name,
                                                    utility_space_name1=utility_space1,
                                                    utility_space_name2=utility_space2,
                                                    user1=user1,
                                                    party1_EUBOAParty=party1_name,
                                                    party2_BOAParty=party2_name)
                                                bilateral_session.start_session()
                                                self.__tournament_analysis_man.add_session_analysis_data(
                                                    bilateral_session.get_analysis_man().get_analysis_data())
                                        elif isinstance(party1_name, EUBOAParty) and isinstance(party2_name, str):
                                            uncertainty_bool_party2 = self.detect_agent_type(party2_name,
                                                                                             utility_space2)
                                            if uncertainty_bool_party2:
                                                count_of_users = len(self.__users)
                                                for i in range(count_of_users):
                                                    user1 = self.__users[i]
                                                    for j in range(i, count_of_users):
                                                        user2 = self.__users[j]
                                                        bilateral_session = BilateralSession(
                                                            protocol_name=self.__protocol_name,
                                                            analysis_man_name=self.__analysis_man_name,
                                                            deadline=self.__deadline,
                                                            deadline_type=self.__deadline_type,
                                                            first_preference=preference_permutations[0],
                                                            second_preference=preference_permutations[1],
                                                            party1_uncertain=None,
                                                            party2_name=party2_name,
                                                            domain_name=domain_name,
                                                            utility_space_name1=utility_space1,
                                                            utility_space_name2=utility_space2,
                                                            user1=user1,
                                                            user2=user2,
                                                            party1_EUBOAParty=party1_name)

                                                        bilateral_session.start_session()
                                                        self.__tournament_analysis_man.add_session_analysis_data(
                                                            bilateral_session.get_analysis_man().get_analysis_data())
                                            else:
                                                for user1 in self.__users:
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=preference_permutations[0],
                                                        second_preference=preference_permutations[1],
                                                        party1_uncertain=None,
                                                        party2_name=party2_name,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=user1,
                                                        user2=None,
                                                        party1_EUBOAParty=party1_name)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())


                                        elif isinstance(party1_name, BOAParty) and isinstance(party2_name, EUBOAParty):
                                            for user2 in self.__users:
                                                bilateral_session = BilateralSession(
                                                    protocol_name=self.__protocol_name,
                                                    analysis_man_name=self.__analysis_man_name,
                                                    deadline=self.__deadline,
                                                    deadline_type=self.__deadline_type,
                                                    first_preference=preference_permutations[0],
                                                    second_preference=preference_permutations[1],
                                                    party1_uncertain=None,
                                                    party2_uncertain=None,
                                                    domain_name=domain_name,
                                                    utility_space_name1=utility_space1,
                                                    utility_space_name2=utility_space2,
                                                    user2=user2,
                                                    party1_BOAParty=party1_name,
                                                    party2_EUBOAParty=party2_name)
                                                bilateral_session.start_session()
                                                self.__tournament_analysis_man.add_session_analysis_data(
                                                    bilateral_session.get_analysis_man().get_analysis_data())
                                        elif isinstance(party1_name, BOAParty) and isinstance(party2_name, BOAParty):

                                            bilateral_session = BilateralSession(
                                                protocol_name=self.__protocol_name,
                                                analysis_man_name=self.__analysis_man_name,
                                                deadline=self.__deadline,
                                                deadline_type=self.__deadline_type,
                                                first_preference=preference_permutations[0],
                                                second_preference=preference_permutations[1],
                                                party1_uncertain=None,
                                                party2_uncertain=None,
                                                domain_name=domain_name,
                                                utility_space_name1=utility_space1,
                                                utility_space_name2=utility_space2,
                                                party1_BOAParty=party1_name,
                                                party2_BOAParty=party2_name)

                                            bilateral_session.start_session()
                                            self.__tournament_analysis_man.add_session_analysis_data(
                                                bilateral_session.get_analysis_man().get_analysis_data())
                                        elif isinstance(party1_name, BOAParty) and isinstance(party2_name, str):
                                            uncertainty_bool_party2 = self.detect_agent_type(party2_name, utility_space2)
                                            if uncertainty_bool_party2:
                                                for user2 in self.__users:
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=preference_permutations[0],
                                                        second_preference=preference_permutations[1],
                                                        party1_BOAParty=party1_name,
                                                        party2_name=party2_name,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=None,
                                                        user2=user2)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())
                                            else:
                                                bilateral_session = BilateralSession(
                                                    protocol_name=self.__protocol_name,
                                                    analysis_man_name=self.__analysis_man_name,
                                                    deadline=self.__deadline,
                                                    deadline_type=self.__deadline_type,
                                                    first_preference=preference_permutations[0],
                                                    second_preference=preference_permutations[1],
                                                    party1_BOAParty=party1_name,
                                                    party2_name=party2_name,
                                                    domain_name=domain_name,
                                                    utility_space_name1=utility_space1,
                                                    utility_space_name2=utility_space2,
                                                    user1=None,
                                                    user2=None)

                                                bilateral_session.start_session()
                                                self.__tournament_analysis_man.add_session_analysis_data(
                                                    bilateral_session.get_analysis_man().get_analysis_data())
                                        elif isinstance(party1_name, str) and isinstance(party2_name, EUBOAParty):
                                            uncertainty_bool_party1 = self.detect_agent_type(party1_name,
                                                                                             utility_space1)
                                            if uncertainty_bool_party1:
                                                count_of_users = len(self.__users)
                                                for i in range(count_of_users):
                                                    user1 = self.__users[i]
                                                    for j in range(i, count_of_users):
                                                        user2 = self.__users[j]
                                                        bilateral_session = BilateralSession(
                                                            protocol_name=self.__protocol_name,
                                                            analysis_man_name=self.__analysis_man_name,
                                                            deadline=self.__deadline,
                                                            deadline_type=self.__deadline_type,
                                                            first_preference=preference_permutations[0],
                                                            second_preference=preference_permutations[1],
                                                            party1_name=party1_name,
                                                            party2_uncertain=None,
                                                            domain_name=domain_name,
                                                            utility_space_name1=utility_space1,
                                                            utility_space_name2=utility_space2,
                                                            user1=user1,
                                                            user2=user2,
                                                            party2_EUBOAParty=party2_name)

                                                        bilateral_session.start_session()
                                                        self.__tournament_analysis_man.add_session_analysis_data(
                                                            bilateral_session.get_analysis_man().get_analysis_data())
                                            else:
                                                for user2 in self.__users:
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=
                                                        preference_permutations[0],
                                                        second_preference=
                                                        preference_permutations[1],
                                                        party1_name=party1_name,
                                                        party2_uncertain=None,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=None,
                                                        user2=user2,
                                                        party2_EUBOAParty=party2_name)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())

                                        elif isinstance(party1_name, str) and isinstance(party2_name, BOAParty):
                                            uncertainty_bool_party1 = self.detect_agent_type(party1_name, utility_space1)
                                            if uncertainty_bool_party1:
                                                for user1 in self.__users:
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=preference_permutations[0],
                                                        second_preference=preference_permutations[1],
                                                        party1_name=party1_name,
                                                        party2_BOAParty=party2_name,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=user1,
                                                        user2=None)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())
                                            else:
                                                bilateral_session = BilateralSession(
                                                    protocol_name=self.__protocol_name,
                                                    analysis_man_name=self.__analysis_man_name,
                                                    deadline=self.__deadline,
                                                    deadline_type=self.__deadline_type,
                                                    first_preference=preference_permutations[0],
                                                    second_preference=preference_permutations[1],
                                                    party1_name=party1_name,
                                                    party2_BOAParty=party2_name,
                                                    domain_name=domain_name,
                                                    utility_space_name1=utility_space1,
                                                    utility_space_name2=utility_space2)

                                                bilateral_session.start_session()
                                                self.__tournament_analysis_man.add_session_analysis_data(
                                                    bilateral_session.get_analysis_man().get_analysis_data())

                                        elif isinstance(party1_name, str) and isinstance(party2_name, str):
                                            uncertainty_bool_party1 = self.detect_agent_type(party1_name, utility_space1)

                                            uncertainty_bool_party2 = self.detect_agent_type(party2_name, utility_space2)

                                            if uncertainty_bool_party1 and not uncertainty_bool_party2:
                                                for user1 in self.__users:
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=preference_permutations[0],
                                                        second_preference=preference_permutations[1],
                                                        party1_name=party1_name,
                                                        party2_name=party2_name,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=user1,
                                                        user2=None)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())

                                            if not uncertainty_bool_party1 and uncertainty_bool_party2:
                                                for user2 in self.__users:
                                                    bilateral_session = BilateralSession(
                                                        protocol_name=self.__protocol_name,
                                                        analysis_man_name=self.__analysis_man_name,
                                                        deadline=self.__deadline,
                                                        deadline_type=self.__deadline_type,
                                                        first_preference=preference_permutations[0],
                                                        second_preference=preference_permutations[1],
                                                        party1_name=party1_name,
                                                        party2_name=party2_name,
                                                        domain_name=domain_name,
                                                        utility_space_name1=utility_space1,
                                                        utility_space_name2=utility_space2,
                                                        user1=None,
                                                        user2=user2)

                                                    bilateral_session.start_session()
                                                    self.__tournament_analysis_man.add_session_analysis_data(
                                                        bilateral_session.get_analysis_man().get_analysis_data())

                                            if uncertainty_bool_party1 and uncertainty_bool_party2:
                                                count_of_users = len(self.__users)
                                                for i in range(count_of_users):
                                                    user1 = self.__users[i]
                                                    for j in range(i, count_of_users):
                                                        user2 = self.__users[j]
                                                        bilateral_session = BilateralSession(
                                                            protocol_name=self.__protocol_name,
                                                            analysis_man_name=self.__analysis_man_name,
                                                            deadline=self.__deadline,
                                                            deadline_type=self.__deadline_type,
                                                            first_preference=preference_permutations[0],
                                                            second_preference=preference_permutations[1],
                                                            party1_name=party1_name,
                                                            party2_name=party2_name,
                                                            domain_name=domain_name,
                                                            utility_space_name1=utility_space1,
                                                            utility_space_name2=utility_space2,
                                                            user1=user1,
                                                            user2=user2)

                                                        bilateral_session.start_session()
                                                        self.__tournament_analysis_man.add_session_analysis_data(
                                                            bilateral_session.get_analysis_man().get_analysis_data())

                                            if not uncertainty_bool_party1 and not uncertainty_bool_party2:
                                                bilateral_session = BilateralSession(protocol_name=self.__protocol_name,
                                                                                     analysis_man_name=self.__analysis_man_name,
                                                                                     deadline=self.__deadline,
                                                                                     deadline_type=self.__deadline_type,
                                                                                     first_preference=
                                                                                     preference_permutations[0],
                                                                                     second_preference=
                                                                                     preference_permutations[1],
                                                                                     party1_name=party1_name,
                                                                                     party2_name=party2_name,
                                                                                     domain_name=domain_name,
                                                                                     utility_space_name1=utility_space1,
                                                                                     utility_space_name2=utility_space2,
                                                                                     user1=None,
                                                                                     user2=None)

                                                bilateral_session.start_session()
                                                self.__tournament_analysis_man.add_session_analysis_data(
                                                    bilateral_session.get_analysis_man().get_analysis_data())


                                        else:
                                            raise TypeError("Something went wrong! ("
                                                            "BilateralTournament2.BilateralTournament)")
                                        # /////////////////////////////////////////////////////////////////////////////




            self.cal_avg()
            # tournament_analysis_data = self.__tournament_analysis_man.get_tournament_analysis_data()
            # count = 1
            # for key, value in tournament_analysis_data.items():
            #     if key not in self.__avg_all_tournament_analysis_data:
            #         self.__avg_all_tournament_analysis_data[key] = value
            #     else:
            #         self.__avg_all_tournament_analysis_data[key] = \
            #             (((self.__avg_all_tournament_analysis_data[key]*count) + value)/(count+1))
            #         count += 1

        print('**************************** Final Result ****************************')
        print(self.__avg_all_tournament_analysis_data)
        print('**********************************************************************')
        self.__tournament_analysis_man.save_analysis_data()

    def detect_agent_type(self, agent_name: str, utility_space: str) -> bool:
        """
        this method get an agent name as string and
        returns True if agent name belongs to an uncertain agent otherwise
        returns False
        :param utility_space:
        :param agent_name: the name of  the agent (string)
        :return: True or False
        """
        uncertainty_bool_party1 = False
        try:
            test_utility_space = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space,
                                                               self.__test_preference1)
            test_party1 = CreateObjectByPath.get_object(PARTY_PATH, agent_name, test_utility_space)
            uncertainty_bool_party1 = False
        except:
            uncertainty_bool_party1 = True
            if self.__users is None:
                raise ValueError(
                    "You selected one or more agent with uncertainty situation but there is no user")
        return uncertainty_bool_party1
        # return False

    def get_avg_all_tournament_analysis_data(self):
        return self.__avg_all_tournament_analysis_data

    def cal_avg(self):
        '''
        this method calculates the average over iterations of tournament
        :return: average
        '''
        tournament_analysis_data = self.__tournament_analysis_man.get_tournament_analysis_data()
        count = 1
        for key, value in tournament_analysis_data.items():
            if not isinstance(value, list):
                if key not in self.__avg_all_tournament_analysis_data:
                    self.__avg_all_tournament_analysis_data[key] = value
                else:
                    self.__avg_all_tournament_analysis_data[key] = \
                        (((self.__avg_all_tournament_analysis_data[key] * count) + value) / (count + 1))
                    count += 1
