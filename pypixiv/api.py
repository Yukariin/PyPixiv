import json
import os
import shutil
from collections import namedtuple

import requests

from .utils import get_md5, get_time, get_date


class ApiClient:
    # App defines
    app_os = "android"
    app_version = "5.0.61"

    # Device defines
    os_version = "6.0"
    device_model = "Google Pixel C - 6.0.0 - API 23 - 2560x1800"
    # By default 5.0.61 app gets device token by
    # android.content.SharedPreferences.getString(String key, String defValue)
    # and uses `pixiv` as defValue
    device_token = "pixiv"

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
    user_id = 0

    def __init__(self):
        self.session = requests.Session()

    @staticmethod
    def parse_json(json_str: str):
        def _obj_hook(d):
            return namedtuple("X", d.keys())(*d.values())

        return json.loads(json_str, object_hook=_obj_hook)

    def call_api(self, method, url, params=None, data=None, headers=None, stream=False):
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

        print("RequestUrl %s %s" % (method, url))
        
        if method == "GET":
            return self.session.get(url, params=params, data=data, headers=headers, stream=stream)
        elif method == "POST":
            return self.session.post(url, params=params, data=data, headers=headers, stream=stream)
        elif method == "DELETE":
            return self.session.delete(url, params=params, data=data, headers=headers, stream=stream)
        else:
            raise ValueError("Unknown method: %s" % method)

    def auth_call_api(self, method, url, params=None, data=None, headers=None, stream=False):
        self.require_auth()

        headers = headers or {}
        headers["Authorization"] = "Bearer %s" % self.access_token

        return self.call_api(method, url, params, data, headers, stream)

    def require_auth(self):
        if self.access_token is None:
            raise Exception("Authentication required! Call login() or set_auth() first!")

    def set_auth(self, access_token, refresh_token=None):
        self.access_token = access_token
        self.refresh_token = refresh_token

    def login(self, username, password):
        return self.auth(username, password)

    def auth(self, username=None, password=None, refresh_token=None):
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
            raise Exception("[ERROR] auth() but no password or refresh_token is set.")

        r = self.call_api("POST", url, data=data)
        print(r.text)
        if r.status_code not in [200, 301, 302]:
            raise Exception("[ERROR] auth() failed!\nHTTP %s: %s" % (r.status_code, r.text))

        token = None
        try:
            token = self.parse_json(r.text)
            self.access_token = token.response.access_token
            self.refresh_token = token.response.refresh_token
            self.user_id = token.response.user.id
        except:
            print("JSON parse error!")

        return token

    def download(self, url, path=os.path.curdir, name=None, replace=False, referer="https://app-api.pixiv.net/"):
        if not name:
            name = os.path.basename(url)

        file_path = os.path.join(path, name)
        if (not os.path.exists(file_path)) or replace:
            res = self.call_api("GET", url, headers={"Referer": referer}, stream=True)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(res.raw, f)


class PixivAppApiClient(ApiClient):
    base_url = "https://app-api.pixiv.net"

    def __init__(self):
        super().__init__()

    def app_info(self):
        url = self.base_url + "/v1/application-info/android"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    def contest_illusts(self, slug="", sort="", filter="for_android"):
        url = self.base_url + "v1/contest/illusts"
        params = {
            "filter": filter,
            "slug": slug,
            "sort": sort
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def emoji(self):
        url = self.base_url + "v1/emoji"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    # restrict: [restrict, private, all]
    def follow_illusts(self, restrict="public"):
        url = self.base_url + "/v2/illust/follow"
        params = {"restrict": restrict}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    # restrict: [restrict, private, all]
    def follow_novels(self, restrict="public"):
        url = self.base_url + "/v1/novel/follow"
        params = {"restrict": restrict}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def force_like_illusts(self):
        url = self.base_url + "v1/walkthrough/force-like-illusts"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    def illust(self, illust_id, filter="for_android"):
        url = self.base_url + "/v1/illust/detail"
        params = {
            "filter": filter,
            "illust_id": illust_id
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    # restrict: [restrict, private, all]
    def illust_bookmark_tags(self, user_id, restrict="public"):
        url = self.base_url + "/v1/user/bookmark-tags/illust"
        params = {
            "user_id": user_id,
            "restrict": restrict
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def illust_browsing_history(self):
        url = self.base_url + "/v1/user/browsing-history/illusts"
        r = self.auth_call_api("GET", url)

        return self.parse_json(r.text)

    def illust_comments(self, illust_id):
        url = self.base_url + "/v1/illust/comments"
        params = {"illust_id": illust_id}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    # mode: [day, week, month,
    #        day_male, day_female,
    #        week_original, week_rookie,
    #        day_r18, day_male_r18, day_female_r18,
    #        week_r18, week_r18g]
    # date: "Y-m-d"
    def illust_ranking(self, mode="day", date=get_date(), filter="for_android"):
        url = self.base_url + "/v1/illust/ranking"
        params = {
            "filter": filter,
            "mode": mode,
            "date": date
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def illust_recommended(self, illust_id, filter="for_android"):
        url = self.base_url + "/v2/illust/related"
        params = {
            "filter": filter,
            "illust_id": illust_id
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)
