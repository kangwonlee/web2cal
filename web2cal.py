import functools
import sys
import urllib.parse as up

import pandas as pd
import requests


def main(argv=sys.argv):
    r = requests.get(get_avs_url())
    assert r.ok, r


@functools.lru_cache()
def get_avs_url():
    return "https://www.automatedvehiclessymposium.org/program/keynotes-plenaries"


if "__main__" == __name__:
    main(sys.argv)
