#!/usr/bin/env python

"""Tests for `flowdock` package."""

import pytest
import os
import flowdock


@pytest.fixture
def org():
    api_token = os.environ.get('API_TOKEN')
    org = os.environ.get('ORG')
    flowdock.Configuration(org, (api_token, ""))
    return flowdock.Org()

def test_list_org(org):
    assert len(org.list_org()) != 0
    

        # def get_org(self, id):
