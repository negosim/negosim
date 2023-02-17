from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan
from core.Preference import Preference


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

        analysis_data_structure = {}

        negotiation_state = self.get_nego_table().get_state_info().get_negotiation_state()
        # preference_party1 = self.get_preference_of_party1()
        # utility_space_party1 = AdditiveUtilitySpace(preference_party1)
        utility_space_party1 = self.get_utility_space(index=0)
        # preference_party2 = self.get_preference_of_party2()
        # utility_space_party2 = AdditiveUtilitySpace(preference_party2)
        utility_space_party2 = self.get_utility_space(index=1)
        party1 = self.get_party(index=0)
        party2 = self.get_party(index=1)
        offers_on_table = self.get_nego_table().get_offers_on_table()
        party1_offers = offers_on_table[party1.get_id()]

        party1_preference: Preference = party1.get_preference()
        party1_reservation_value = party1_preference.get_reservation()

        party2_preference: Preference = party2.get_preference()
        party2_reservation_value = party2_preference.get_reservation()

        if len(party1_offers) > 0:
            last_offer = party1_offers[len(party1_offers)-1]

            final_utility_party1 = utility_space_party1.get_utility_distinct(last_offer) if negotiation_state == 1 else party1_reservation_value
            final_utility_party2 = utility_space_party2.get_utility_distinct(last_offer) if negotiation_state == 1 else party2_reservation_value

            social_welfare = final_utility_party1 + final_utility_party2

            analysis_data_structure['party1_'+party1.get_name()] = final_utility_party1
            analysis_data_structure['party2_'+party2.get_name()] = final_utility_party2
            analysis_data_structure[party1.get_name()+'_SocialWelfare'] = social_welfare
        else:
            analysis_data_structure['party1_' + party1.get_name()] = party1_reservation_value
            analysis_data_structure['party2_' + party2.get_name()] = party2_reservation_value
            social_welfare = party1_reservation_value + party2_reservation_value
            analysis_data_structure[party1.get_name() + '_SocialWelfare'] = social_welfare

        return analysis_data_structure

    def save_analysis_data(self):
        pass