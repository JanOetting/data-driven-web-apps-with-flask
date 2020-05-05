from unittest import mock

from flask import Response

from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app, client


def test_register_validation_when_valid():
    # Arrange
    form_data = {
        'name': 'Jan',
        'email': "Jan.Oetting@gmail.com",
        'password': "1" * 7

    }
    # flask_app
    with flask_app.test_request_context(path="/account/register", data=form_data):
        vm = RegisterViewModel()

    # Act
    target = "pypi_org.services.user_service.find_user_by_email"
    with mock.patch(target, return_value=None):
        vm.validate()

    # verify
    assert not vm.error


def test_register_validation_when_existing():
    # Arrange
    form_data = {
        'name': 'Jan',
        'email': "Jan.Oetting@gmail.com",
        'password': "1" * 7

    }
    # flask_app
    with flask_app.test_request_context(path="/account/register", data=form_data):
        vm = RegisterViewModel()

    # Act
    target = "pypi_org.services.user_service.find_user_by_email"
    testuser = User(email=form_data.get("email"))
    with mock.patch(target, return_value=testuser):
        vm.validate()

    # verify
    assert "exists" in vm.error


def test_register_view_new_user():
    # Arrange
    from pypi_org.views.account_views import register_post
    form_data = {
        'name': 'Jan',
        'email': "Jan.Oetting@gmail.com",
        'password': "1" * 7

    }
    # flask_app
    target = "pypi_org.services.user_service.find_user_by_email"
    with mock.patch(target, return_value=None):
        target = "pypi_org.services.user_service.create_user"
        with mock.patch(target, return_value=User()):
            with flask_app.test_request_context(path="/account/register", data=form_data):
                # Act

                resp: Response = register_post()

    # verify
    assert resp.location == "/account"


def test_int_account_home_no_login(client: client):
    target="pypi_org.services.user_service.find_user_by_id"
    with mock.patch(target,return_value=None):
        resp: Response = client.get("/account")
        assert resp.status_code == 302
        assert resp.location=="http://localhost/account/login"

def test_int_account_home_with_login(client: client):
    target="pypi_org.services.user_service.find_user_by_id"
    test_user=User(name='Jan',email="JanOetting@gmail.com")
    with mock.patch(target,return_value=test_user):
        resp: Response = client.get("/account")
        assert resp.status_code == 200
        assert b"Jan" in resp.data
