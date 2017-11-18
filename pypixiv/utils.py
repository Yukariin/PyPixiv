from datetime import datetime, timezone
from hashlib import md5


def get_md5(data: str):
    return md5(data.encode("utf-8")).hexdigest()


def get_time(dt: datetime=datetime.utcnow()):
    return dt.replace(tzinfo=timezone.utc).astimezone(tz=None).strftime("%Y-%m-%d'T'%H:%M:%S%z")


def get_date(dt: datetime=datetime.utcnow()):
    return dt.strftime("%Y-%m-%d")


class PixivError(Exception):
    """
    Base exception type
    """


class PixivAuthFailed(PixivError):
    """
    Auth error
    """
