from abc import ABC, abstractmethod
from core.Bid import Bid
from core.AbstractNegoPartyUncertainCondition import AbstractNegoPartyUncertainCondition
from core.ElicitationStrategyInterface import ElicitationStrategyInterface
from core.UserInterface import UserInterface
import CreateObjectByPath
from configurations import *
from core.Preference import Preference
from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.UserModelInterface import UserModelInterface
from core.BiddingStrategyInterface import BiddingStrategyInterface
from core.OpponentModelInterface import OpponentModelInterface


class EUBOAParty(AbstractNegoPartyUncertainCondition, ABC):

    def __init__(self,
                 user_model: str,
                 elicitation_strategy: str,
                 opponent_model: str,
                 bidding_strategy: str,
                 acceptance_strategy: str, preference: Preference = None,
                 user: UserInterface = None):

        super(EUBOAParty, self).__init__(preference=preference, user=user)
        self.__user = self.get_user()
        if self.get_p() is not None:
            self.initial_preference_user_model = self.get_initial_preference()
            self.initial_preference_opponent_model = self.initial_preference_user_model.__copy__()

            self.__user_model = CreateObjectByPath.get_object(USER_MODEL_PATH, user_model, self.initial_preference_user_model)
            self.__elicitation_strategy = CreateObjectByPath.get_object(ELICITATION_STRATEGIES_PATH, elicitation_strategy, self.__user, self.__user_model)
            self.__opponent_model = CreateObjectByPath.get_object(OPPONENT_MODEL_PATH, opponent_model, self.initial_preference_opponent_model)
            self.__bidding_strategy = CreateObjectByPath.get_object(BIDDING_STRATEGIES_PATH, bidding_strategy, self.__opponent_model, None, self.__user_model)
            self.__acceptance_strategy = CreateObjectByPath.get_object(ACCEPTANCE_STRATEGIES_PATH, acceptance_strategy, None, self.__user_model)
        else:
            # raise ValueError("(Initial) preference was not set")
            self.initial_preference_user_model = None
            self.initial_preference_opponent_model = None

            self.__user_model = CreateObjectByPath.get_object(USER_MODEL_PATH, user_model, self.initial_preference_user_model)
            self.__elicitation_strategy = CreateObjectByPath.get_object(ELICITATION_STRATEGIES_PATH, elicitation_strategy, self.__user, self.__user_model)
            self.__opponent_model = CreateObjectByPath.get_object(OPPONENT_MODEL_PATH, opponent_model, self.initial_preference_opponent_model)
            # self.__bidding_strategy = CreateObjectByPath.get_object(BIDDING_STRATEGIES_PATH, bidding_strategy, self.__opponent_model, None, self.__user_model)
            self.__bidding_strategy = CreateObjectByPath.get_object(BIDDING_STRATEGIES_PATH, bidding_strategy, self.__opponent_model, None, None)
            self.__acceptance_strategy = CreateObjectByPath.get_object(ACCEPTANCE_STRATEGIES_PATH, acceptance_strategy, None, self.__user_model)

    def get_elicitation_strategy(self) -> ElicitationStrategyInterface:
        return self.__elicitation_strategy

    def get_user_model(self) -> UserModelInterface:
        """
        This method can be used for analysing purpose
        if this method returns user model this means the
        analysis entity should analyze the user model otherwise
        if it returns None means the analysis entity would not analyze
        the opponent modeling
        :return: user model
        """
        return self.__user_model

    def get_bidding_strategy(self) -> BiddingStrategyInterface:
        return self.__bidding_strategy

    def get_opponent_model(self) -> OpponentModelInterface:
        """
        This method can be used for analysing purpose
        if this method returns opponent model this means the
        analysis entity should analyze the opponent model otherwise
        if it returns None means the analysis entity would not analyze
        the opponent modeling
        :return: opponent model
        """
        return self.__opponent_model

    def get_acceptance_strategy(self) -> AcceptanceStrategyInterface:
        return self.__acceptance_strategy

    def get_preference(self):
        return self.get_user_model().get_preference()


    def send_bid(self, protocol) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        state_info = protocol.get_state_info()
        self.__elicitation_strategy.is_asking_time_from_user(state_info=state_info)

        parties = protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponent_offers = protocol.get_offers_on_table(opponent)
        bid = self.__bidding_strategy.send_bid(protocol.get_time_line())
        if len(opponent_offers) > 0:
            op_offer = opponent_offers[-1]
            self.__opponent_model.update_preference(op_offer)
            if self.__acceptance_strategy.is_acceptable(offer=op_offer, my_next_bid=bid,
                                                        opponent_model=self.__opponent_model):
                return op_offer.get_bid()
        return bid

    @abstractmethod
    def get_name(self):
        """
        :return: Party Name
        """
        raise NotImplementedError()
