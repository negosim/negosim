from core.BilateralTournament2 import BilateralTournament

# bilateral_tournament = BilateralTournament(protocol_name='SOAP',
#                                            analysis_man_name='Analysis_man0',
#                                            Tournament_analysis_name='AnalysisTournament1',
#                                            deadline='3',
#                                            deadline_type='s',
#                                            agent_names=['Boulware', 'RandomAgentEUBOA2'],
#                                            opponent_names=['Conceder'],
#                                            domain_names=['laptop'],
#                                            tournament_repetition='1',
#                                            utility_space_names=['AdditiveUtilitySpace'],
#                                            users=['DefaultUser'])

# bilateral_tournament = BilateralTournament(protocol_name='SOAP',
#                                            analysis_man_name='Analysis_man0',
#                                            Tournament_analysis_name='AnalysisTournament1',
#                                            deadline='3',
#                                            deadline_type='s',
#                                            agent_names=['Boulware'],
#                                            opponent_names=[],
#                                            domain_names=['laptop'],
#                                            tournament_repetition='1',
#                                            utility_space_names=['AdditiveUtilitySpace'],
#                                            users=['DefaultUser'],
#                                            elicitation_strategies=['DefaultElicitationStrategy'],
#                                            user_models=['DefaultUserModel'],
#                                            bidding_strategies=['RandomStrategy'],
#                                            opponent_models=['DefaultOpponentModel'],
#                                            acceptance_strategies=['ACNext'],
#                                            EUBOA_is_opponent_side=True)

# bilateral_tournament = BilateralTournament(protocol_name='SOAP',
#                                            analysis_man_name='Analysis_man0',
#                                            Tournament_analysis_name='AnalysisTournament1',
#                                            deadline='3',
#                                            deadline_type='s',
#                                            agent_names=['Boulware'],
#                                            opponent_names=['Conceder'],
#                                            domain_names=['laptop'],
#                                            tournament_repetition='1',
#                                            utility_space_names=['AdditiveUtilitySpace'])





bilateral_tournament = BilateralTournament(protocol_name='SOAP',
                                           analysis_man_name='Analysis_man0',
                                           Tournament_analysis_name='AnalysisTournament1',
                                           deadline='3',
                                           deadline_type='s',
                                           agent_names=[],
                                           opponent_names=['Boulware'],
                                           domain_names=['laptop'],
                                           tournament_repetition='1',
                                           utility_space_names=['AdditiveUtilitySpace'],
                                           users=['DefaultUser'],
                                           elicitation_strategies=['DefaultElicitationStrategy'],
                                           user_models=['DefaultUserModel'],
                                           bidding_strategies=['RandomStrategy'],
                                           opponent_models=['DefaultOpponentModel'],
                                           acceptance_strategies=['ACNext'],
                                           EUBOA_is_agent_side=True)






# bilateral_tournament = BilateralTournament(protocol_name='SOAP',
#                                            analysis_man_name='Analysis_man0',
#                                            Tournament_analysis_name='AnalysisTournament1',
#                                            deadline='3',
#                                            deadline_type='s',
#                                            agent_names=['Conceder', 'RandomAgentEUBOA2'],
#                                            opponent_names=['Boulware', 'RandomAgentEUBOA2'],
#                                            domain_names=['laptop'],
#                                            tournament_repetition='1',
#                                            utility_space_names=['AdditiveUtilitySpace'],
#                                            users=['DefaultUser'],
#                                            elicitation_strategies=['DefaultElicitationStrategy'],
#                                            user_models=['DefaultUserModel'],
#                                            bidding_strategies=['RandomStrategy'],
#                                            opponent_models=['DefaultOpponentModel'],
#                                            acceptance_strategies=['ACNext'],
#                                            EUBOA_is_agent_side=True,
#                                            EUBOA_is_opponent_side=True)

# bilateral_tournament = BilateralTournament(protocol_name='SOAP',
#                                            analysis_man_name='Analysis_man0',
#                                            Tournament_analysis_name='AnalysisTournament1',
#                                            deadline='3',
#                                            deadline_type='s',
#                                            agent_names=['RandomPartyBOA'],
#                                            opponent_names=['Conceder'],
#                                            domain_names=['laptop'],
#                                            tournament_repetition='1',
#                                            utility_space_names=['AdditiveUtilitySpace'])

# bilateral_tournament = BilateralTournament(protocol_name='SOAP',
#                                            analysis_man_name='Analysis_man0',
#                                            Tournament_analysis_name='AnalysisTournament1',
#                                            deadline='3',
#                                            deadline_type='s',
#                                            agent_names=['RandomPartyBOA', 'RandomAgentEUBOA2'],
#                                            opponent_names=['Conceder', 'RandomAgentEUBOA2'],
#                                            domain_names=['laptop'],
#                                            tournament_repetition='1',
#                                            utility_space_names=['AdditiveUtilitySpace'],
#                                            users=['DefaultUser'])

bilateral_tournament.start_tournament()
