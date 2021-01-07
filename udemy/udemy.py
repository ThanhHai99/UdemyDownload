# pylint: disable=R,C
#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from udemy.internal import InternUdemyCourse as Udemy
from udemy.internal import InternUdemyCourses as UdemyCourses


def course(url, username='', password='', cookies='', basic=True, skip_hls_stream=False, callback=None):
    """Returns udemy course instance.

    @params:
        url      : Udemy course url required : type (string).
        username : Udemy email account required : type (string).
        password : Udemy account password required : type (string)
        cookies  : Udemy account logged in browser cookies optional : type (string)
    """
    return Udemy(url, username, password, cookies, basic, skip_hls_stream, callback)

def fetch_enrolled_courses(username='', password='', cookies='', basic=True):
    """Returns udemy course instance.

    @params:
        url      : Udemy course url required : type (string).
        username : Udemy email account required : type (string).
        password : Udemy account password required : type (string)
        cookies  : Udemy account logged in browser cookies optional : type (string)
    """
    return UdemyCourses(username, password, cookies, basic)