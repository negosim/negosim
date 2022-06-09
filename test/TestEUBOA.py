import unittest
from Agents_uncertainty.RandomAgentEUBOA import RandomAgentEUBOA
from Agents.RandomParty1 import RandomParty1
from users.DefaultUser import DefaultUser
from core.Preference import Preference
from protocols.SOAP import SOAP
from core.TimeLine import TimeLine
from core.NegoTable import NegoTable
from core.StateInfo import StateInfo
from analysis.Analysis_man0 import Analysis_man0


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        preference1 = Preference('laptop', 'laptop_buyer_utility.xml')
        initial_preference_1 = preference1.get_initial_preference()
        preference2 = Preference('laptop', 'laptop_seller_utility.xml')
        user = DefaultUser(preference=preference1)
        self.time_line = TimeLine(1.0, 's')
        self.party1 = RandomAgentEUBOA(initial_preference=initial_preference_1, user=user)
        party2 = RandomParty1(preference2)
        parties = (self.party1, party2)
        state_info = StateInfo(self.time_line, [], {})
        nego_table = NegoTable(parties, state_info)
        self.analysis_man = Analysis_man0(self.party1, party2, nego_table, preference1, preference2)
        self.protocol = SOAP(self.time_line, nego_table, self.analysis_man)

    def test_something(self):
        self.protocol.negotiate()


if __name__ == '__main__':
    unittest.main()
