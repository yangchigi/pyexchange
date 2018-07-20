# -*- coding: utf-8 -*-
import requests
import json
import logging


class HttpUtil:
    """
    http 요청 유틸
    """

    def get(self, url, params=None):
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            logging.error('get(%s) failed(%d)' % (url, resp.status_code))
            if resp.text is not None:
                logging.error('resp: %s' % resp.text)
            return None
        return json.loads(resp.text)
