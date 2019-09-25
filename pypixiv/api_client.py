import datetime
import json
import os
import shutil
from collections import namedtuple

import requests

from .utils import get_time, get_md5, PixivError, PixivAuthFailed


class ApiClient:
    # App defines
    app_os = "android"
    app_version = "5.0.61"

    # Device defines
    os_version = "6.0"
    device_model = "Google Pixel C - 6.0.0 - API 23 - 2560x1800"

    # UA defines (based on device and app defines)
    user_agent = "PixivAndroidApp/%s (Android %s; %s)" % (app_version, os_version, device_model)
    short_ua = "PixivAndroidApp/%s" % app_version

    # App/OS specific keys
    # android - 5.0.61
    client_id = "MOBrBDS8blbauoSck0ZfDbtuzpyT"
    client_secret = "lsACyCD94FhDUtGTXi3QzcFE2uU1hqtDaKeqrdwj"
    client_hash = "28c1fdd170a5204386cb1313c7077b34f83e4aaf4aa829ce78c231e05b0bae2c"

    access_token = None
    refresh_token = None
    expire = None
    user_id = 0
    # By default 5.0.61 app gets device token by
    # android.content.SharedPreferences.getString(String key, String defValue)
    # and uses `pixiv` as defValue
    # Then app calls auth() and get tokens and store required device_token into SharedPreferences file
    device_token = "pixiv"

    def __init__(self):
        self.session = requests.Session()

    @staticmethod
    def parse_json(json_str: str):
        def _obj_hook(d):
            return namedtuple("X", d.keys())(*d.values())

        return json.loads(json_str, object_hook=_obj_hook)

    def call_api(self, method: str, url: str, params: dict=None, data: dict=None, headers: dict=None, stream: bool=False):
        req_time = get_time()
        req_hash = get_md5(req_time + self.client_hash)

        headers = headers or {}
        headers["User-Agent"] = self.short_ua
        headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        headers["Accept-Language"] = "*"

        headers["App-OS"] = self.app_os
        headers["App-OS-Version"] = self.os_version
        headers["App-Version"] = self.app_version

        headers["X-Client-Time"] = req_time
        headers["X-Client-Hash"] = req_hash

        #print("RequestUrl %s %s" % (method, url))

        if data is not None:
            param = ""
            for key, value in data.items():
                if key != "password":
                    param += "%s: %s " % (key, value)

            #print("RequestPostParam %s" % param)

        res = None
        if method == "GET":
            res = self.session.get(url, params=params, data=data, headers=headers, stream=stream)
        elif method == "POST":
            res = self.session.post(url, params=params, data=data, headers=headers, stream=stream)
        elif method == "DELETE":
            res = self.session.delete(url, params=params, data=data, headers=headers, stream=stream)
        else:
            raise ValueError("Unknown method: %s" % method)

        if res.status_code != 200:
            #print(res.status_code)
            raise PixivError(res.text)

        return res

    def auth_call_api(self, method: str, url: str, params: dict=None, data: dict=None, headers: dict=None, stream: bool=False):
        self.require_auth()
        if (datetime.datetime.now() > self.expire) and (self.refresh_token is not None):
            self.auth(refresh_token=self.refresh_token);

        headers = headers or {}
        headers["Authorization"] = "Bearer %s" % self.access_token

        return self.call_api(method, url, params, data, headers, stream)

    def require_auth(self):
        if self.access_token is None:
            raise Exception("Authentication required! Call login() or set_auth() first!")

    def set_auth(self, access_token: str, refresh_token: str=None):
        self.access_token = access_token
        self.refresh_token = refresh_token

    def login(self, username: str, password: str):
        return self.auth(username, password)

    def auth(self, username: str=None, password: str=None, refresh_token: str=None):
        url = "https://oauth.secure.pixiv.net/auth/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "device_token": self.device_token,
            "get_secure_url": True,
        }

        if (username is not None) and (password is not None):
            data["grant_type"] = "password"
            data["username"] = username
            data["password"] = password
        elif (refresh_token is not None) or (self.refresh_token is not None):
            data["grant_type"] = "refresh_token"
            data["refresh_token"] = refresh_token or self.refresh_token
        else:
            raise ValueError("no password or refresh_token is set")

        r = self.call_api("POST", url, data=data)
        if r.status_code not in [200, 301, 302]:
            raise PixivAuthFailed(r.text)

        token = self.parse_json(r.text)
        self.access_token = token.response.access_token
        self.refresh_token = token.response.refresh_token
        self.expire = datetime.datetime.now() + datetime.timedelta(seconds=token.response.expires_in)
        self.user_id = token.response.user.id
        self.device_token = token.response.device_token

        return token

    def download(self, url: str, path: str=os.path.curdir, name: str=None, replace: bool=False, referer: str="https://app-api.pixiv.net/"):
        if not name:
            name = os.path.basename(url)

        file_path = os.path.join(path, name)
        if (not os.path.exists(file_path)) or replace:
            res = self.call_api("GET", url, headers={"Referer": referer}, stream=True)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(res.raw, f)
