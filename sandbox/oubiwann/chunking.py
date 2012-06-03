import cPickle as pickle
from pprint import pprint
import os

from nltk import chunk, tokenize


d = """"Hello, Martha. It isn't cocktail-time yet, is it?" The girl at the
table spoke without raising her head, almost without moving her lips, as
though she were afraid that the slightest breath would disturb the flaky
stuff in front of her."""


def tagLoader():
    data_dir = os.path.expanduser("~/.cwethan")
    tagger_cache_file = os.path.join(data_dir, "tagger.pkl")
    fh = open(tagger_cache_file, "rb")
    tagger = pickle.load(fh)
    fh.close()
    return tagger


tagger = tagLoader()
sent = tokenize.word_tokenize(d)
tags = tagger.tag(sent)
print chunk.ne_chunk(tags)
