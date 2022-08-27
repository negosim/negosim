#######################################################
# 
# Bid.py
# Python implementation of the Class Bid
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: Arash Ebrahimnezhad
# 
#######################################################


class Bid:
    """
    bid = {
    'Brand': 'Lenovo',
    'Monitor': '15',
    'HDD': '1T'
    }
    """

    def __init__(self, issues_item: dict):
        if not isinstance(issues_item, dict):
            raise TypeError('Please send issue_item as dictionary!')
        self.__issues_items = issues_item

    def get_issues_items(self) -> dict:
        """
        This method returns issues and their values
        in dictionary data typ
        :return: dict
        """
        return self.__issues_items

    def is_equal(self, bid) -> bool:
        if not isinstance(bid, Bid):
            raise TypeError('Please send an object from Bid Class!')
        return self.__issues_items == bid.get_issues_items()

    def __repr__(self):
        s = '{'
        for issue, item in self.get_issues_items().items():
            s += f'{issue}: {item}, '
        s += '}'
        return s
