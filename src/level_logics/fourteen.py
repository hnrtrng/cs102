from __future__ import annotations

from typing import TYPE_CHECKING

from common import util
from common.types import EntityType, COLLECTABLE_TYPES

if TYPE_CHECKING:
    from worlds.world import World

logger = util.get_logger(__name__)


def event_handler(world: World) -> None:
    """
    Logics for ending bonus level 14.
    """
    needed_items_cnt = 60
    if world.player.count_inventory(COLLECTABLE_TYPES) >= needed_items_cnt:
        for entity in world.get_entities(EntityType.GROUND_C):
            world.remove_entity(entity.id)