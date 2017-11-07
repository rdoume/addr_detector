#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:27:48 2017

@author: robin
"""

from sklearn.base import BaseEstimator, ClassifierMixin
from pyfasttext import FastText
import pkg_resources


def is_addr(fasttext_output):
    return fasttext_output == ['1']


class Fasttext_clf(BaseEstimator, ClassifierMixin):
    data_path = pkg_resources.resource_filename('addr_detector.model', 'ft_ad.ftz')

    def __init__(self, path=data_path):
        self.model = FastText(path)

    def fit(self, X, y):
        return self

    def predict(self, X):
        if isinstance(X, str):  #
            res = self.model.predict_single(X)
            return [is_addr(res)]
        elif isinstance(X, list):
            # X=[(x) for x in X]
            return list(map(is_addr, self.model.predict(X)))

    def predict_proba(self, X):
        results = []
        if isinstance(X, str):  #
            results = results + [self.model.predict_proba_single(X)]
        elif isinstance(X, list):
            #X=[(x+'\n') for x in X]
            results = results + self.model.predict_proba(X)
        return results


def score(self, X, y=None):
    return sum(self.predict(X))
