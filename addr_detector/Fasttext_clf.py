#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:27:48 2017

@author: robin
"""

from sklearn.base import BaseEstimator, ClassifierMixin
from fastText import load_model
import pkg_resources


def is_addr(fasttext_output):
    """
    the fasttext model is:
    '__label__1': an address
    '__label__0': not an address
    """
    if fasttext_output:
        return fasttext_output[0] == '__label__1'
    return False


class Fasttext_clf(BaseEstimator, ClassifierMixin):
    data_path = pkg_resources.resource_filename('addr_detector.model', 'ft_ad.ftz')

    def __init__(self, path=data_path):
        self.model = load_model(path)

    def fit(self, X, y):
        return self

    def predict(self, X):
        r = self.model.predict(X)
        if r:
            return is_addr(r[0])
        return False

    def predict_proba(self, X):
        r = self.model.predict(X)
        if r and len(r) >= 2:
            probas = r[1]
            if probas:
                return probas[0]
        return False


def score(self, X, y=None):
    return sum(self.predict(X))
