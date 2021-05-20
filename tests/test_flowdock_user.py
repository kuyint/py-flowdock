#!/usr/bin/env python

"""Tests for `flowdock` package."""

import pytest
import os
import flowdock
import random

@pytest.fixture
def user():
    api_token = os.environ.get('API_TOKEN')
    org = os.environ.get('ORG')
    flowdock.Configuration(org, (api_token, ""))
    return flowdock.User()

@pytest.fixture
def flow():
    api_token = os.environ.get('API_TOKEN')
    org = os.environ.get('ORG')
    flowdock.Configuration(org, (api_token, ""))
    return flowdock.Flow()

def test_list_users(user):
    assert len(user.list_users()) != 0

def test_list_flow_users(user):
    assert len(user.list_flow_users('main')) != 0

def test_org_users(user):
    assert len(user.org_users()) != 0

def get_user(user):
    username = os.environ.get('FLOWDOCK_USERNAME')
    return user.get_user(username)

@pytest.mark.parametrize("user", user)
@pytest.mark.parametrize("get_user", get_user)
def test_get_user(user, get_user):
    assert len(get_user) != 0

def create_flow(flow):
    flow_name = "test-{}".format(random.randint(0,9))
    return flow.create_flow(flow_name)

@pytest.mark.parametrize("user", user)
@pytest.mark.parametrize("create_flow", create_flow)
@pytest.mark.parametrize("get_user", get_user)
def test_add_user_flow(user, create_flow, get_user):
    user_id = get_user.get('id')
    assert len(user.add_user_flow(create_flow.get('parameterized_name'), user_id)) != 0

    # def delete_user(self, id):



    #         def list_private_conversations(self):
    #     def get_private_conversations(self, id):


