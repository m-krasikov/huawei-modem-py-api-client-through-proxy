import logging

from huaweisms.api.config import MODEM_HOST
from huaweisms.api.common import get_from_url


logger = logging.getLogger(__name__)
life_proxy = {'http': 'http://poxy:1Modems1@176.36.24.156:7121',
              'https': 'http://poxy:1Modems1@176.36.24.156:7121'
              }


def get_session_token_info(base_url: str = None, proxy=None):
    """
    Get session token information

    :param base_url: base url for the modem api
    :return:
    """
    if base_url is None:
        logger.warning(
            'calling %s.get_session_token_info without base_url argument is deprecated',
            __name__
        )
        base_url = 'http://{}/api'.format(MODEM_HOST)
    url = "{}/webserver/SesTokInfo".format(base_url)
    return get_from_url(url, proxy=proxy, timeout=30)
