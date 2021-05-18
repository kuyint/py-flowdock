#!/usr/bin/env python

"""Tests for `flowdock` package."""

import pytest
import os
import flowdock


@pytest.fixture
def user():
    api_token = os.environ.get('API_TOKEN')
    org = os.environ.get('ORG')
    flowdock.Configuration(org, (api_token, ""))
    return flowdock.User()

def test_list_users(user):
    assert len(user.list_users()) != 0

def test_list_flow_users(user):
    assert len(user.list_flow_users('main')) != 0

def test_org_users(user):
    assert len(user.org_users()) != 0

    # def get_user(self, id):
    # def delete_user(self, id):
    # def add_user_flow(self, flow, id):


    #         def list_private_conversations(self):
    #     def get_private_conversations(self, id):


