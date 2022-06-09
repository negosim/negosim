from Agents.TimeDependent import TimeDependent
from core.Preference import Preference


class Boulware(TimeDependent):
    """
    Bilateral Boulware Agent
    """

    def __init__(self, preference: Preference):
        TimeDependent.__init__(self, preference=preference)
        self.set_values(p_min=0.0, p_max=1.0, k=0.0, e=0.2)

    def get_name(self):
        """
        :return: Party Name
        """
        return "Boulware"
