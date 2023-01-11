import unittest
from core.Preference import Preference
from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.TimeLine import TimeLine
from core.StateInfo import StateInfo
from Agents.RandomParty1 import RandomParty1
from Agents.RandomPartyBOA import RandomPartyBOA
from Agents.Boulware import Boulware
from Agents.Conceder import Conceder
from Agents.StupidParty1 import StupidParty1
from analysis.Analysis_man0 import Analysis_man0
from core.NegoTable import NegoTable
from protocols.SOAP import SOAP


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        preference1 = Preference('laptop', 'laptop_buyer_utility.xml')
        utility_space1 = AdditiveUtilitySpace(preference=preference1)
        preference2 = Preference('laptop', 'laptop_seller_utility.xml')
        utility_space2 = AdditiveUtilitySpace(preference=preference2)
        time_line = TimeLine(5.0, 's')
        state_info = StateInfo(time_line, [], {})
        party1 = Boulware(utility_space1)
        party2 = StupidParty1(utility_space2)
        nego_table = NegoTable(state_info, time_line, party1.get_id(), party2.get_id())
        party1.set_nego_table(nego_table=nego_table)
        party2.set_nego_table(nego_table=nego_table)

        analysis_man = Analysis_man0(nego_table, party1, party2)
        self.protocol = SOAP(time_line, nego_table, analysis_man, party1, party2)

    def test_something(self):
        self.protocol.negotiate()


if __name__ == '__main__':
    unittest.main()
