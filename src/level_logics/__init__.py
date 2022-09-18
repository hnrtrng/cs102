"""
Each level may have some custom logics, depending on the game story.

For example, in level 1 we handle when the quest TRAMPOLINE is complete,
or when the Player gets to the end of the level.

Refer to two.py to write your own levels and stories.
"""
from typing import Callable, Optional

from level_logics import (
    two,
    nine,
    ten,
    eleven,
    twelve,
    thirteen,
    fourteen,
    fifteen,
    sixteen,
    seventeen,
    nineteen,
    twenty
)

_HANDLERS = {
    2: two.event_handler,
    9: nine.event_handler,
    10: ten.event_handler,
    11: eleven.event_handler,
    12: twelve.event_handler,
    13: thirteen.event_handler,
    14: fourteen.event_handler,
    15: fifteen.event_handler,
    16: sixteen.event_handler,
    17: seventeen.event_handler,
    19: nineteen.event_handler,
    20: twenty.event_handler
}

def get_event_handler(level_id: int) -> Optional[Callable]:
    return _HANDLERS.get(level_id)
