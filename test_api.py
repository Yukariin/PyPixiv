import pytest

from pypixiv import api


def test_require_auth_raises_exception_on_empty_access_token():
    a = api.BaseApi()
    with pytest.raises(Exception):
        a.require_auth()
