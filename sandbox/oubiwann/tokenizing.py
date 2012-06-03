from pprint import pprint

from nltk import tag, tokenize
import nltk.data


d = """"Hello, Martha. It isn't cocktail-time yet, is it?" The girl at the
table spoke without raising her head, almost without moving her lips, as
though she were afraid that the slightest breath would disturb the flaky
stuff in front of her."""


t = tokenize.word_tokenize(d)
pprint(tag.pos_tag(t))
