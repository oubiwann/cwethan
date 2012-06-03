~~~~
TODO
~~~~


Bugs
====

TBD


Simple Tasks
============

TBD


Initial Exploration
===================


Quest-Giver Dialog
------------------

Experiment with dialog and common parts of speech (POS) patterns:

* identify corpora that may be useful for this

  - in the brown corpus, the following would be good: adventure, fiction,
    mystery, science_fiction::

    categories = ["science_fiction", "mystery", "fiction", "adventure"]
    brown.tagged_sents(categories=categories)

  - produce examples of usage for dialog parsing with NLTK

  - examine the usefulness of induced grammars

  - given tokenized and tagged sentences, see what's possible as far as
    inferring a grammar

* generate a small corpora for fantasy/adventure dialog

* identify well-written dialog of this genre and examine POS patterns

* with a view towards a more specialized use, examine the dialogue of "quest
  givers"

  - maybe take translations of Lau Tzu? Socrates? Zen koans?

* look into what NLTK offers for storing only POS

  - not actual words themselves

  - use this to generate unique sentences/dialogues

* classify imperative statements for level of urgency

* start defining lists of "interesting" words

  - use this to generate unique sentences/dialogues


Faction Identification
----------------------

Part of the quest-giving/-accepting process is deciding whether a particular
quest meets one's over-all goals. Often goals are filtered as appropriate by
determining faction association. Not only does one not want to do a quest
for an enemy faction, one wants to protect beneficial faction relationships and
not follow quests that could jeopardize those.

Similarly, if playing in-character, one doesn't want to be inconsistent (for
instance, saving an innocent village in one quest, and then destroying it or
one like it in another). Being providing with clues as to a quest-giver's
faction association can give the player some confidence in being consistent.

There are levels of subtlety here, and deception plays a strong part (e.g,
enemies trying to get a hero to violate relationships, agreements, vows, etc.)
in the challenges that face a player... as well as the surprises that can
unfold in a well-written story.

All of these (ane more) need to be examined (psycho)linguistically so that a
game player might have good clues as to the ultimate orientation of a given
faction.


Word of Mouth
-------------

Repeating, paraphrasing, and semantically degnerating text (e.g., the
"telephone game") would be very nice to have. This could be used to provide a
support to main conversations (by primary NPCs) in a game, in that minor NPCs
or "extras" could simply start repeating something they'd "heard" from a main
NPC either shortly before a player talks to the main NCP or shortly afterwards.

The path that phrases would travel would be via associations and factions.
There would be a stronger sementic degeneration along paths that crossed from a
friendly faction to a non-friendly one. (Various sociolinguistic analyses that
have been conducted on Twitter might be great sources of inspriation here...)
