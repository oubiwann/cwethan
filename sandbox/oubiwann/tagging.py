import cPickle as pickle
from pprint import pprint
import os

from nltk import tag, tokenize
from nltk.corpus import brown
from nltk.tag import brill


d = """"Hello, Martha. It isn't cocktail-time yet, is it?" The girl at the
table spoke without raising her head, almost without moving her lips, as
though she were afraid that the slightest breath would disturb the flaky
stuff in front of her."""


word_patterns = [
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*ould$', 'MD'),
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ness$', 'NN'),
    (r'.*ment$', 'NN'),
    (r'.*ful$', 'JJ'),
    (r'.*ious$', 'JJ'),
    (r'.*ble$', 'JJ'),
    (r'.*ic$', 'JJ'),
    (r'.*ive$', 'JJ'),
    (r'.*ic$', 'JJ'),
    (r'.*est$', 'JJ'),
    (r'^a$', 'PREP'),
    ]


brill_templates = [
    brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (1,1)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (2,2)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (1,2)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateTagsRule, (1,3)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (1,1)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (2,2)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (1,2)),
    brill.SymmetricProximateTokensTemplate(brill.ProximateWordsRule, (1,3)),
    brill.ProximateTokensTemplate(brill.ProximateTagsRule, (-1, -1), (1,1)),
    brill.ProximateTokensTemplate(brill.ProximateWordsRule, (-1, -1), (1,1)),
    ]


def _tagFactory(train_sents, word_patterns, bill_templates):
    d = tag.DefaultTagger('NN')
    ud = tag.UnigramTagger(train_sents, backoff=d)
    bud = tag.BigramTagger(train_sents, backoff=ud)
    tbud = tag.TrigramTagger(train_sents, backoff=bud)
    atbud = tag.AffixTagger(train_sents, backoff=tbud)
    ratbud = tag.RegexpTagger(word_patterns, backoff=atbud)
    brill_trainer = brill.FastBrillTaggerTrainer(ratbud, brill_templates)
    bratbud = brill_trainer.train(train_sents, max_rules=100, min_score=3)
    return bratbud


def tagFactory(train_sents, word_patterns, bill_templates, force_new=False):
    data_dir = os.path.expanduser("~/.cwethan")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    tagger_cache_file = os.path.join(data_dir, "tagger.pkl")
    if not force_new and os.path.isfile(tagger_cache_file):
        fh = open(tagger_cache_file, "rb")
        tagger = pickle.load(fh)
    else:
        tagger = _tagFactory(train_sents, word_patterns, brill_templates)
        fh = open(tagger_cache_file, "wb")
        pickle.dump(tagger, fh)
    fh.close()
    return tagger


categories = ["science_fiction", "mystery", "fiction", "adventure"]
train_sents = brown.tagged_sents(categories=categories)
tagger = tagFactory(train_sents, word_patterns, brill_templates)
sent = tokenize.word_tokenize(d)
pprint(tagger.tag(sent))
