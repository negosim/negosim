from elicitation_strategies.default_elicitation_strategy import DefaultElicitationStrategy
from core.AbstractNegoPartyUncertainCondition import AbstractNegoPartyUncertainCondition
from opponent_models.DefaultOpponentModel import DefaultOpponentModel
from bidding_strategies.RandomStrategy import RandomStrategy
from user_models.default_user_model import DefaultUserModel
from core.ProtocolInterface import ProtocolInterface
from acceptance_strategies.ACNext import ACNext
from core.UserInterface import UserInterface
from core.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.Preference import Preference
from core.TimeLine import TimeLine
from core.Bid import Bid


class RandomAgentEUBOA(AbstractNegoPartyUncertainCondition):

    def __init__(self, initial_preference: Preference, user: UserInterface):
        super(RandomAgentEUBOA, self).__init__(initial_preference=initial_preference, user=user)
        self.__user = self.get_user()
        self.initial_preference_user_model = self.get_initial_preference()
        self.initial_preference_opponent_model = self.initial_preference_user_model.__copy__()

        self.__user_model = DefaultUserModel(self.initial_preference_user_model)
        self.__elicitation_strategy = DefaultElicitationStrategy(user=self.__user, user_model=self.__user_model)
        self.__opponent_model = DefaultOpponentModel(self.initial_preference_opponent_model)
        self.__bidding_strategy = RandomStrategy(opponent_model=self.__opponent_model,
                                                 preference=self.initial_preference_user_model)
        self.__acceptance_strategy = ACNext(utility_space=AdditiveUtilitySpace(self.initial_preference_user_model))

    def send_bid(self, protocol: ProtocolInterface) -> Bid:
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

    def get_name(self):
        """
        :return: Party Name
        """
        return "DefaultAgentEUBOA"

    def get_opponent_model(self):
        """
        This method can be used for analysing purpose
        if this method returns opponent model this means the
        analysis entity should analyze the opponent model otherwise
        if it returns None means the analysis entity would not analyze
        the opponent modeling
        :return: opponent model
        """
        return self.__opponent_model

    def get_user_model(self):
        """
        This method can be used for analysing purpose
        if this method returns user model this means the
        analysis entity should analyze the user model otherwise
        if it returns None means the analysis entity would not analyze
        the opponent modeling
        :return: user model
        """
        return self.__user_model


    def get_preference(self):
        return self.get_user_model().get_preference()