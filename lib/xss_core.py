"""
    XSS Core Interface
"""

from lib.models import xss_get_cookies


def get_cookie(web_input):
    try:
        project_id = int(web_input.id)
    except ValueError:
        return
    xss_get_cookies(
        project_id=project_id,
        xss_location=web_input.xss_location,
        xss_toplocation=web_input.xss_toplocation,
        xss_cookies=web_input.xss_cookie,
        xss_opener=web_input.xss_opener,
        xss_referrer=web_input.xss_referrer,
        xss_title=web_input.xss_title,
    )