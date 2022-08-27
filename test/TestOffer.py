import unittest
from unittest.mock import Mock
from core.Offer import Offer
from core.Bid import Bid


class TestOffer(unittest.TestCase):

    def test_offer_initialize(self):
        self.assertRaises(TypeError, Offer, None, '')

    def test_get_bid(self):
        bid = Mock(spec=Bid)
        offer = Offer(bid, 1.0)
        self.assertTrue(isinstance(offer.get_bid(), Bid))

    def test_get_time(self):
        bid = Mock(spec_set=Bid)
        offer = Offer(bid, 1.0)
        self.assertEqual(offer.get_time(), 1.0)


if __name__ == '__main__':
    unittest.main()