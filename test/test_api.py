import pytest

from pypixiv import PixivAppApi


def test_require_auth_raises_exception_on_empty_access_token():
    a = PixivAppApi()
    with pytest.raises(Exception):
        a.require_auth()
