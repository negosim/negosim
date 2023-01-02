import CreateObjectByPath
from core.NegoTable import NegoTable
from core.Preference import Preference
from configurations import *
from core.StateInfo import StateInfo
from core.TimeLine import TimeLine
from core.AbstractNegoParty import AbstractNegoParty
from core.AbstractNegoPartyUncertainCondition import AbstractNegoPartyUncertainCondition
from core.EUBOAParty import EUBOAParty
from core.BOAParty import BOAParty


class BilateralSession:

    def __init__(self, protocol_name: str, analysis_man_name: str, deadline, deadline_type: str,
                 first_preference, second_preference,
                 domain_name: str,
                 utility_space_name1: str, utility_space_name2: str = None,
                 party1_name: str = None, party2_name: str = None,
                 party1: AbstractNegoParty = None, party2: AbstractNegoParty = None,
                 party1_uncertain: AbstractNegoPartyUncertainCondition = None, party2_uncertain: AbstractNegoPartyUncertainCondition = None,
                 party1_EUBOAParty: EUBOAParty = None, party2_EUBOAParty: EUBOAParty = None,
                 party1_BOAParty: BOAParty = None, party2_BOAParty: BOAParty = None,
                 user1: str = None, user2: str = None):


        # print("protocol_name=", protocol_name,
        #       "analysis_man_name=", analysis_man_name,
        #       "deadline=", deadline,
        #       "deadline_type=", deadline_type,
        #       "first_preference=", first_preference," & ","second_preference=", second_preference,
        #       "domain_name=", domain_name,
        #       "utility_space_name1=", utility_space_name1, " & ", "utility_space_name2=", utility_space_name2,
        #       "party1_name=", party1_name, " & ", "party2_name=", party2_name,
        #       "party1=", party1, " & ", "party2=", party2,
        #       "party1_uncertain=", party1_uncertain, " & ", "party2_uncertain=", party2_uncertain,
        #       "party1_EUBOAParty=", party1_EUBOAParty, " & ", "party2_EUBOAParty=", party2_EUBOAParty,
        #       "user1=", user1, " & ", "user2=", user2)


        """

        :param protocol_name:
        :param analysis_man_name:
        :param deadline:
        :param deadline_type:
        :param first_preference: should be a name of preference or an preference object
        :param second_preference: should be a name of preference or an preference object
        :param domain_name:
        :param utility_space_name1:
        :param utility_space_name2:
        :param party1_name:
        :param party2_name:
        :param party1:
        :param party2:
        :param party1_uncertain:
        :param party2_uncertain:
        :param party1_EUBOAParty:
        :param party2_EUBOAParty:
        :param party1_BOAParty:
        :param party2_BOAParty:
        :param user1:
        :param user2:
        """



        if not isinstance(protocol_name, str):
            raise TypeError('protocol_name must be a string')
        if not isinstance(analysis_man_name, str):
            raise TypeError('analysis_man_name must be a string')
        if not isinstance(deadline, str):
            raise TypeError('deadline must be a string')
        if not isinstance(deadline_type, str):
            print(type(deadline_type))
            raise TypeError('deadline_type must be a string')
        if not (isinstance(first_preference, str) or isinstance(first_preference, Preference)):
            raise TypeError('first_preference_name must be a string')
        if not (isinstance(second_preference, str) or isinstance(second_preference, Preference)):
            raise TypeError('second_preference_name must be a string')
        if not isinstance(domain_name, str):
            raise TypeError('domain_name must be a string')
        if not isinstance(utility_space_name1, str):
            raise TypeError('utility_space_name1 must be a string')
        if not isinstance(utility_space_name2, str) and utility_space_name2 is not None:
            raise TypeError('utility_space_name2 must be a string or None')
        if not isinstance(party1_EUBOAParty, EUBOAParty) and party1_EUBOAParty is not None:
            raise TypeError('party1_EUBOAParty must be an instance of EUBOAParty or None')
        if not isinstance(party2_EUBOAParty, EUBOAParty) and party2_EUBOAParty is not None:
            raise TypeError('party2_EUBOAParty must be an instance of EUBOAParty or None')
        if not isinstance(party1_BOAParty, BOAParty) and party1_BOAParty is not None:
            raise TypeError('party1_BOAParty must be an instance of BOAParty or None')
        if not isinstance(party2_BOAParty, BOAParty) and party2_BOAParty is not None:
            raise TypeError('party2_BOAParty must be an instance of BOAParty or None')
        if not isinstance(user1, str) and user1 is not None:
            raise TypeError('user1 must be a string or None')
        if not isinstance(user2, str) and user2 is not None:
            raise TypeError('user2 must be a string or None')
        if not isinstance(party1_name, str) and party1_name is not None:
            raise TypeError('party1_name must be a string or None')
        if not isinstance(party2_name, str) and party2_name is not None:
            raise TypeError('party2_name must be a string or None')
        if not isinstance(party1, AbstractNegoParty) and party1 is not None:
            raise TypeError('party1 must be a string or None')
        if not isinstance(party2, AbstractNegoParty) and party2 is not None:
            raise TypeError('party2 must be a string or None')
        if not isinstance(party1_uncertain, AbstractNegoParty) and party1_uncertain is not None:
            raise TypeError('party1_uncertain must be a string or None')
        if not isinstance(party2_uncertain, AbstractNegoParty) and party2_uncertain is not None:
            raise TypeError('party2_uncertain must be a string or None')
        if not(
                ((party1_name is not None and party2_name is not None) or
                (party1_name is not None and party2 is not None) or
                (party1_name is not None and party2_uncertain is not None) or
                (party1_name is not None and party2_EUBOAParty is not None) or
                (party1_name is not None and party2_BOAParty is not None))
               or
               ((party1 is not None and party2_name is not None) or
                (party1 is not None and party2 is not None) or
                (party1 is not None and party2_uncertain is not None) or
                (party1 is not None and party2_EUBOAParty is not None) or
                (party1 is not None and party2_BOAParty is not None))
               or
               ((party1_uncertain is not None and party2_name is not None) or
                (party1_uncertain is not None and party2 is not None) or
                (party1_uncertain is not None and party2_uncertain) or
                (party1_uncertain is not None and party2_EUBOAParty) or
                (party1_uncertain is not None and party2_BOAParty))
                or
                ((party1_EUBOAParty is not None and party2_name is not None) or
                 (party1_EUBOAParty is not None and party2 is not None) or
                 (party1_EUBOAParty is not None and party2_uncertain) or
                 (party1_EUBOAParty is not None and party2_EUBOAParty) or
                 (party1_EUBOAParty is not None and party2_BOAParty))
                or
                ((party1_BOAParty is not None and party2_name is not None) or
                 (party1_BOAParty is not None and party2 is not None) or
                 (party1_BOAParty is not None and party2_uncertain) or
                 (party1_BOAParty is not None and party2_EUBOAParty) or
                 (party1_BOAParty is not None and party2_BOAParty))
        ):
            raise TypeError('Selected agents to negotiate each other are wrong! please read manual to select '
                            'correct combination of agents')

        try:
            if isinstance(first_preference, str):
                self.preference1 = Preference(domain_name, first_preference)
            else:
                self.preference1 = first_preference

            if isinstance(second_preference, str):
                self.preference2 = Preference(domain_name, second_preference)
            else:
                self.preference2 = second_preference

            # utility space of first agent (utility_space1) is created regards of utility_space_name1
            utility_space1 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space_name1, self.preference1)

            # utility space of second agent can be None if the user wants to use same utility space name for both
            # agents (if statement), otherwise utility space of first agent (utility_space1) is created regards of
            # utility_space_name2 (else statement)
            if utility_space_name2 is None:
                utility_space2 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space_name1, self.preference2)
            else:
                utility_space2 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space_name2, self.preference2)


            # fdfdfs
            # sfaasf
            # safsdf
            if isinstance(party1_name, str) and party1 is None and party1_uncertain is None and party1_EUBOAParty is None and party1_BOAParty is None:
                # party1_name is the name of first agent which is a string and can be the name of agent which works in
                # certain condition or uncertain condition. this try-except block of code first tries to make an
                # instant of the certain agent if attempt would failed, make an instance of uncertain agent
                try:
                    self.__party1 = CreateObjectByPath.get_object(PARTY_PATH, party1_name, utility_space1)
                except:
                    if user1 is None:
                        raise ValueError("You selected first agent with uncertainty but there is no User!")
                    self.__User1 = CreateObjectByPath.get_object(USER_PATH, user1, self.preference1)
                    self.__initial_preference1 = self.preference1.get_initial_preference()
                    self.__party1 = CreateObjectByPath.get_object(PARTY_PATH, party1_name, self.__initial_preference1, self.__User1)
            elif party1_name is None and isinstance(party1, AbstractNegoParty) and party1_uncertain is None and party1_EUBOAParty is None and party1_BOAParty is None:
                self.__party1 = party1
            elif party1_name is None and party1 is None and isinstance(party1_uncertain, AbstractNegoPartyUncertainCondition) and party1_EUBOAParty is None and party1_BOAParty is None:
                self.__party1 = party1_uncertain
            elif party1_name is None and party1 is None and party1_uncertain is None and isinstance(party1_EUBOAParty, EUBOAParty) and party1_BOAParty is None:
                # since in class of CreateAllAgentsUsingEUBOAComponents, we do not know about the selected user and
                # preferences so we have to set a user for elicitation strategy and preference (initial preference) for
                # the user model and opponent model
                if user1 is None:
                    raise ValueError("You selected first agent with uncertainty but there is no User!")
                else:
                    self.__User1 = CreateObjectByPath.get_object(USER_PATH, user1, self.preference1)
                    party1_EUBOAParty.get_elicitation_strategy().set_user(user=self.__User1)
                initial_preference = self.preference1.get_initial_preference()
                party1_EUBOAParty.get_user_model().set_initial_preference(initial_preference=initial_preference)
                party1_EUBOAParty.get_bidding_strategy().set_user_model(party1_EUBOAParty.get_user_model())
                party1_EUBOAParty.get_opponent_model().set_preference(preference=initial_preference)
                self.__party1 = party1_EUBOAParty
            elif party1_name is None and party1 is None and party1_uncertain is None and party1_EUBOAParty is None and isinstance(party1_BOAParty, BOAParty):
                party1_BOAParty.get_bidding_strategy().set_utility_space(utility_space=utility_space1)
                initial_preference = self.preference1.get_initial_preference()
                party1_BOAParty.get_opponent_model().set_preference(preference=initial_preference)
                party1_BOAParty.get_acceptance_strategy().set_utility_space(utility_space=utility_space1)
                self.__party1 = party1_BOAParty
            else:
                raise TypeError("One of the arguments party1_name or party1 or party1_uncertain should be set")





            # ffdssaf
            # dfsafsf
            # saggfgf
            if isinstance(party2_name, str) and party2 is None and party2_uncertain is None and party2_EUBOAParty is None and party2_BOAParty is None:
                # party1_name is the name of first agent which is a string and can be the name of agent which works in
                # certain condition or uncertain condition. this try-except block of code first tries to make an instant of
                # the certain agent if attempt would failed, make an instance of uncertain agent
                try:
                    self.__party2 = CreateObjectByPath.get_object(PARTY_PATH, party2_name, utility_space2)
                except:
                    if user2 is None:
                        raise ValueError("You selected second agent with uncertainty but there is no User!")
                    self.__User2 = CreateObjectByPath.get_object(USER_PATH, user2, self.preference2)
                    self.__initial_preference2 = self.preference2.get_initial_preference()
                    self.__party2 = CreateObjectByPath.get_object(PARTY_PATH, party2_name, self.__initial_preference2, self.__User2)
            elif party2_name is None and isinstance(party2, AbstractNegoParty) and party2_uncertain is None and party2_EUBOAParty is None and party2_BOAParty is None:
                self.__party2 = party2
            elif party2_name is None and party2 is None and isinstance(party2_uncertain, AbstractNegoPartyUncertainCondition) and party2_EUBOAParty is None and party2_BOAParty is None:
                self.__party2 = party2_uncertain
            elif party2_name is None and party2 is None and party2_uncertain is None and isinstance(party2_EUBOAParty, EUBOAParty) and party2_BOAParty is None:
                # since in class of CreateAllAgentsUsingEUBOAComponents, we do not know about the selected user and
                # preferences so we have to set a user for elicitation strategy and preference (initial preference) for
                # the user model and opponent model
                if user2 is None:
                    raise ValueError("You selected first agent with uncertainty but there is no User!")
                else:
                    self.__User2 = CreateObjectByPath.get_object(USER_PATH, user2, self.preference2)
                    party2_EUBOAParty.get_elicitation_strategy().set_user(user=self.__User2)
                initial_preference = self.preference2.get_initial_preference()
                party2_EUBOAParty.get_user_model().set_initial_preference(initial_preference=initial_preference)
                party2_EUBOAParty.get_bidding_strategy().set_user_model(party2_EUBOAParty.get_user_model())
                party2_EUBOAParty.get_opponent_model().set_preference(preference=initial_preference)
                self.__party2 = party2_EUBOAParty
            elif party2_name is None and party2 is None and party2_uncertain is None and party2_EUBOAParty is None and isinstance(party2_BOAParty, BOAParty):
                party2_BOAParty.get_bidding_strategy().set_utility_space(utility_space=utility_space2)
                initial_preference = self.preference2.get_initial_preference()
                party2_BOAParty.get_opponent_model().set_preference(preference=initial_preference)
                party2_BOAParty.get_acceptance_strategy().set_utility_space(utility_space=utility_space2)
                self.__party2 = party2_BOAParty
            else:
                raise TypeError("One of the arguments party1_name or party1 or party1_uncertain or party1_EUBOAParty should be set")

            time_line = TimeLine(float(deadline), deadline_type)
            state_info = StateInfo(time_line=time_line, my_agent_offers=[], opponent_offers={})

            nego_table = NegoTable(parties=(self.__party1, self.__party2), state_info=state_info)

            self.analysis_man = CreateObjectByPath.get_object(ANALYSIS_PATH,
                                                              analysis_man_name,
                                                              nego_table)

            self.protocol = CreateObjectByPath.get_object(PROTOCOL_PATH,
                                                          protocol_name,
                                                          time_line,
                                                          nego_table,
                                                          self.analysis_man)

        except (ImportError, AttributeError) as e:
            raise ImportError('NegoSim could not import :)', e)

    def start_session(self):
        print('----------------- Negotiation Session -----------------')
        print(self.preference1.get_domain_name(), ',', self.preference2.get_domain_name(), ' -> ', self.__party1.get_name(), '(',
              self.preference1.get_preference_name(), ')', ' Vs ', self.__party2.get_name(), '(',
              self.preference2.get_preference_name(), ')')
        print('-------------------------------------------------------')
        self.protocol.negotiate()
        print('----------------- Negotiation Result -----------------')
        print(self.analysis_man.get_analysis_data())
        print('------------------------------------------------------\n')
        self.analysis_man.save_analysis_data()

    def get_protocol(self):
        return self.protocol

    def get_analysis_man(self):
        return self.analysis_man
