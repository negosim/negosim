import unittest
from core.NegoTable import NegoTable
from core.NegoPartyInterface import NegoPartyInterface
from unittest.mock import Mock
from core.StateInfo import StateInfo
from core.Offer import Offer


class TestNegoTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.party1 = Mock(spec_set=NegoPartyInterface)
        cls.party2 = Mock(spec_set=NegoPartyInterface)
        cls.parties = (cls.party1, cls.party2)
        cls.state_info = Mock(spec_set=StateInfo)
        cls.nego_table = NegoTable(cls.parties, cls.state_info)

    def test_NegoTable_initialize(self):
        self.assertRaises(TypeError, NegoTable, {}, '')
        self.assertRaises(TypeError, NegoTable, [], '')

        party = Mock(spec_set=NegoPartyInterface)
        parties = (party,)
        state_info = Mock(spec_set=StateInfo)
        self.assertRaises(TypeError, NegoTable, party, state_info)
        self.assertIsInstance(NegoTable(parties, state_info), NegoTable)

    def test_get_state_info(self):
        party = Mock(spec_set=NegoPartyInterface)
        parties = (party,)
        state_info = Mock(spec_set=StateInfo)
        nego_table = NegoTable(parties, state_info)
        self.assertIsInstance(nego_table.get_state_info(), StateInfo)

    # def test_is_table_empty(self):
    #     self.assertTrue(TestNegoTable.nego_table.is_table_empty())
    #     offer1 = Mock(spec_set=Offer)
    #     TestNegoTable.nego_table.add_offer(TestNegoTable.party1, offer1)
    #     self.assertFalse(TestNegoTable.nego_table.is_table_empty())

    def test_get_parties(self):
        parties = TestNegoTable.nego_table.get_parties()
        self.assertIsInstance(parties, tuple)
        for party in parties:
            self.assertIsInstance(party, NegoPartyInterface)

    # def test_get_offers_on_table(self):
    #     print(TestNegoTable.nego_table.get_offers_on_table())
    #     offer1 = Mock(spec_set=Offer)
    #     TestNegoTable.nego_table.add_offer(TestNegoTable.party1, offer1)
    #     print(TestNegoTable.nego_table.get_offers_on_table())


    # def test_add_offer(self):
    #     offer1 = Mock(spec_set=Offer)
    #     TestNegoTable.nego_table.add_offer(TestNegoTable.party1, offer1)


if __name__ == '__main':
    unittest.main()
