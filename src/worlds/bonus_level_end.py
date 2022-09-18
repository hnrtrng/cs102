from typing import Sequence

from common import util
from common.event import EventType, GameEvent
from common.util import now
from worlds.base_scene import BaseScene


class BonusLevelEnd(BaseScene):
    """The congrats page for finishing any bonus level."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.created_at_ms: int = now()

    def tick(self, events: Sequence[GameEvent]) -> bool:
        super().tick(events)
        # TODO: clean up, move hardcoded values to configs
        util.display_text(
            self.screen,
            text="Congratulations! You cleared the extra level!",
            x=310,
            y=270,
            font_size=32,
        )
        now_ms = now()
        if now_ms - self.created_at_ms > 1800:
            util.display_text(
                self.screen, text="Returning to the main menu ...", x=420, y=370, font_size=32
            )
        if now_ms - self.created_at_ms > 4100:
            GameEvent(EventType.SHOW_MENU_AND_RESET_LEVEL_ID).post()
        return True
