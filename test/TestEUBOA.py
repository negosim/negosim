import unittest
from Agents.RandomAgentEUBOA2 import RandomAgentEUBOA2
from Agents.RandomParty1 import RandomParty1
from Agents.Boulware import Boulware
from users.DefaultUser import DefaultUser
from core.Preference import Preference
from protocols.SOAP import SOAP
from core.TimeLine import TimeLine
from core.NegoTable import NegoTable
from core.StateInfo import StateInfo
from analysis.Analysis_man0 import Analysis_man0
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        preference1 = Preference('laptop', 'laptop_buyer_utility.xml')
        initial_preference_1 = preference1.get_initial_preference()
        # utility_space1 = AdditiveUtilitySpace(preference=initial_preference_1)
        preference2 = Preference('laptop', 'laptop_seller_utility.xml')
        utility_space2 = AdditiveUtilitySpace(preference=preference2)
        user = DefaultUser(preference=preference1)
        time_line = TimeLine(5.0, 's')
        party1 = RandomAgentEUBOA2(preference=initial_preference_1, user=user)
        party2 = Boulware(utility_space2)
        # parties = (self.party1, party2)
        state_info = StateInfo(time_line, [], {})
        nego_table = NegoTable(state_info, time_line, party1.get_id(), party2.get_id())
        party1.set_nego_table(nego_table=nego_table)
        party2.set_nego_table(nego_table=nego_table)
        analysis_man = Analysis_man0(nego_table, party1, party2)
        self.protocol = SOAP(time_line, nego_table, analysis_man, party1, party2)

    def test_something(self):
        self.protocol.negotiate()
        # pass

if __name__ == '__main__':
    unittest.main()
