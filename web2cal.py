import functools
import pprint
import sys
import urllib.parse as up

import lxml.html
import pandas as pd
import requests


def main(argv=sys.argv):
    url = get_keynote_url()
    print(url)
    print(get_breakouts_url())


@functools.lru_cache()
def get_keynote_url() -> str:
    return get_url(get_avs_keynote_url())


@functools.lru_cache()
def get_url(avs_url:str) -> str:
    r = requests.get(avs_url)

    assert r.ok, r

    # https://stackoverflow.com/questions/33817325
    webpage = lxml.html.fromstring(r.content)
    url = tuple(
            filter(lambda link: 'a2zinc' in up.urlparse(link).netloc, webpage.xpath('//a/@href'))
        )[0]
    return url


def get_breakouts_url() -> str:
    return get_url(get_avs_breakout_url())


@functools.lru_cache()
def get_avs_keynote_url() -> str:
    return "https://www.automatedvehiclessymposium.org/program/keynotes-plenaries"


@functools.lru_cache()
def get_avs_breakout_url() -> str:
    return "https://www.automatedvehiclessymposium.org/program/breakouts"


if "__main__" == __name__:
    main(sys.argv)
