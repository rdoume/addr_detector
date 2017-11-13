#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `addr_detector` package."""

import pytest
from addr_detector.Fasttext_clf import Fasttext_clf
from addr_detector.Postal_clf import Postal_clf


@pytest.fixture
def postal():
    return Postal_clf()


@pytest.fixture
def fasttext():
    return Fasttext_clf()


def test_good_addr_fasttext(fasttext):
    assert fasttext.predict('7 rue spontini paris')


def test_bad_addr_fasttext(fasttext):
    assert not fasttext.predict('Comment se faire cuire un oeuf')


def test_good_addr_postal(postal):
    assert postal.predict('7 rue spontini paris')


def test_bad_addr_postal(postal):
    assert not postal.predict('Comment se faire cuire un oeuf')
