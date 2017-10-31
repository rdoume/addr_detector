#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:29:59 2017

@author: robin
"""

from sklearn.ensemble import VotingClassifier
from .postal_clf import Postal_clf
from .Fasttext_clf import Fasttext_clf

from sklearn.base import BaseEstimator, ClassifierMixin


class addr_voting(BaseEstimator, ClassifierMixin):
    postal_clf = Postal_clf()
    # Temporary, replace with sk_ft() when issue is fixed.
    ft_clf = Fasttext_clf()

    def __init__(self, classifiers=[('postal', postal_clf), ('ft', ft_clf)]):
        self.model = VotingClassifier(estimators=classifiers)

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        results = []
        if isinstance(X, str):  #
            results = results + [self.model.predict(X)]
        elif isinstance(X, list):
            results = results + self.model.predict(X)
        return results

    def predict_proba(self, X):
        results = []
        if isinstance(X, str):  #
            results = results + [self.model.predict(X)]
        elif isinstance(X, list):
            results = results + self.model.predict(X)
        return results


def score(self, X, y=None):
    return sum(self.predict(X))
