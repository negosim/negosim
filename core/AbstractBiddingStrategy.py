from core.BiddingStrategyInterface import BiddingStrategyInterface
from abc import abstractmethod
from core.Bid import Bid
from core.OpponentModelInterface import OpponentModelInterface
from core.TimeLine import TimeLine
from core.Offer import Offer
import random
from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.UserModelInterface import UserModelInterface


class AbstractBiddingStrategy(BiddingStrategyInterface):

    def __init__(self,
                 opponent_model: OpponentModelInterface,
                 utility_space: AbstractUtilitySpace = None,
                 user_model: UserModelInterface = None):

        """
        This class is used in BOA and EUBOA frameworks. one of the utility_space and user_model
        should be None and the other one should be set.
        :param opponent_model: opponent model
        :param utility_space: if you use BOA framework set this argument otherwise set it None
        :param user_model: if you use EUBOA framework set this argument otherwise set it None
        """

        if not isinstance(opponent_model, OpponentModelInterface):
            raise TypeError('opponent_model argument must be an instance of OpponentModelInterface')
        if not isinstance(utility_space, AbstractUtilitySpace) and utility_space is not None:
            raise TypeError('utility_space argument must be an instance of AdditiveUtilitySpace or None')
        if not isinstance(user_model, UserModelInterface) and user_model is not None:
            raise TypeError('user_model argument must be an instance of AbstractUserModel or None')
        # if (utility_space is None) and (user_model is None):
        #     raise TypeError('utility_space argument or user_model argument must be set with an object (Both of '
        #                     'utility_space argument or user_model argument cannot be None)')
        # if not (utility_space is None) and not (user_model is None):
        #     raise TypeError('at least one of utility_space or user_model must not be None')

        self.__opponent_model = opponent_model
        self.__utility_space = utility_space
        self.__user_model = user_model

        if utility_space is not None:
            self.__preference = utility_space.get_preference()
        elif user_model is not None:
            self.__preference = user_model.get_preference()
        # else:
        #     raise TypeError('at least one of utility_space or user_model must not be None')

    def set_utility_space(self, utility_space: AbstractUtilitySpace):
        if not isinstance(utility_space, AbstractUtilitySpace):
            raise TypeError("utility_space must be an instance of AbstractUtilitySpace")
        # if self.__utility_space is None and self.__user_model is None:
        self.__utility_space = utility_space
        self.__preference = utility_space.get_preference()
        # else:
        #     raise ValueError("One of the utility_space or user_model was set before!")

    def set_user_model(self, user_model: UserModelInterface):
        if not isinstance(user_model, UserModelInterface):
            raise TypeError("user_model mus be type of UserModelInterface")
        # if self.__utility_space is None and self.__user_model is None:
        self.__user_model = user_model
        self.__preference = user_model.get_preference()
        # else:
        #     raise ValueError("One of the utility_space or user_model was set before!")

    def get_utility_space(self) -> AbstractUtilitySpace:
        return self.__utility_space

    @abstractmethod
    def send_bid(self, timeline: TimeLine) -> Bid:
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        """
        This method must return the name of bidding strategy
        :return: the name of bidding strategy
        """
        raise NotImplementedError()

    def get_opponent_model(self):
        return self.__opponent_model

    def get_preference(self):
        return self.__preference

    def generate_random_bid(self):
        issue_items = {}
        preference_data_structure = self.get_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':
                issue_item = list((preference_data_structure[issue][1]).keys())
                issue_items[issue] = random.choice(issue_item)

        bid = Bid(issue_items)
        return bid

    def get_utility(self, bid: Bid) -> float:
        if self.__utility_space is not None:
            return self.__utility_space.get_utility(bid)
        elif self.__user_model is not None:
            return self.__user_model.get_utility(bid)
        else:
            raise TypeError('at least one of utility_space or user_model must not be None')

    def get_utility_distinct(self, offer: Offer) -> float:
        if self.__utility_space is not None:
            return self.__utility_space.get_utility_distinct(offer)
        elif self.__user_model is not None:
            return self.__user_model.get_utility_distinct(offer)
        else:
            raise TypeError('at least one of utility_space or user_model must not be None')
