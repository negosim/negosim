import pickle
import time
from abc import ABC, abstractmethod
from pathlib import Path


class AbstractTournamentAnalysisMan(ABC):

    def __init__(self, agent_names: list):
        self.__agent_names = agent_names
        self.__session_analysis_dataset = []  # list of session analysis data
        self.tournament_analysis_data = {}

    def get_agent_names(self):
        return self.__agent_names

    def add_session_analysis_data(self, session_analysis_data):
        self.__session_analysis_dataset.append(session_analysis_data)

    def get_session_analysis_dataset(self):
        return self.__session_analysis_dataset

    @abstractmethod
    def get_tournament_analysis_data(self) -> dict:
        '''
        :return: a dict like {
                                'utility1': 0.89,
                                'utility2': 0.75,
                                'socialwelfare': 1.64
                              }
        '''
        raise NotImplementedError()


    def save_analysis_data(self):
        file_name = 'TournamentData_pickled' + str(time.strftime('%Y%m%d-%H%M%S'))
        log_dir = Path("TournamentLogs")
        if not log_dir.exists():
            log_dir.mkdir(parents=True)
        tournament_data = open(f'./TournamentLogs/{file_name}', 'ab')
        data = self.tournament_analysis_data if len(self.tournament_analysis_data) > 0 else self.tournament_analysis_data
        pickle.dump(data, tournament_data)
        tournament_data.close()