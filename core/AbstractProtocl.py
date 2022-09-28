from core.ProtocolInterface import ProtocolInterface
from abc import abstractmethod
from core.TimeLine import TimeLine
from core.NegoTable import NegoTable
from core.NegoPartyInterface import NegoPartyInterface
from core.AbstractAnalysisMan import AbstractAnalysisMan


class AbstractProtocol(ProtocolInterface):

    def __init__(self, time_line: TimeLine, nego_table: NegoTable, analysis_man: AbstractAnalysisMan):
        if not isinstance(time_line, TimeLine):
            raise TypeError('time_line argument must be an instance of TimeLine')
        if not isinstance(nego_table, NegoTable):
            raise TypeError('nego_table argument must be an instance of NegoTable')
        if not isinstance(analysis_man, AbstractAnalysisMan):
            raise TypeError('analysis_man argument must be an instance of AbstractAnalysisMan')
        self.__time_line = time_line
        self.__nego_table = nego_table
        self.__analysis_man = analysis_man

    @abstractmethod
    def negotiate(self):
        """This method ask a bid from party according to order and negotiation state then
        convert it to offer and add it to the table offers and update negotiation state

           negotiation state will be 1 if the last parties' offer are same
           negotiation state will be 0 if the last parties' offer are not same
           negotiation state will be -1 if the one of last parties' offer's Bid is {}
        """
        raise NotImplementedError()

    @abstractmethod
    def get_offers_on_table(self, party_name: str) -> tuple:
        """This method gets a party name in string type and returns a tuple of offers
        related to the party name that has got through the object that has called the
        method.
           Before returning the offers, the method checks out whether the object that
        has called the method has authority to access the offers or not? if there is no
        permission it returns an error.
        """
        raise NotImplementedError()

    def get_time(self) -> float:
        return self.__time_line.get_time()

    def get_time_line(self) -> TimeLine:
        return self.__time_line

    def get_nego_table(self) -> NegoTable:
        return self.__nego_table

    def get_parties(self) -> tuple:
        return self.__nego_table.get_parties()

    def get_analysis_man(self):
        return self.__analysis_man

    def get_state_info(self):
        return self.__nego_table.get_state_info()