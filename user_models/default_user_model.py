from core.Preference import Preference
from core.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.AbstractUserModel import AbstractUserModel
from core.Offer import Offer


class DefaultUserModel(AbstractUserModel):

    """
    this class implements very simple user model
    which adds 1 to a value of item in spacial issue
    """

    def __init__(self, initial_preference: Preference):
        super().__init__(initial_preference)
        self.initial_preference = initial_preference

    def generate_initial_preference(self, initial_ranked_bids) -> Preference:
        self.initial_preference = self.get_initial_preference()
        return self.generate_preference(ranked_bids=initial_ranked_bids)

    def get_utility(self, offer: Offer) -> float:
        utility_space: AdditiveUtilitySpace = AdditiveUtilitySpace(preference=self.initial_preference)
        return utility_space.get_utility_distinct(offer=offer)

    def update_preference(self, ranked_bids: list) -> Preference:
        return self.generate_preference(ranked_bids=ranked_bids)

    def generate_preference(self, ranked_bids: list) -> Preference:
        """
        preference_data_structure = {
            'Brand': [0.33, {'Lenovo': 1, 'Assus': 1, 'Mac': 1}],
            'Monitor': [0.33, {'15': 1, '10': 1, '11': 1}],
            'HDD': [0.33, {'1T': 1, '2T': 1, '3T': 1}],
            'discount factor = 1,
            'reservation value = 0
        }
            bid1 = {
                'Brand': 'Lenovo',
                'Monitor': '11',
                'HDD': '1T'
            },
            bid2 = {
                'Brand': 'Assus',
                'Monitor': '10',
                'HDD': '2T'
            },
            bid3 = {
                'Brand': 'Mac',
                'Monitor': '15',
                'HDD': '3T'
            }
            ranked_bids = [bid1, bid2, bid3]
            bid1 <= bid2 <= bid3
        """
        num_of_bids = len(ranked_bids)
        for i in range(num_of_bids):
            bid = ranked_bids[-1*(i+1)]
            for issue, item in bid.get_issues_items().items():
                old_value, _ = self.initial_preference.get_issue_item_value(issue=issue, item=item)
                new_value = old_value + 1
                self.initial_preference.update_value(new_value=new_value, issue=issue, item=item)
        return self.initial_preference
