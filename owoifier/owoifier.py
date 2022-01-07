"""OwO what's this?"""

import random

from .constants import PREFIXES, SUFFIXES


MAPPINGS = [
    ["r", "w"],
    ["l", "w"],
    ["na", "nya"],
    ["ni", "nyi"],
    ["nu", "nyu"],
    ["ne", "nye"],
    ["no", "nyo"],
    ["ove", "uv"]
]

def _extend_mapping(attr):
    for old in MAPPINGS:
        new = [getattr(i, attr)() for i in old]
        if new not in MAPPINGS:
            MAPPINGS.append(new)

_extend_mapping("upper")
_extend_mapping("capitalize")

def _pick(iterable, chance):
    if 0 < chance <= 1 and random.random() <= chance:
        return random.choice(iterable)
    return

def owoify(text, prefix_chance=0.0, suffix_chance=0.0):
    """Translates English text to OwO.

    Picks a random prefix or suffix when the chance is within 0.0 and 1.0.
    Nothing is added when the chance is at 0.0. When the chance is at 1.0,
    a prefix or suffix is always added.

    Parameters
    ----------
    text : str
        Text that needs to be translated.

    prefix_chance : float, default 0.0
        Chance to get a prefix. Prefixes are isabled by default.

    suffix_chance : float, default 0.0
        Chance to get a suffix. Suffixes are disabled by default.

    Returns
    -------
    str
        The twanswated stwing.
    """
    for src, dst in MAPPINGS:
        if src in text:
            text = text.replace(src, dst)

    prefix = _pick(PREFIXES, prefix_chance)
    if prefix is not None:
        text = f"{prefix} {text}"

    suffix = _pick(SUFFIXES, suffix_chance)
    if suffix is not None:
        text = f"{text} {suffix}"

    return text
