import unittest
from Agents.RandomPartyBOA import RandomPartyBOA
from Agents.RandomParty1 import RandomParty1
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
        utility_space1 = AdditiveUtilitySpace(preference=initial_preference_1)
        preference2 = Preference('laptop', 'laptop_seller_utility.xml')
        utility_space2 = AdditiveUtilitySpace(preference=preference2)
        self.time_line = TimeLine(5.0, 's')
        self.party1 = RandomPartyBOA(utility_space=utility_space1)
        party2 = RandomParty1(utility_space2)
        parties = (self.party1, party2)
        state_info = StateInfo(self.time_line, [], {})
        nego_table = NegoTable(parties, state_info)
        self.analysis_man = Analysis_man0(nego_table)
        self.protocol = SOAP(self.time_line, nego_table, self.analysis_man)

    def test_something(self):
        self.protocol.negotiate()


if __name__ == '__main__':
    unittest.main()
