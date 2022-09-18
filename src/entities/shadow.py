from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING, Sequence

from common.event import GameEvent
from common.types import EntityType
from common.util import now
from config import ShadowConfig
from entities.animated_entity import AnimatedEntity
from entities.bullet import Bullet

if TYPE_CHECKING:
    from worlds.world import World

logger = logging.getLogger(__name__)


class Shadow(AnimatedEntity):
    """Shadow entity haunting STEAM Valley."""

    def __init__(self, damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage = damage
        self.time_since_last_attack = now()

        # Shadow may move in a random direction at the start.
        self.move_random()

    def update(self, events: Sequence[GameEvent], world: World) -> None:
        super().update(events, world)
        if self.is_dying:
            return

        # Shadow has a probability to change direction.
        rand_move = random.randint(1, 30)
        if rand_move == 1:
            self.move_opposite()

        self._handle_get_hit()

        if now() - self.time_since_last_attack >= ShadowConfig.ATTACK_INTERVAL_MS:
            self.attack()

    def attack(self):
        for _ in range(self.num_of_bullets_shot()):
            bullet_id = self.world.add_entity(
                EntityType.SHADOW_BULLET,
                int(self.rect.centerx + self.rect.width / 2),
                int(self.rect.centery + self.rect.height / 2),
            )

            bullet: Bullet = self.world.get_entity(bullet_id)
            bullet.move_random()
        self.time_since_last_attack = now()

    def num_of_bullets_shot(self):
        ran = random.random()
        if ran < 0.4:
            return 1
        if 0.4 <= ran < 0.7:
            return 2
        if 0.7 <= ran < 0.9:
            return 3
        return 4

    def die(self):
        super().die()
        self.set_remaining_ttl_ms(self.animation_interval_ms * 6)

    def _handle_get_hit(self):
        for bullet in self.world.get_entities(EntityType.PLAYER_BULLET):
            if self.collide(bullet):
                self.start_hurt(0)  # For Sound effects - skip hurt state
                self.die()

        if self.collide(self.world.player):
            self.world.player._handle_get_hit()
            self.die()
