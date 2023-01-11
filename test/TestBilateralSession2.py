import unittest
from core.BilateralSession2 import BilateralSession


class MyTestCase(unittest.TestCase):

    def test_something(self):
        # bilateral_session = BilateralSession(protocol_name='SOAP',
        #                                      analysis_man_name='Analysis_man0',
        #                                      deadline='5',
        #                                      deadline_type='s',
        #                                      first_preference='Jobs_util1.xml',
        #                                      second_preference='Jobs_util2.xml',
        #                                      party1_name='RandomPartyBOA',
        #                                      party2_name='Conceder',
        #                                      domain_name='Job',
        #                                      utility_space_name1='AdditiveUtilitySpace',
        #                                      utility_space_name2='AdditiveUtilitySpace')

        bilateral_session = BilateralSession(protocol_name='SOAP',
                                             analysis_man_name='Analysis_man0',
                                             deadline='5',
                                             deadline_type='s',
                                             first_preference='Jobs_util1.xml',
                                             second_preference='Jobs_util2.xml',
                                             party1_name='RandomPartyBOA',
                                             party2_name='RandomAgentEUBOA2',
                                             domain_name='Job',
                                             utility_space_name1='AdditiveUtilitySpace',
                                             utility_space_name2='AdditiveUtilitySpace',
                                             user2="DefaultUser")

        bilateral_session.start_session()


if __name__ == '__main__':
    unittest.main()
