import unittest
from Agents.TimeDependent import TimeDependent
from Agents.RandomParty1 import RandomParty1
from core.Preference import Preference
from protocols.SOAP import SOAP
from core.TimeLine import TimeLine
from core.NegoTable import NegoTable
from core.StateInfo import StateInfo
from analysis.Analysis_man0 import Analysis_man0


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        preference1 = Preference('laptop', 'laptop_buyer_utility.xml')
        preference2 = Preference('laptop', 'laptop_seller_utility.xml')
        self.time_line = TimeLine(1.0, 's')
        self.party1 = TimeDependent(preference1)
        party2 = RandomParty1(preference2)
        parties = (self.party1, party2)
        state_info = StateInfo(self.time_line, [], {})
        nego_table = NegoTable(parties, state_info)
        self.analysis_man = Analysis_man0(self.party1, party2, nego_table, preference1, preference2)
        self.protocol = SOAP(self.time_line, nego_table, self.analysis_man)

    def test_something(self):
        # self.party1.get_bid_space().get_all_bids_with_utility()
        print(self.party1.get_bid_space().get_all_bids_with_utility())
        # print(self.party1.send_bid(self.protocol, self.time_line))
        # self.protocol.negotiate()
        # print('@@@@@@@@@@@@@@@@@@@@@@', self.analysis_man.get_analysis_data())


if __name__ == '__main__':
    unittest.main()
