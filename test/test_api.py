import pytest

from pypixiv import PixivAppApiClient


def test_require_auth_raises_exception_on_empty_access_token():
    a = PixivAppApiClient()
    with pytest.raises(Exception):
        a.require_auth()
