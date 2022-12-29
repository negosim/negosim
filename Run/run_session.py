from core.BilateralSession import BilateralSession
from core.Preference import Preference

preference1 = Preference('Job', 'Jobs_util1.xml')

bilateral_session = BilateralSession(protocol_name='SOAP',
                                     analysis_man_name='Analysis_man0',
                                     deadline='5',
                                     deadline_type='s',
                                     first_preference='Jobs_util1.xml',
                                     second_preference='Jobs_util2.xml',
                                     party1_name='RandomAgentEUBOA2',
                                     party2_name='RandomAgentEUBOA2',
                                     domain_name='Job',
                                     utility_space_name1='AdditiveUtilitySpace',
                                     utility_space_name2='AdditiveUtilitySpace',
                                     user1="DefaultUser",
                                     user2="DefaultUser")


# bilateral_session = BilateralSession(protocol_name='SOAP',
#                                      analysis_man_name='Analysis_man0',
#                                      deadline='5',
#                                      deadline_type='s',
#                                      first_preference='Jobs_util1.xml',
#                                      second_preference='Jobs_util2.xml',
#                                      party1_name='RandomAgentEUBOA2',
#                                      party2_name='RandomPartyBOA',
#                                      domain_name='Job',
#                                      utility_space_name1='AdditiveUtilitySpace',
#                                      utility_space_name2='AdditiveUtilitySpace',
#                                      user1="DefaultUser")


# bilateral_session = BilateralSession(protocol_name='SOAP',
#                                      analysis_man_name='Analysis_man0',
#                                      deadline='5',
#                                      deadline_type='s',
#                                      first_preference='Jobs_util1.xml',
#                                      second_preference='Jobs_util2.xml',
#                                      party1_name='RandomPartyBOA',
#                                      party2_name='RandomAgentEUBOA2',
#                                      domain_name='Job',
#                                      utility_space_name1='AdditiveUtilitySpace',
#                                      utility_space_name2='AdditiveUtilitySpace',
#                                      user2="DefaultUser")


# bilateral_session = BilateralSession(protocol_name='SOAP',
#                                      analysis_man_name='Analysis_man0',
#                                      deadline='5',
#                                      deadline_type='s',
#                                      first_preference='Jobs_util1.xml',
#                                      second_preference='Jobs_util2.xml',
#                                      party1_name='Boulware',
#                                      party2_name='Conceder',
#                                      domain_name='Job',
#                                      utility_space_name1='AdditiveUtilitySpace',
#                                      utility_space_name2='AdditiveUtilitySpace')


bilateral_session.start_session()
