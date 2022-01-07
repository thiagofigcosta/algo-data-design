import re
import unicodedata

from unidecode import unidecode

ALPHANUMERIC_SPACE_PATTERN = re.compile(r'[^ \w+]+', re.UNICODE)
ALPHANUMERIC_PATTERN = re.compile(r'[^\w]+', re.UNICODE)


def strip_accents(string):
    try:
        string = unidecode(string, 'utf-8')
    except NameError:  # unicode is a default on python 3
        pass

    return unicodedata.normalize('NFD', string).encode('ascii', 'ignore').decode("utf-8")


def strip_non_alpha(string):
    return ALPHANUMERIC_PATTERN.sub('', string)


def strip_non_alpha_or_non_space(string):
    return ALPHANUMERIC_SPACE_PATTERN.sub('', string)
