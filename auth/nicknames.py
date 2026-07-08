"""Random English nickname generation for new Physical Revolt accounts.

On first sign-in a user has no name yet, so we mint a friendly, URL-safe English
handle like `brave-otter-42`. The wordlists below are curated to be positive,
short, and unambiguous. `generate_nickname()` assembles them into a unique handle.
"""

import secrets

# Curated, positive, single-word, lowercase — keep them short and readable.
ADJECTIVES = [
    "brave", "calm", "clever", "bold", "bright", "swift", "keen", "lucky",
    "mellow", "nimble", "quiet", "sunny", "witty", "zesty", "cosmic", "royal",
    "amber", "coral", "jade", "noble", "rapid", "spry", "vivid", "wild",
    "gentle", "merry", "plucky", "snappy", "cheery", "dandy",
]

NOUNS = [
    "otter", "falcon", "maple", "comet", "pixel", "robot", "gecko", "koala",
    "lynx", "puffin", "quokka", "tapir", "walrus", "yak", "zebra", "badger",
    "cactus", "dynamo", "ember", "ferry", "gizmo", "harbor", "island", "jetpack",
    "kettle", "lantern", "meteor", "nugget", "orbit", "piston",
]


def generate_nickname(exists):
    """Return a unique, URL-safe English nickname (e.g. "brave-otter-42").

    Args:
        exists: a callable `exists(name: str) -> bool` that returns True when
            the candidate name is already taken (checked against the users DB).

    Contract:
        - Combine a random ADJECTIVE + NOUN + a number into a lowercase,
          hyphen-joined handle.
        - Keep drawing new candidates until `exists(candidate)` is False, then
          return that candidate. (Collisions are rare but must be handled.)
        - Use `secrets.choice(...)` / `secrets.randbelow(...)` for randomness.

    Note: `secrets` is imported above. Decide the number range/format yourself.
    """
    while True:
        name = f"{secrets.choice(ADJECTIVES)}-{secrets.choice(NOUNS)}-{secrets.randbelow(100):02d}"
        if not exists(name):
            return name
