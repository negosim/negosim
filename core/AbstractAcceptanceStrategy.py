from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.Offer import Offer
from abc import abstractmethod
from core.AbstractUtilitySpace import AbstractUtilitySpace
from core.OpponentModelInterface import OpponentModelInterface
from core.Bid import Bid
from core.AbstractUserModel import AbstractUserModel
from core.UserModelInterface import UserModelInterface


class AbstractAcceptanceStrategy(AcceptanceStrategyInterface):

    def __init__(self, utility_space: AbstractUtilitySpace = None, user_model: UserModelInterface = None):
        """
        this class is used in BOA and EUBOA frameworks. one of the utility_space and user_model
        should be None and the other one should be set.
        :param utility_space: if you use BOA framework set this argument otherwise set it None
        :param user_model: if you use EUBOA framework set this argument otherwise set it None
        """
        if not isinstance(utility_space, AbstractUtilitySpace) and utility_space is not None:
            raise TypeError('utility_space argument must be an instance of AbstractUtilitySpace or None')
        if not isinstance(user_model, UserModelInterface) and user_model is not None:
            raise TypeError('user_model argument must be an instance of AbstractUserModel or None')
        # if (utility_space is None) and (user_model is None):
        #     raise TypeError('utility_space argument or user_model argument must be set with an object (Both of '
        #                     'utility_space argument or user_model argument cannot be None)')
        # if not (utility_space is None) and not (user_model is None):
        #     raise TypeError('at least one of utility_space or user_model must not be None')

        self.__utility_space = utility_space
        self.__user_model = user_model

    def set_utility_space(self, utility_space: AbstractUtilitySpace):
        if not isinstance(utility_space, AbstractUtilitySpace):
            raise TypeError("utility_space must be an instance of AbstractUtilitySpace")
        # if self.__utility_space is None and self.__user_model is None:
        self.__utility_space = utility_space
        # else:
        #     raise ValueError("One of the utility_space or user_model was set before!")

    def set_user_model(self, user_model):
        if not isinstance(user_model, UserModelInterface):
            raise TypeError("user_model mus be type of UserModelInterface")
        if self.__utility_space is None and self.__user_model is None:
            self.__user_model = user_model
        else:
            raise ValueError("One of the utility_space or user_model was set before!")

    @abstractmethod
    def is_acceptable(self, offer: Offer, my_next_bid: Bid, opponent_model: OpponentModelInterface) -> int:
        """this method returns 0 refer to reject opponent's offer or 1 refer to accept
        opponent offer.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        """
        this method must return the name of acceptance strategy
        :return: name of acceptance strategy
        """
        raise NotImplementedError()

    def get_utility_space(self):
        return self.__utility_space

    def get_user_model(self):
        return self.__user_model

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
