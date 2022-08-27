from core.AbstractOpponentModel import AbstractOpponentModel
from core.Preference import Preference
from core.Offer import Offer


class DefaultOpponentModel(AbstractOpponentModel):

    def update_preference(self, offer: Offer) -> Preference:
        return self.get_preference()