import CreateObjectByPath
from core.NegoTable import NegoTable
from core.Preference import Preference
from configurations import *
from core.StateInfo import StateInfo
from core.TimeLine import TimeLine


class BilateralSession:

    def __init__(self, protocol_name: str, analysis_man_name: str, deadline, deadline_type: str,
                 first_preference, second_preference,
                 party1_name: str, party2_name: str, domain_name: str,
                 utility_space_name1: str, utility_space_name2: str):
        """

        :param protocol_name:
        :param analysis_man_name:
        :param deadline:
        :param deadline_type:
        :param first_preference: should be a name of preference or an preference object
        :param second_preference: should be a name of preference or an preference object
        :param party1_name:
        :param party2_name:
        :param domain_name:
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
        if not isinstance(party1_name, str):
            raise TypeError('party1_name must be a string')
        if not isinstance(party2_name, str):
            raise TypeError('party2_name must be a string')
        if not isinstance(domain_name, str):
            raise TypeError('domain_name must be a string')
        if not isinstance(utility_space_name1, str):
            raise TypeError('utility_space_name1 must be a string')
        if not isinstance(utility_space_name2, str):
            raise TypeError('utility_space_name2 must be a string')

        try:
            if isinstance(first_preference, str):
                self.preference1 = Preference(domain_name, first_preference)
            else:
                self.preference1 = first_preference
            utility_space1 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space_name1, self.preference1)
            self.party1 = CreateObjectByPath.get_object(PARTY_PATH, party1_name, utility_space1)

            if isinstance(second_preference, str):
                self.preference2 = Preference(domain_name, second_preference)
            else:
                self.preference2 = second_preference
            utility_space2 = CreateObjectByPath.get_object(UTILITY_SPACE_PATH, utility_space_name2, self.preference2)
            self.party2 = CreateObjectByPath.get_object(PARTY_PATH, party2_name, utility_space2)

            time_line = TimeLine(float(deadline), deadline_type)
            state_info = StateInfo(time_line=time_line, my_agent_offers=[], opponent_offers={})

            nego_table = NegoTable(parties=(self.party1, self.party2), state_info=state_info)

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
        print(self.preference1.get_domain_name(), ',', self.preference2.get_domain_name(), ' -> ', self.party1, '(',
              self.preference1.get_preference_name(), ')', ' Vs ', self.party2, '(',
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
