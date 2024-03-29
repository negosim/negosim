from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan
import math
from statistics import mean


class AnalysisMan2(AbstractAnalysisMan):

    def cal_estimation_analysis_data(self) -> dict:
        self.estimation_analysis_data_structure = {}
        preference_party1 = self.get_preference(index=0)
        preference_party2 = self.get_preference(index=1)
        if self.get_opponent_model(index=0) != None:
            estimated_preference = self.get_opponent_model(index=0).get_preference()
            total = 0
            issue_weights = preference_party1.get_weights()

            for issue, weight in issue_weights.items():
                item_value = preference_party1.get_issue_ItemValue(issue=issue)
                estimated_item_value = estimated_preference.get_issue_ItemValue(issue=issue)
                avg_values = mean(float(x) for x in item_value.values())
                for item, _ in item_value.items():
                    v = avg_values - float(estimated_item_value[item])
                    total += float(weight) * (v ** 2)
            wrmse1 = math.sqrt(total)
            if not (self.get_party(index=0).get_name()+'_opWRMSE') in self.estimation_analysis_data_structure:
                self.estimation_analysis_data_structure[self.get_party(index=0).get_name()+'_opWRMSE'] = [wrmse1]
            else:
                self.estimation_analysis_data_structure[self.get_party(index=0).get_name()+'_opWRMSE'].append(wrmse1)

        if self.get_opponent_model(index=1) != None:
            estimated_preference = self.get_opponent_model(index=1).get_preference()
            total = 0
            issue_weights = preference_party2.get_weights()

            for issue, weight in issue_weights.items():
                item_value = preference_party2.get_issue_ItemValue(issue=issue)
                estimated_item_value = estimated_preference.get_issue_ItemValue(issue=issue)
                avg_values = mean(float(x) for x in item_value.values())
                for item, _ in item_value.items():
                    v = avg_values - float(estimated_item_value[item])
                    total += float(weight) * (v ** 2)
            wrmse2 = math.sqrt(total)
            if not (self.get_party(index=1).get_name()+'_opWRMSE') in self.estimation_analysis_data_structure:
                self.estimation_analysis_data_structure[self.get_party(index=1).get_name()+'_opWRMSE'] = wrmse2
            else:
                self.estimation_analysis_data_structure[self.get_party(index=1).get_name()+'_opWRMSE'].append(wrmse2)
        return self.estimation_analysis_data_structure

    def get_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''

        analysis_data_structure = {}

        negotiation_state = self.get_nego_table().get_state_info().get_negotiation_state()
        preference_party1 = self.get_preference(index=0)
        reservation_value_party1 = preference_party1.get_reservation()
        utility_space_party1 = AdditiveUtilitySpace(preference_party1)
        preference_party2 = self.get_preference(index=1)
        reservation_value_party2 = preference_party2.get_reservation()
        utility_space_party2 = AdditiveUtilitySpace(preference_party2)
        party1 = self.get_party(index=0)
        party2 = self.get_party(index=1)
        offers_on_table = self.get_nego_table().get_offers_on_table()
        party1_offers = offers_on_table[party1.get_id()]
        party2_offers = offers_on_table[party2.get_id()]
        last_offer = party1_offers[len(party1_offers) - 1]

        final_utility_party1 = utility_space_party1.get_utility_distinct(last_offer) if negotiation_state == 1 else reservation_value_party1
        final_utility_party2 = utility_space_party2.get_utility_distinct(last_offer) if negotiation_state == 1 else reservation_value_party2

        social_welfare = final_utility_party1 + final_utility_party2

        offers1 = [(offer.get_bid(), offer.get_time(), utility_space_party1.get_utility_distinct(offer)) for offer in
                   party1_offers]
        analysis_data_structure['party1_offers'] = offers1
        offers2 = [(offer.get_bid(), offer.get_time(), utility_space_party2.get_utility_distinct(offer)) for offer in
                   party2_offers]
        analysis_data_structure['party2_offers'] = offers2

        analysis_data_structure['party1_' + party1.get_name()] = final_utility_party1
        analysis_data_structure['party2_' + party2.get_name()] = final_utility_party2
        analysis_data_structure[party1.get_name() + '_SocialWelfare'] = social_welfare

        if len(analysis_data_structure) > 0:
            for key in self.estimation_analysis_data_structure:
                analysis_data_structure[key] = self.estimation_analysis_data_structure[key]

        return analysis_data_structure
