from core.BilateralSession import BilateralSession
from core.Preference import Preference

preference1 = Preference('Job', 'Jobs_util1.xml')

bilateral_session = BilateralSession(protocol_name='SOAP',
                                     analysis_man_name='Analysis_man0',
                                     deadline='5',
                                     deadline_type='s',
                                     first_preference='Jobs_util1.xml',
                                     second_preference='Jobs_util2.xml',
                                     party1_name='Boulware',
                                     party2_name='Conceder',
                                     domain_name='Job')
bilateral_session.start_session()