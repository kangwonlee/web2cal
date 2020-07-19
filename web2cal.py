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


def get_keynote_url():
    r = requests.get(get_avs_url())

    assert r.ok, r

    # https://stackoverflow.com/questions/33817325
    webpage = lxml.html.fromstring(r.content)
    url = tuple(
            filter(lambda link: 'a2zinc' in up.urlparse(link).netloc, webpage.xpath('//a/@href'))
        )[0]
    return url


@functools.lru_cache()
def get_avs_url():
    return "https://www.automatedvehiclessymposium.org/program/keynotes-plenaries"


if "__main__" == __name__:
    main(sys.argv)
