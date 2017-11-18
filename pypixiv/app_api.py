from .api_client import ApiClient
from .utils import get_date


class PixivAppApi(ApiClient):
    base_url = "https://app-api.pixiv.net"

    def __init__(self):
        super().__init__()

    def get_app_info(self):
        url = self.base_url + "/v1/application-info/android"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    # sort: [date_desc, date_asc, popular_desc]
    def get_contest_illusts(self, slug, sort="date_desc", filter="for_android"):
        url = self.base_url + "/v1/contest/illusts"
        params = {
            "filter": filter,
            "slug": slug,
            "sort": sort
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_contest_info_illust(self, filter="for_android"):
        url = self.base_url + "/v1/contest/info/illust"
        params = {"filter": filter}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_emoji(self):
        url = self.base_url + "/v1/emoji"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    # restrict: [public, private, all]
    def get_follow_illusts(self, restrict="public"):
        url = self.base_url + "/v2/illust/follow"
        params = {"restrict": restrict}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    # restrict: [public, private, all]
    def get_follow_novels(self, restrict="public"):
        url = self.base_url + "/v1/novel/follow"
        params = {"restrict": restrict}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_follow_user_detail(self, user_id):
        url = self.base_url + "/v1/user/follow/detail"
        params = {"user_id": user_id}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_force_like_illusts(self):
        url = self.base_url + "/v1/walkthrough/force-like-illusts"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    def get_illust(self, illust_id, filter="for_android"):
        url = self.base_url + "/v1/illust/detail"
        params = {
            "filter": filter,
            "illust_id": illust_id
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    # restrict: [public, private, all]
    def get_illust_bookmark_tags(self, user_id, restrict="public"):
        url = self.base_url + "/v1/user/bookmark-tags/illust"
        params = {
            "user_id": user_id,
            "restrict": restrict
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_illust_browsing_history(self):
        url = self.base_url + "/v1/user/browsing-history/illusts"
        r = self.auth_call_api("GET", url)

        return self.parse_json(r.text)

    def get_illust_comments(self, illust_id):
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
    def get_illust_ranking(self, mode="day", date=get_date(), filter="for_android"):
        url = self.base_url + "/v1/illust/ranking"
        params = {
            "filter": filter,
            "mode": mode,
            "date": date
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_illust_recommended(self, illust_id, filter="for_android"):
        url = self.base_url + "/v2/illust/related"
        params = {
            "filter": filter,
            "illust_id": illust_id
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_illust_trend_tags(self, filter="for_android"):
        url = self.base_url + "/v1/trending-tags/illust"
        params = {"filter": filter}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    # restrict: [public, private, all]
    def get_like_illust(self, user_id, restrict="public", tag=""):
        url = self.base_url + "/v1/user/bookmarks/illust"
        params = {
            "user_id": user_id,
            "restrict": restrict,
            "tag": tag
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_like_illust_detail(self, illust_id):
        url = self.base_url + "/v2/illust/bookmark/detail"
        params = {"illust_id": illust_id}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_like_novel(self, user_id, restrict="public", tag=""):
        url = self.base_url + "/v1/user/bookmarks/novel"
        params = {
            "user_id": user_id,
            "restrict": restrict,
            "tag": tag
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_like_novel_detail(self, novel_id):
        url = self.base_url + "/v2/novel/bookmark/detail"
        params = {"novel_id": novel_id}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_liked_illust_user(self, illust_id, filter="for_android"):
        url = self.base_url + "/v1/illust/bookmark/users"
        params = {
            "filter": filter,
            "illust_id": illust_id
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_liked_novel_user(self, novel_id):
        url = self.base_url + "/v1/novel/bookmark/users"
        params = {"novel_id": novel_id}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def post_mail_authentication(self):
        url = self.base_url + "/v1/mail-authentication/send"
        r = self.auth_call_api("POST", url)
        
        return self.parse_json(r.text)

    def get_muted_list(self):
        url = self.base_url + "/v1/mute/list"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_my_pixiv_illusts(self):
        url = self.base_url + "/v2/illust/mypixiv"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_my_pixiv_novels(self):
        url = self.base_url + "/v1/novel/mypixiv"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_new_illust(self, content_type, filter="for_android"):
        url = self.base_url + "/v1/illust/new"
        params = {
            "filter": filter,
            "content_type": content_type
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_new_novel(self):
        url = self.base_url + "/v1/novel/new"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_next(self, url):
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_notification_settings(self):
        url = self.base_url + "/v1/notification/settings"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_novel(self, novel_id):
        url = self.base_url + "/v2/novel/detail"
        params = {"novel_id": novel_id}
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    # restrict: [public, private, all]
    def get_novel_bookmark_tags(self, user_id, restrict="public"):
        url = self.base_url + "/v1/user/bookmark-tags/novel"
        params = {
            "user_id": user_id,
            "restrict": restrict
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_novel_browsing_history(self):
        url = self.base_url + "/v1/user/browsing-history/novels"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_novel_comments(self, novel_id):
        url = self.base_url + "/v1/novel/comments"
        params = {"novel_id": novel_id}
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_novel_markers(self):
        url = self.base_url + "/v2/novel/markers"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    # mode: [day, week, month,
    #        day_male, day_female,
    #        week_original, week_rookie,
    #        day_r18, day_male_r18, day_female_r18,
    #        week_r18, week_r18g]
    # date: "Y-m-d"
    def get_novel_ranking(self, mode="day", date=get_date()):
        url = self.base_url + "/v1/novel/ranking"
        params = {
            "mode": mode,
            "date": date
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_novel_series(self, series_id):
        url = self.base_url + "/v1/novel/series"
        params = {"series_id": series_id}
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_novel_text(self, novel_id):
        url = self.base_url + "/v1/novel/text"
        params = {"novel_id": novel_id}
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_novel_trend_tags(self):
        url = self.base_url + "/v1/trending-tags/novel"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_pixivision_articles(self, category, filter="for_android"):
        url = self.base_url + "/v1/spotlight/articles"
        params = {
            "filter": filter,
            "category": category
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_popular_illust(self, content_type):
        url = self.base_url + "/v1/illust/popular"
        params = {"content_type": content_type}
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_popular_novel(self):
        url = self.base_url + "/v1/novel/popular"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_popular_preview_illust(self, word, search_target, duration, filter="for_android"):
        url = self.base_url + "/v1/search/popular-preview/illust"
        params = {
            "filter": filter,
            "word": word,
            "search_target": search_target,
            "duration": duration
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_popular_preview_novel(self, word, search_target, duration):
        url = self.base_url + "/v1/search/popular-preview/novel"
        params = {
            "word": word,
            "search_target": search_target,
            "duration": duration
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_profile_presets(self):
        url = self.base_url + "/v1/user/profile/presets"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    def get_recommended_illusts(self, include_ranking_illusts, filter="for_android"):
        url = self.base_url + "/v1/illust/recommended"
        params = {
            "filter": filter,
            "include_ranking_illusts": include_ranking_illusts
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_recommended_manga_list(self, include_ranking_illusts, bookmark_illust_ids, filter="for_android"):
        url = self.base_url + "/v1/manga/recommended"
        params = {
            "filter": filter,
            "include_ranking_illusts": include_ranking_illusts,
            "bookmark_illust_ids": bookmark_illust_ids
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_recommended_novels(self, include_ranking_illusts):
        url = self.base_url + "/v1/novel/recommended"
        params = {
            "include_ranking_illusts": include_ranking_illusts
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_search_auto_complete_keywords(self, word):
        url = self.base_url + "/v1/search/autocomplete"
        params = {"word": word}
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_search_illust(self, word, sort, search_target, bookmark_num, duration, filter="for_android"):
        url = self.base_url + "/v1/search/illust"
        params = {
            "filter": filter,
            "word": word,
            "search_target": search_target,
            "bookmark_num": bookmark_num,
            "duration": duration
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_search_novel(self, word, sort, search_target, bookmark_num, duration):
        url = self.base_url + "/v1/search/novel"
        params = {
            "word": word,
            "search_target": search_target,
            "bookmark_num": bookmark_num,
            "duration": duration
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_search_user(self, word, filter="for_android"):
        url = self.base_url + "/v1/search/user"
        params = {
            "filter": filter,
            "word": word
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def post_ugoira_metadata(self, illust_id):
        url = self.base_url + "/v1/ugoira/metadata"
        data = {"illust_id": illust_id}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_upload_illust_status(self, convert_key):
        url = self.base_url + "/v1/upload/status"
        data = {"convert_key": convert_key}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)
    
    def get_user(self, user_id, filter="for_android"):
        url = self.base_url + "/v1/user/detail"
        params = {
            "filter": filter,
            "user_id": user_id
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_user_follower(self, user_id, filter="for_android"):
        url = self.base_url + "/v1/user/follower"
        params = {
            "filter": filter,
            "user_id": user_id
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_user_following(self, user_id, restrict, filter="for_android"):
        url = self.base_url + "/v1/user/following"
        params = {
            "filter": filter,
            "user_id": user_id,
            "restrict": restrict
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)
    
    def get_user_illusts(self, user_id, type, filter="for_android"):
        url = self.base_url + "/v1/user/illusts"
        params = {
            "filter": filter,
            "user_id": user_id,
            "type": type
        }
        r = self.auth_call_api("GET", url, params=params)
        
        return self.parse_json(r.text)

    def get_user_me_state(self):
        url = self.base_url + "/v1/user/me/state"
        r = self.auth_call_api("GET", url)
        
        return self.parse_json(r.text)

    def get_user_my_pixiv(self, user_id, filter="for_android"):
        url = self.base_url + "/v1/user/mypixiv"
        params = {
            "filter": filter,
            "user_id": user_id
        }
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_user_novels(self, user_id):
        url = self.base_url + "/v1/user/novels"
        params = {"user_id": user_id}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_user_recommended(self, filter="for_android"):
        url = self.base_url + "/v1/user/recommended"
        params = {"filter": filter}
        r = self.auth_call_api("GET", url, params=params)

        return self.parse_json(r.text)

    def get_user_topic(self):
        url = self.base_url + "/v1/notification/user/topic"
        r = self.auth_call_api("GET", url)

        return self.parse_json(r.text)

    def get_walkthrough_illusts(self):
        url = self.base_url + "/v1/walkthrough/illusts"
        r = self.call_api("GET", url)

        return self.parse_json(r.text)

    def post_add_illust_browsing_history(self, illust_ids):
        url = self.base_url + "/v2/user/browsing-history/illust/add"
        data = {"illust_ids[]": illust_ids}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_add_novel_browsing_history(self, novel_ids):
        url = self.base_url + "/v2/user/browsing-history/novel/add"
        data = {"novel_ids[]": novel_ids}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_add_novel_marker(self, novel_id, page):
        url = self.base_url + "/v1/novel/marker/add"
        data = {
            "novel_id": novel_id,
            "page": page
        }
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_debug_receipt(self, receipt_data):
        url = self.base_url + "/v1/dev/ios/receipt/post"
        data = {"receipt_data": receipt_data}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_delete_illust(self, illust_id):
        url = self.base_url + "/v1/illust/delete"
        data = {"illust_id": illust_id}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_delete_novel(self, novel_id):
        url = self.base_url + "/v1/novel/delete"
        data = {"novel_id": novel_id}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_delete_novel_marker(self, novel_id):
        url = self.base_url + "/v1/novel/marker/delete"
        data = {"novel_id": novel_id}
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_feedback(self, message, device, dimension01, dimension02, dimension03, dimension04):
        url = self.base_url + "/v1/feedback"
        data = {
            "message": message,
            "device": device,
            "dimension01": dimension01,
            "dimension02": dimension02,
            "dimension03": dimension03,
            "dimension04": dimension04
        }
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_follow_user(self, user_id, restrict):
        url = self.base_url + "/v1/user/follow/add"
        data = {
            "user_id": user_id,
            "restrict": restrict
        }
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_illust_comment(self, illust_id, comment, parent_comment_id):
        url = self.base_url + "/v1/illust/comment/add"
        data = {
            "illust_id": illust_id,
            "comment": comment,
            "parent_comment_id": parent_comment_id
        }
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_like_illust(self, illust_id, restrict, tags):
        url = self.base_url + "/v2/illust/bookmark/add"
        data = {
            "illust_id": illust_id,
            "restrict": restrict,
            "tags[]": tags
        }
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_like_novel(self, novel_id, restrict, tags):
        url = self.base_url + "/v2/novel/bookmark/add""/v1/user/follow/add"
        data = {
            "novel_id": novel_id,
            "restrict": restrict,
            "tags[]": tags
        }
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_mute_setting(self, add_user_ids, delete_user_ids, add_tags, delete_tags):
        url = self.base_url + "/v1/mute/edit"
        data = {
            "add_user_ids[]": add_user_ids,
            "delete_user_ids[]": delete_user_ids,
            "add_tags[]": add_tags,
            "delete_tags[]": delete_tags
        }
        r = self.auth_call_api("POST", url, data=data)
        
        return self.parse_json(r.text)

    def post_novel_comment(self, novel_id, comment, parent_comment_id):
        url = self.base_url + "/v1/novel/comment/add"
        data = {
            "novel_id": novel_id,
            "comment": comment,
            "parent_comment_id": parent_comment_id
        }
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_register_premium(self, purchase_data, signature, app_version):
        url = self.base_url + "/v1/premium/android/register"
        data = {
            "purchase_data": purchase_data,
            "signature": signature,
            "app_version": app_version
        }
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_unfollow_user(self, user_id):
        url = self.base_url + "/v1/user/follow/delete"
        data = {"user_id": user_id}
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_unlike_illust(self, illust_id):
        url = self.base_url + "/v1/illust/bookmark/delete"
        data = {"illust_id": illust_id}
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)
    
    def post_unlike_novel(self, novel_id):
        url = self.base_url + "/v1/novel/bookmark/delete"
        data = {"novel_id": novel_id}
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_upload_illust(self, data):
        url = self.base_url + "/v1/upload/illust"
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_user_profile_edit(self, data):
        url = self.base_url + "/v1/user/profile/edit"
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)

    def post_user_workspace_edit(self, pc, monitor, tool, scanner, tablet, mouse, printer, desktop, music, desk, chair, comment):
        url = self.base_url + "/v1/user/workspace/edit"
        data = {
            "pc": pc,
            "monitor": monitor,
            "tool": tool,
            "scanner": scanner,
            "tablet": tablet,
            "mouse": mouse,
            "printer": printer,
            "desktop": desktop,
            "music": music,
            "desk": desk,
            "chair": chair,
            "comment": comment
        }
        r = self.auth_call_api("POST", url, data=data)

        return self.parse_json(r.text)
