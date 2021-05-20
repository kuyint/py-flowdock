#!/usr/bin/env python

"""Tests for `flowdock` package."""

import pytest
import os
import flowdock
import random
import time


@pytest.fixture
def flow():
    api_token = os.environ.get('API_TOKEN')
    org = os.environ.get('ORG')
    flowdock.Configuration(org, (api_token, ""))
    return flowdock.Flow()

@pytest.fixture
def flow_auth_user():
    username = os.environ.get('FLOWDOCK_USERNAME')
    password = os.environ.get('FLOWDOCK_PASSWORD')
    org = os.environ.get('ORG')
    flowdock.Configuration(org, (username, password))
    return flowdock.Flow()

def test_flow_list(flow_auth_user):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert len(flow_auth_user.list_flows()) != 0

def test_flow_list(flow):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert len(flow.list_flows()) != 0

def test_list_all_flows(flow):
    assert len(flow.list_all_flows()) != 0

def test_get_flow_id(flow):
    assert len(flow.get_flow(flow_id='054c77e2-1a31-4792-a51e-de5ceae0d4a7')) != 0

def test_get_flow_name(flow):
    assert len(flow.get_flow('main')) != 0

def create_flow(flow):
    flow_name = "test-{}".format(random.randint(0,9))
    return flow.create_flow(flow_name)

@pytest.mark.parametrize("flow", flow)
@pytest.mark.parametrize("create_flow", create_flow)
def test_create_flow(flow, create_flow):
    assert len(create_flow) != 0

@pytest.mark.parametrize("flow", flow)
@pytest.mark.parametrize("create_flow", create_flow)
def test_rename_flow(flow, create_flow):
    flow_name = "test-{}".format(random.randint(0,9))
    assert len(flow.rename_flow(create_flow.get('parameterized_name'), flow_name)) != 0

@pytest.mark.parametrize("flow", flow)
@pytest.mark.parametrize("create_flow", create_flow)
def test_flow_access_mode(flow, create_flow):
    assert len(flow.access_mode(create_flow.get('parameterized_name'), 'organization')) != 0

@pytest.mark.parametrize("flow", flow)
@pytest.mark.parametrize("create_flow", create_flow)
def test_delete_flow(flow, create_flow):
    assert len(flow.delete_flow(create_flow.get('parameterized_name'))) != 0
