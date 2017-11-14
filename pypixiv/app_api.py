from .api_client import ApiClient
from .utils import get_date


class PixivAppApi(ApiClient):
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
