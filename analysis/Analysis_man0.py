from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan


class Analysis_man0(AbstractAnalysisMan):

    def cal_estimation_analysis_data(self) -> dict:
        return None

    def get_analysis_data(self) -> dict:
        '''
        :return: a dict {
                         'Utility party1': 1.000051804171754,
                         'Utility party2': 0.8151053951696905,
                         'Social Welfare': 1.8151571993414446
                         }
        '''

        self.analysis_data_structure = {}

        negotiation_state = self.get_nego_table().get_state_info().get_negotiation_state()
        # preference_party1 = self.get_preference_of_party1()
        # utility_space_party1 = AdditiveUtilitySpace(preference_party1)
        utility_space_party1 = self.get_utility_space_of_party1()
        # preference_party2 = self.get_preference_of_party2()
        # utility_space_party2 = AdditiveUtilitySpace(preference_party2)
        utility_space_party2 = self.get_utility_space_of_party2()
        party1 = self.get_party1()
        party2 = self.get_party2()
        offers_on_table = self.get_nego_table().get_offers_on_table()
        party1_offers = offers_on_table[party1]
        if len(party1_offers) > 0:
            last_offer = party1_offers[len(party1_offers)-1]

            final_utility_party1 = utility_space_party1.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0
            final_utility_party2 = utility_space_party2.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0

            social_welfare = final_utility_party1 + final_utility_party2

            self.analysis_data_structure['party1_'+party1.get_name()] = final_utility_party1
            self.analysis_data_structure['party2_'+party2.get_name()] = final_utility_party2
            self.analysis_data_structure[party1.get_name()+'_SocialWelfare'] = social_welfare

        return self.analysis_data_structure

    def save_analysis_data(self):
        pass