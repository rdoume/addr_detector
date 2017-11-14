#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:27:48 2017

@author: robin
"""

from sklearn.base import BaseEstimator, ClassifierMixin
from postal.parser import parse_address
from postal.expand import expand_address


class Postal_clf(BaseEstimator, ClassifierMixin):
    def __init__(
            self,
            param=None,
            expander=expand_address,
            parser=parse_address):
        self.param = None
        self.parser = parser
        self.expander = expander

    def fit(self, X, y):
        print(2)
        return self

    def predict(self, X):
        return self.is_addr(X)

    def is_addr(self, X):
        full_road = False
        exp_add = self.expander(X)
        parsed_add = self.parser(exp_add[0])
        num_elt_addr = len(parsed_add)
        address = dict.fromkeys(['house_number',
                                 'road',
                                 'house',
                                 'suburb',
                                 'city_district',
                                 'city',
                                 'state',
                                 'postcode',
                                 'country'])

        for x, y in parsed_add:
            address[y] = x
        if address['road'] is not None:
            # len(query_road_set)>1 # We check the length of the troad.  If
            # eq=1, means it's just dummy name (like street)
            full_road = True
        if num_elt_addr >= 4:
            return True

        elif (address['house_number'] is not None and address['city'] is not None and full_road):
            return True
        elif (address['house_number'] is not None and address['postcode'] is not None and full_road):
            return True
        elif (address['house_number'] is not None and full_road):
            return False
        elif ((address['postcode'] or address['city']) is not None and full_road):
            return True
        return False

    def score(self, X, y=None):
        return sum(self.predict(X))
