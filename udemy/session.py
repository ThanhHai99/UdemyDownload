# pylint: disable=R,C,W
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from udemy.compat import (
    requests,
    HEADERS,
)


class Session(object):
    def __init__(self):
        self._headers = HEADERS
        self._session = requests.sessions.Session()

    def _set_auth_headers(self, access_token="", client_id=""):
        self._headers["Authorization"] = "Bearer {}".format(access_token)
        self._headers["X-Udemy-Authorization"] = "Bearer {}".format(access_token)

    def _get(self, url):
        session = self._session.get(url, headers=self._headers)
        if session.ok or session.status_code in [502, 503]:
            return session
        if not session.ok:
            raise Exception(f"{session.status_code} {session.reason}")

    def _post(self, url, data, redirect=True):
        session = self._session.post(
            url, data, headers=self._headers, allow_redirects=redirect
        )
        if session.ok:
            return session
        if not session.ok:
            raise Exception(f"{session.status_code} {session.reason}")

    def terminate(self):
        self._set_auth_headers()
        return
