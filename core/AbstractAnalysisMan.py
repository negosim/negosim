import pickle
import time
from abc import ABC, abstractmethod
from pathlib import Path

from core.UserModelInterface import UserModelInterface
from core.Preference import Preference
from core.OpponentModelInterface import OpponentModelInterface
from core.NegoTable import NegoTable
from core.NegoPartyInterface import NegoPartyInterface


class AbstractAnalysisMan(ABC):
    '''
    analysis_data_structure = {
        'parties_utility': {party1: 0.74, party2: 0.85},
        'social_welfare': 1.59,
        ...
    }
    '''

    def __init__(self, nego_table):
        # if not isinstance(party1, NegoPartyInterface):
        #     raise TypeError('party1 argument must be an instance of NegoPartyInterface')
        # if not isinstance(party2, NegoPartyInterface):
        #     raise TypeError('party2 argument must be an instance of NegoPartyInterface')
        if not isinstance(nego_table, NegoTable):
            raise TypeError('offers_on_table argument must be an instance of dict')
        # if not isinstance(preference_of_party1, Preference):
        #     raise TypeError('preference_of_party1 argument must be an instance of NegoPartyInterface')
        # if not isinstance(preference_of_party2, Preference):
        #     raise TypeError('preference_of_party2 argument must be an instance of NegoPartyInterface')
        # if not (isinstance(opponent_model_party1, OpponentModelInterface) or opponent_model_party1 == None):
        #     raise TypeError('estimated_preference_of_party1 argument must be an instance of Preference')
        # if not (isinstance(opponent_model_party2, OpponentModelInterface) or opponent_model_party2 == None):
        #     raise TypeError('estimated_preference_of_party2 argument must be an instance of Preference')
        # if not (isinstance(user_model_party1, UserModelInterface) or user_model_party1 == None):
        #     raise TypeError('estimated_preference_of_party2 argument must be an instance of Preference')
        # if not (isinstance(user_model_party2, UserModelInterface) or user_model_party2 == None):
        #     raise TypeError('estimated_preference_of_party2 argument must be an instance of Preference')

        self.__nego_table = nego_table
        self.__party1: NegoPartyInterface = nego_table.get_parties()[0]
        self.__party2: NegoPartyInterface = nego_table.get_parties()[1]
        self.__preference_of_party1 = self.__party1.get_preference()
        self.__preference_of_party2 = self.__party2.get_preference()
        self.__opponent_model_party1 = self.__party1.get_opponent_model()
        self.__opponent_model_party2 = self.__party2.get_opponent_model()
        self.__user_model_party1 = self.__party1.get_user_model()
        self.__user_model_party2 = self.__party2.get_user_model()
        self.estimation_analysis_data_structure = {}
        self.analysis_data_structure = {}

    def get_party1(self):
        return self.__party1

    def get_party2(self):
        return self.__party2

    def get_nego_table(self):
        return self.__nego_table

    def get_preference_of_party1(self):
        return self.__preference_of_party1

    def get_preference_of_party2(self):
        return self.__preference_of_party2

    def get_opponent_model_party1(self):
        return self.__opponent_model_party1

    def get_opponent_model_party2(self):
        return self.__opponent_model_party2

    def get_user_model_party1(self):
        return self.__user_model_party1

    def get_user_model_party2(self):
        return self.__user_model_party2

    @abstractmethod
    def cal_estimation_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''
        raise NotImplementedError()

    def save_analysis_data(self):
        file_name = 'sessionData_pickled' + str(time.strftime('%Y%m%d-%H%M%S'))
        log_dir = Path("logs")
        if not log_dir.exists():
            log_dir.mkdir(parents=True)
        session_data = open(f'./logs/{file_name}', 'ab')
        data = self.analysis_data_structure if len(self.analysis_data_structure) > 0 else self.get_analysis_data()
        pickle.dump(data, session_data)
        session_data.close()
