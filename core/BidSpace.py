from utility_spaces.AdditiveUtilitySpace import AdditiveUtilitySpace
import itertools
from core.Bid import Bid


class BidSpace:
    """
    preference = {
        'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
        'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
        'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
    }
    """

    def __init__(self, preference):
        self.__preference = preference
        self.__utility_space = AdditiveUtilitySpace(preference)

    # ////////////////////////////////////////////////////////////////////////////
    def get_number_of_bids(self):
        mValues = self.__preference.get_preference_data_structure().copy()
        mValues.pop('discount_factor', None)  # remove distinct factor
        mValues.pop('reservation', None)  # remove reservation value
        values = mValues.values()
        size = 1
        for value in values:
            size *= len(value[1])
        return size

    # def get_all_bids(self) -> tuple:
    #     q = []
    #     mValues = self.__preference.get_preference_data_structure().copy()
    #     mValues.pop('discount_factor', None)  # remove distinct factor
    #     mValues.pop('reservation', None)  # remove reservation value
    #     values = mValues.values()
    #     for x in values:
    #         q.append(list(x[1]))
    #     return tuple(itertools.product(*q))

    def get_all_bids(self) -> list:
        issues = list(self.__preference.get_preference_data_structure().keys())
        issues = issues[0:-2]
        bids = []
        q = []
        mValues = self.__preference.get_preference_data_structure().copy()
        mValues.pop('discount_factor', None)  # remove distinct factor
        mValues.pop('reservation', None)  # remove reservation value
        values = mValues.values()
        for x in values:
            q.append(list(x[1]))
        for i in itertools.product(*q):
            issue_item = {}
            for j in range(len(issues)):
                issue_item[tuple(issues)[j]] = i[j]
            bid = Bid(issue_item)
            bids.append(bid)

        return bids

    def get_best_bid(self):
        issues_item = {}
        mValues = self.__preference.get_preference_data_structure().copy()
        mValues.pop('discount_factor', None)  # remove distinct factor
        mValues.pop('reservation', None)  # remove reservation value
        for key, value in mValues.items():
            issues_item[key] = max(value[1].keys(), key=lambda k: float(value[1][k]))

        best_bid = Bid(issues_item)

        return best_bid

    def get_worst_bid(self):
        issues_item = {}
        mValues = self.__preference.get_preference_data_structure().copy()
        mValues.pop('discount_factor', None)  # remove distinct factor
        mValues.pop('reservation', None)  # remove reservation value
        for key, value in mValues.items():
            issues_item[key] = min(value[1].keys(), key=lambda k: float(value[1][k]))

        worst_bid = Bid(issues_item)

        return worst_bid

    def get_all_bids_with_utility(self) -> dict:
        issues = list(self.__preference.get_preference_data_structure().keys())
        issues = issues[0:-2]
        bids_with_utility = {}
        q = []
        mValues = self.__preference.get_preference_data_structure().copy()
        mValues.pop('discount_factor', None)  # remove distinct factor
        mValues.pop('reservation', None)  # remove reservation value
        values = mValues.values()
        for x in values:
            q.append(list(x[1]))
        for i in itertools.product(*q):
            issue_item = {}
            for j in range(len(issues)):
                issue_item[tuple(issues)[j]] = i[j]
            bid = Bid(issue_item)
            utility = self.__utility_space.get_utility(bid)
            bids_with_utility[bid] = utility

        return bids_with_utility

    def get_sorted_all_bids_with_utility(self) -> list:
        all_bids = self.get_all_bids_with_utility()
        bids_list = list(all_bids.items())
        return sorted(bids_list, key=lambda x: x[1])

    def get_all_bids_utility(self):
        issues = self.__preference.get_preference_data_structure().keys()
        issue_item = {}
        bids_utility = []
        q = []
        values = self.__preference.get_preference_data_structure().values()
        for x in values:
            q.append(list(x[1]))
        for i in itertools.product(*q):
            for j in range(len(issues)):
                issue_item[tuple(issues)[j]] = i[j]
            bid = Bid(issue_item)
            utility = self.__utility_space.get_utility(bid)
            bids_utility.append(utility)

        return bids_utility

    # def product(self, *iterables):
    #     """ which does NOT build intermediate results.
    #         Omitted 'repeat' option.
    #         product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    #     """
    #     nIters = len(iterables)
    #     lstLenths = []
    #     lstRemaining = [1]
    #     for i in range(nIters-1, -1, -1):
    #         m = len(iterables[i])
    #         lstLenths.insert(0, m)
    #         lstRemaining.insert(0, m * lstRemaining[0])
    #     nProducts = lstRemaining.pop(0)
    #
    #     for p in range(nProducts):
    #         lstVals = []
    #         for i in range(nIters):
    #             j = p/lstRemaining[i]%lstLenths[i]
    #             lstVals.append(iterables[int(i)][int(j)])
    #         yield tuple(lstVals)

# if __name__ == '__main__':
#     get_all_bids_with_utility()
