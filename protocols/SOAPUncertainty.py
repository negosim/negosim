from core.AbstractProtocl import AbstractProtocol
from core.Offer import Offer
from core.AbstractNegoPartyUncertainCondition import AbstractNegoPartyUncertainCondition


class SOAPUncertainty(AbstractProtocol):

    def negotiate(self):
        """This method ask a bid from party according to order and negotiation state then
        convert it to offer and add it to the table offers and update negotiation state

           negotiation state will be 1 if the last parties' offer are same
           negotiation state will be 0 if the last parties' offer are not same
           negotiation state will be -1 if the one of last parties' offer's Bid is {} or deadline was reached
        """
        parties = self.get_nego_table().get_parties()
        for party in parties:
            if not isinstance(party, AbstractNegoPartyUncertainCondition):
                raise TypeError("Party must be an instance of AbstractNegoPartyUncertainCondition class")

        while self.get_nego_table().get_state_info().get_negotiation_state() == 0:
            parties = self.get_nego_table().get_parties()
            for party in parties:
                if self.get_time_line().is_time_ended():
                    self.get_nego_table().get_state_info().set_negotiation_state(-1)
                if self.get_nego_table().get_state_info().get_negotiation_state() == 0:
                    bid = party.send_bid(self, self.get_time_line())
                    offer = Offer(bid, self.get_time())
                    self.get_nego_table().add_offer(party, offer)
                    print(party.get_name(), ' -> ', offer)
                    self.get_analysis_man().cal_estimation_analysis_data()
                if self.is_agreement() is True:
                    self.get_nego_table().get_state_info().set_negotiation_state(1)
                    print("Negotiation was ended due to reaching Agreement!")
                    break
                if self.get_time() >= 1.0:
                    self.get_nego_table().get_state_info().set_negotiation_state(-1)
                    print("Negotiation was ended due to reaching deadline!")
                    break

    def is_agreement(self):
        """
        :return: True if all parties lats offer is same
        """
        parties = self.get_nego_table().get_parties()
        bids_issues_items = []
        for party in parties:
            party_offers = self.get_nego_table().get_offers_on_table()[party]
            if len(party_offers) == 0:
                return False
            bids_issues_items.append(party_offers[len(party_offers)-1].get_bid().get_issues_items())

        # print('is_agreement ', bids_issues_items)
        if bids_issues_items.count(bids_issues_items[len(bids_issues_items)-1]) == len(bids_issues_items):
            # print('is_agreement ', 'True')
            return True
        # print('is_agreement ', 'False')
        return False

    def get_offers_on_table(self, party) -> tuple:
        """This method gets a party name in string type and returns a tuple of offers
        related to the party name that has got through the object that has called the
        method.
           Before returning the offers, the method checks out whether the object that
        has called the method has authority to access the offers or not? if there is no
        permission it returns an error.

        This protocol lets all parties knows each other offers
        """
        return self.get_nego_table().get_offers_on_table()[party]