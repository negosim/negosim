from configurations import *
from os import listdir
from os.path import isfile, join
import os
from genericpath import isdir
from xml.etree import ElementTree


class GUIContent:
    def __init__(self):
        pass

    def fetch_users(self):
        user_list = [f for f in listdir(
            USER_PATH) if isfile(join(USER_PATH, f))]
        user_list.remove('__init__.py')
        if user_list.count('__pycache__') > 0:
            user_list.remove('__pycache_')
        return user_list

    def fetch_protocols(self):
        protocol_list = [f for f in listdir(
            PROTOCOL_PATH) if isfile(join(PROTOCOL_PATH, f))]
        protocol_list.remove('__init__.py')
        if protocol_list.count('__pycache__') > 0:
            protocol_list.remove('__pycache_')
        return protocol_list

    def fetch_agents(self):
        party_list = [f for f in listdir(
            PARTY_PATH) if isfile(join(PARTY_PATH, f))]
        party_list.remove('__init__.py')
        if party_list.count('__pycache__') > 0:
            party_list.remove('__pycache_')
        return party_list

    def fetch_domins(self):
        if isdir(DOMAIN_PATH):
            domain_lists = [name for name in os.listdir(DOMAIN_PATH)]
            return domain_lists
        raise FileNotFoundError(f"There is a problem fetching domains from path '{DOMAIN_PATH}'")

    def fetch_preferences_of_domain(self, domain: str):
        path = DOMAIN_PATH + '/' + domain
        if isdir(path):
            preference_profile_list = [name for name in os.listdir(path)]
            return preference_profile_list
        return None

    def fetch_elicitation_strategies(self):
        if isdir(ELICITATION_STRATEGIES_PATH):
            elicitation_strategies_list = [name for name in os.listdir(ELICITATION_STRATEGIES_PATH)]
            elicitation_strategies_list.remove('__init__.py')
            if elicitation_strategies_list.count('__pycache__') > 0:
                elicitation_strategies_list.remove('__pycache__')
            return elicitation_strategies_list
        return None

    def fetch_user_models(self):
        if isdir(USER_MODEL_PATH):
            user_models_list = [name for name in os.listdir(USER_MODEL_PATH)]
            user_models_list.remove('__init__.py')
            if user_models_list.count('__pycache__') > 0:
                user_models_list.remove('__pycache_')
            return user_models_list
        return None

    def fetch_bidding_strategies(self):
        if isdir(BIDDING_STRATEGIES_PATH):
            bidding_strategies_list = [name for name in os.listdir(BIDDING_STRATEGIES_PATH)]
            bidding_strategies_list.remove('__init__.py')
            if bidding_strategies_list.count('__pycache__') > 0:
                bidding_strategies_list.remove('__pycache__')
            return bidding_strategies_list
        return None

    def fetch_opponent_models(self):
        if isdir(ELICITATION_STRATEGIES_PATH):
            opponent_models_list = [name for name in os.listdir(ELICITATION_STRATEGIES_PATH)]
            opponent_models_list.remove('__init__.py')
            if opponent_models_list.count('__pycache__') > 0:
                opponent_models_list.remove('__pycache__')
            return opponent_models_list
        return None

    def fetch_acceptance_strategies(self):
        if isdir(ACCEPTANCE_STRATEGIES_PATH):
            acceptance_strategies_list = [name for name in os.listdir(ACCEPTANCE_STRATEGIES_PATH)]
            acceptance_strategies_list.remove('__init__.py')
            if acceptance_strategies_list.count('__pycache__') > 0:
                acceptance_strategies_list.remove('__pycache__')
            return acceptance_strategies_list
        return None

    def fetch_analysis_men(self):
        if isdir(ANALYSIS_PATH):
            analysis_men_list = [name for name in os.listdir(ANALYSIS_PATH)]
            analysis_men_list.remove('__init__.py')
            if analysis_men_list.count('__pycache__') > 0:
                analysis_men_list.remove('__pycache__')
            return analysis_men_list
        return None

    def fetch_Tournament_analysis_men(self):
        if isdir(ANALYSIS_PATH):
            analysis_men_list = [name for name in os.listdir(ANALYSIS_TOURNAMENT_PATH)]
            analysis_men_list.remove('__init__.py')
            if analysis_men_list.count('__pycache__') > 0:
                analysis_men_list.remove('__pycache__')
            return analysis_men_list
        return None

    def fetch_tournament_gui_segments(self):
        if isdir(TOURNAMENT_GUI_SEGMENT_PATH):
            tournament_gui_segments = [name for name in os.listdir(TOURNAMENT_GUI_SEGMENT_PATH)]
            tournament_gui_segments.remove('__init__.py')
            if tournament_gui_segments.count('__pycache__') > 0:
                tournament_gui_segments.remove('__pycache__')
            return tournament_gui_segments
        return None

    def fetch_session_gui_segments(self):
        if isdir(SESSION_GUI_SEGMENT_PATH):
            tournament_gui_segments = [name for name in os.listdir(SESSION_GUI_SEGMENT_PATH)]
            tournament_gui_segments.remove('__init__.py')
            if tournament_gui_segments.count('__pycache__') > 0:
                tournament_gui_segments.remove('__pycache__')
            return tournament_gui_segments
        return None


class PreferenceXMLParser:
    """
        preference = {
                'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
                'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
                'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
            }
    """

    def __init__(self, domain_name: str, xml_file: str):
        self.file_name = xml_file
        self.domain_name = domain_name

    def get_preference_data_structure(self):
        full_file = os.path.abspath(os.path.join(DOMAIN_PATH+'\\'+self.domain_name, self.file_name))
        dom = ElementTree.parse(full_file)

        preference = {}
        objectives = dom.findall('objective')
        for objective in objectives:
            issues = objective.findall('issue')
            for issue in issues:
                preference[issue.attrib['name']] = []
                items = issue.findall('item')
                item_value = {}
                for item in items:
                    item_value[item.attrib['value']] = item.attrib['evaluation']
                preference[issue.attrib['name']].append(item_value)

            weights = objective.findall('weight')
            i = 0
            for issue in preference:
                preference[issue].insert(0, weights[i].attrib['value'])
                i += 1

        discount_factor = dom.find('discount_factor')
        if discount_factor is not None:
            preference['discount_factor'] = discount_factor.attrib['value']

        reservation = dom.find('reservation')
        if reservation is not None:
            preference['reservation'] = reservation.attrib['value']

        return preference


if __name__ == '__main__':
    model = GUIContent()
    print(model.fetch_acceptance_strategies())
    # print(model.fetch_users())
    # preferenceXMLParser = PreferenceXMLParser('laptop', 'laptop_buyer_utility.xml')
    # print(preferenceXMLParser.get_preference_data_structure())