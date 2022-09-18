from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from common.event import GameEvent
from common.types import ActionType
from config import TrampolineConfig
from entities.movable_entity import MovableEntity

if TYPE_CHECKING:
    from worlds.world import World


class Bullet(MovableEntity):
    def __init__(self, damage, jump_with_trampoline_speed: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage = damage
        self.jump_with_trampoline_speed: int = jump_with_trampoline_speed
    def update(self, events: Sequence[GameEvent], world: World) -> None:
        super().update(events, world)
        for trampoline in self.world.get_trampolines():
            if self.collide(trampoline) and self.rect.bottom > trampoline.rect.top:
                trampoline.set_action(
                    ActionType.ANIMATE, duration_ms=TrampolineConfig.ANIMATION_DURATION_MS
                )
                self.jump_with_trampoline()