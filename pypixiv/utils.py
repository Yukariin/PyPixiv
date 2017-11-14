from datetime import datetime, timezone
from hashlib import md5


def get_md5(data):
    return md5(data.encode("utf-8")).hexdigest()


def get_time():
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None).strftime("%Y-%m-%dT%H:%M:%S%z")


def get_date():
    return datetime.utcnow().strftime("%Y-%m-%d")
