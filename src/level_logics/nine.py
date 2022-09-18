from __future__ import annotations

from typing import TYPE_CHECKING

from common.event import EventType, GameEvent
from common.types import EntityType

if TYPE_CHECKING:
    from worlds.world import World


def event_handler(world: World) -> None:
    """
    Logics for some specific events in level 1.
    """
    for event in world.events:
        npc_chu_huy_id = world.get_entity_id_by_type(EntityType.NPC_CHU_HUY)
        if event.get_sender_id() == npc_chu_huy_id and event.is_type(EventType.NPC_DIALOGUE_END):
            GameEvent(EventType.LEVEL_END).post()