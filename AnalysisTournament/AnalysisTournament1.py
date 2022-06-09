from core.AbstractTournamentAnalysisMan import AbstractTournamentAnalysisMan
import time
import pickle


class AnalysisTournament1(AbstractTournamentAnalysisMan):

    def get_tournament_analysis_data(self) -> dict:
        '''
        :return: a dict like {
                                'AVG utility1': 0.89,
                                'AVG utility2': 0.75,
                                'AVG socialwelfare': 1.64
                              }
        '''
        session_analysis_dataset = self.get_session_analysis_dataset()
        i = 1
        for session_analysis_data in session_analysis_dataset:
            for key, value in session_analysis_data.items():
                if key.split('_')[0] == 'party1' or key.split('_')[1] == 'SocialWelfare' or key.split('_')[1] == 'opWRMSE':
                    if not isinstance(value, list):
                        if key not in self.tournament_analysis_data:
                            self.tournament_analysis_data[key] = value
                        else:
                            self.tournament_analysis_data[key] = (value + (self.tournament_analysis_data[key] * i)) / (
                                    i + 1)
                            i = i + 1
                    elif key.split('_')[1] == 'opWRMSE':
                        if key not in self.tournament_analysis_data:
                            self.tournament_analysis_data[key] = value[len(value)-1]
                        else:
                            self.tournament_analysis_data[key] = (value[len(value)-1] + (self.tournament_analysis_data[key] * i)) / (
                                    i + 1)
                            i = i + 1

        return self.tournament_analysis_data

