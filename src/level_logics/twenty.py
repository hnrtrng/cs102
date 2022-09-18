from __future__ import annotations

import pygame
import random
from typing import TYPE_CHECKING, Optional

from common.event import EventType, GameEvent
from common.types import EntityType
from common.util import now
from config import GameConfig

if TYPE_CHECKING:
    from worlds.world import World

boss_died_at_ms: Optional[int] = None


def event_handler(world: World) -> None:
    """
    Logics for level 20 ending.
    """
    global boss_died_at_ms
    for event in world.events:
        if event.get_sender_type() == EntityType.SHADOW_BOSS and event.is_type(EventType.DIE):
            boss_died_at_ms = now()
            world.set_bg_delta_alpha(-1)  # fading the background
            for shadow in world.get_entities(EntityType.SHADOW):
                shadow.die()
            for bullet in world.get_entities(EntityType.SHADOW_BULLET):
                world.remove_entity(bullet.id)
            for spikes in world.get_entities(EntityType.SPIKES):
                world.remove_entity(spikes.id)

    if boss_died_at_ms is not None:
        for _ in range(2):
            world.add_entity(EntityType.ENDING_BURGER, x=random.randint(0, GameConfig.WIDTH), y=0)

        if now() > boss_died_at_ms + 4300:
            boss_died_at_ms = None
            GameEvent(EventType.VICTORY).post()  # it's time to roll the credits