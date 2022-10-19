from core.BilateralTournament import BilateralTournament

bilateral_tournament = BilateralTournament(protocol_name='SOAP',
                                           analysis_man_name='Analysis_man0',
                                           Tournament_analysis_name='AnalysisTournament1',
                                           deadline='3',
                                           deadline_type='s',
                                           agent_names=['Boulware'],
                                           opponent_names=['Conceder'],
                                           domain_names=['laptop'],
                                           tournament_repetition='1',
                                           utility_space_names=['AdditiveUtilitySpace'])
bilateral_tournament.start_tournament()
