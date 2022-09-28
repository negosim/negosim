from abc import ABC
from core.Offer import Offer
from core.AbstractElicitationStrategy import AbstractElicitationStrategy
from core.StateInfo import StateInfo
from core.UserModelInterface import UserModelInterface
from core.UserInterface import UserInterface
from core.Preference import Preference


class DefaultElicitationStrategy(AbstractElicitationStrategy, ABC):

    def is_asking_time_from_user(self, state_info: StateInfo):
        """
        This method decides about when and which bid elicit from user
        :param state_info:
        Cal ask_offer_rank_from_user method
        """
        user_model: UserModelInterface = self.get_user_model()
        if self.get_initial_ranked_bids() is None:
            # this line asks initial ranked bids (self.__initial_ranked_bids = initial ranked bids)
            initial_ranked_bids = self.ask_initial_ranked_bids_from_user()
            user_model.generate_initial_preference(initial_ranked_bids=initial_ranked_bids)
        else:
            offers_must_be_asked = user_model.get_must_be_asked_offers()
            if len(offers_must_be_asked) > 0:
                for offer in offers_must_be_asked:
                    self.ask_offer_rank_from_user(offer=offer)
                # ranked_offers = self.get_ranked_bids()
                # ranked_bids = [offer.get_bid() for offer in ranked_offers]
                ranked_bids = self.get_ranked_bids()
                user_model.update_preference(ranked_bids=ranked_bids)

            offers_from_elicitation_strategy = self.simple_elicitation_strategy(user=self.get_user(), user_model=self.get_user_model(), state_info=state_info)
            for offer in offers_from_elicitation_strategy:
                self.ask_offer_rank_from_user(offer=offer)
            ranked_bids = self.get_ranked_bids()
            # ranked_bids = [offer for offer in ranked_offers]
            user_model.update_preference(ranked_bids=ranked_bids)

    def simple_elicitation_strategy(self, user: UserInterface, user_model: UserModelInterface,
                                    state_info: StateInfo) -> list:
        """

        :param user:
        :param user_model:
        :return: which bids must be ask (list of offer)
        """
        preference: Preference = user_model.get_preference()
        total_bothering = user.get_total_bothering()
        if total_bothering <= 0.5:
            random_bid = preference.generate_random_bid()
            if random_bid not in self.get_ranked_bids():
                time = state_info.get_time_line().get_time()
                random_offer = Offer(random_bid, time)
                return [random_offer, ]
