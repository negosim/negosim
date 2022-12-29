from itertools import permutations
import CreateObjectByPath
from core.BilateralSession import BilateralSession
from controller import Controller
from configurations import *
from core.Preference import Preference


class BilateralTournament:

    def __init__(self, protocol_name: str, analysis_man_name: str, Tournament_analysis_name: str,
                 deadline: str, deadline_type: str, agent_names: list, opponent_names: list, domain_names: list,
                 tournament_repetition: str, utility_space_names: list, users: list = None):

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
                            if party1_name != party2_name:
                                # for utility_space1 in self.__utility_space_names:
                                count_of_utility_spaces = len(self.__utility_space_names)
                                for i in range(count_of_utility_spaces):
                                    utility_space1 = self.__utility_space_names[i]
                                    for j in range(i, count_of_utility_spaces):
                                        utility_space2 = self.__utility_space_names[j]

                                        uncertainty_bool_party1 = False
                                        try:
                                            test_preference1 = Preference(domain_name='laptop', xml_file_name='laptop_buyer_utility.xml')
                                            test_utility_space1 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space1, test_preference1)
                                            test_party1 = CreateObjectByPath.get_object(PARTY_PATH, party1_name, test_utility_space1)
                                            uncertainty_bool_party1 = False
                                        except:
                                            uncertainty_bool_party1 = True
                                            if self.__users is None:
                                                raise ValueError("You selected one or more agent with uncertainty situation but there is no user")

                                        uncertainty_bool_party2 = False
                                        try:
                                            test_preference2 = Preference(domain_name='laptop', xml_file_name='laptop_buyer_utility.xml')
                                            test_utility_space2 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space2, test_preference2)
                                            test_party2 = CreateObjectByPath.get_object(PARTY_PATH, party2_name, test_utility_space2)
                                            uncertainty_bool_party2 = False
                                        except:
                                            uncertainty_bool_party2 = True
                                            if self.__users is None:
                                                raise ValueError("You selected one or more agent with uncertainty situation but there is no user")

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
                                                                                 first_preference=preference_permutations[0],
                                                                                 second_preference=preference_permutations[1],
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
