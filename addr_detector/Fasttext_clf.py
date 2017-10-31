#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:27:48 2017

@author: robin
"""

from sklearn.base import BaseEstimator, ClassifierMixin
from pyfasttext import FastText
import pkg_resources


class Fasttext_clf(BaseEstimator, ClassifierMixin):
    data_path = pkg_resources.resource_filename('addr_detector', 'model.ftz')
    print(data_path)

    def __init__(self, path=data_path):
        self.model = FastText(path)
        print(self.model.labels)

    def fit(self, X, y):
        return self

    def predict(self, X):
        results = []
        if isinstance(X, str):  #
            results = results + [self.model.predict_single(X)]
        elif isinstance(X, list):
            results = results + self.model.predict(X)
        return results

    def predict_proba(self, X):
        results = []
        if isinstance(X, str):  #
            results = results + [self.model.predict_proba_single(X)]
        elif isinstance(X, list):
            results = results + self.model.predict_proba(X)
        return results


def score(self, X, y=None):
    return sum(self.predict(X))
