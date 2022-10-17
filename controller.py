import Model
from Model import PreferenceXMLParser
# from core.Preference import Preference


class Controller:
    def __init__(self):
        self.init_model()

    def init_model(self):
        self.model = Model.GUIContent()

    def fetch_users(self):
        users = self.model.fetch_users()
        return users

    def fetch_protocols(self):
        protocols = self.model.fetch_protocols()
        return protocols

    def fetch_utility_spaces(self):
        utility_spaces = self.model.fetch_utility_spaces()
        return utility_spaces

    def fetch_agents(self):
        agents = self.model.fetch_agents()
        return agents

    def fetch_domains(self):
        domains = self.model.fetch_domins()
        return domains

    def fetch_preferences_of_domain(self, domain: str):
        preferences_of_domain = self.model.fetch_preferences_of_domain(domain)
        return preferences_of_domain

    def fetch_preference_data_structure(self, domain_name: str, xml_file_name: str):
        preference_data_structure = PreferenceXMLParser(domain_name, xml_file_name).get_preference_data_structure()
        return preference_data_structure

    def fetch_elicitation_strategies(self):
        elicitation_strategies = self.model.fetch_elicitation_strategies()
        return elicitation_strategies

    def fetch_user_models(self):
        user_models = self.model.fetch_user_models()
        return user_models

    def fetch_bidding_strategies(self):
        bidding_strategies = self.model.fetch_bidding_strategies()
        return bidding_strategies

    def fetch_opponent_models(self):
        opponent_models = self.model.fetch_opponent_models()
        return opponent_models

    def fetch_acceptance_strategies(self):
        acceptance_strategies = self.model.fetch_acceptance_strategies()
        return acceptance_strategies

    # def fetch_preference(self, domain_name, xml_file):
    #     preference = Preference(domain_name, xml_file)
    #     return preference

    def fetch_analysis_men(self):
        analysis_men = self.model.fetch_analysis_men()
        return analysis_men

    def fetch_tournament_analysis_men(self):
        tournament_analysis_men = self.model.fetch_Tournament_analysis_men()
        return tournament_analysis_men

    def fetch_tournament_gui_segments(self, path):
        tournament_gui_segments = self.model.fetch_gui_segments(path=path)
        return tournament_gui_segments

    def fetch_gui_segments(self, path):
        session_gui_segments = self.model.fetch_gui_segments(path=path)
        return session_gui_segments

if __name__ == '__main__':
    c = Controller()
    print(c.fetch_preference_data_structure('laptop', 'laptop_buyer_utility.xml'))
