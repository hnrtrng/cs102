import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

import pygame

from common.types import EntityType

pygame.init()

ASSET_DIR = Path("assets")
DATA_DIR = Path("data")

FONT_PATH = ASSET_DIR / "fonts" / "arial.ttf"


class Color:
    DEFAULT = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    LOADING_BAR = (255, 51, 153)
    PLAYER_HP_BAR = (255, 51, 153)
    BOSS_HP_BAR = (255, 51, 153)
    TEXT_DIALOGUE_SUBJECT = (19, 2, 150)
    TEXT_DIALOGUE = (204, 115, 14)
    TEXT_INVENTORY_CNT = (255, 255, 0)
    TEXT_INTERNSHIP_REPORT = (242, 222, 179)
    TEXT_CREDIT = (230, 147, 154)


class GameConfig:
    DEBUG: bool = True
    NAME: str = "STEAM Valley"
    FPS: int = 60
    WIDTH: int = 1248
    HEIGHT: int = 768
    TILE_SIZE: int = 30
    PLAYER_SOFT_EDGE_WIDTH: int = 300

    VICTORY_BACKGROUND: Path = ASSET_DIR / "backgrounds" / "victory.png"

    MENU_MUSIC: Path = ASSET_DIR / "sounds" / "background" / "menu.wav"
    MENU_MUSIC_VOLUME: float = 0.3

    DEFEATED_MUSIC: Path = ASSET_DIR / "sounds" / "background" / "defeated.wav"
    VICTORY_MUSIC: Path = ASSET_DIR / "sounds" / "background" / "victory.wav"
    BONUS_LEVEL_END_MUSIC: Path = ASSET_DIR / "sounds" / "background" / "victory.wav"

    INGAME_MUSIC_VOLUME: float = 0.3
    SOUND_EFFECT_VOLUME: float = 0.3


class LevelLoadingBarConfig:
    WIDTH: int = 600
    HEIGHT: int = 100
    STEP = 3 if not GameConfig.DEBUG else 10  # how fast the loading bar goes


class DialogueBoxConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "dialogue_box.png"
    WIDTH: int = 800
    HEIGHT: int = 200
    SCALE: Tuple[int, int] = (WIDTH, HEIGHT)
    X: int = (GameConfig.WIDTH - WIDTH) // 2
    Y: int = GameConfig.HEIGHT - HEIGHT + 24
    PADDING_X: int = 108
    PADDING_Y: int = 30
    LINE_HEIGHT: int = 24


class PlayerConfig:
    DEFAULT_X: int = 350
    DEFAULT_Y: int = 400
    SPRITE_PATH: Path = ASSET_DIR / "player"
    SCALE: float = 0.125
    GRAVITY: float = 1.25
    SPEED: int = 5
    JUMP_VERTICAL_SPEED: int = 18
    JUMP_WITH_TRAMPOLINE_SPEED: int = 27
    # minimal time until switching to the next sprite in sequence
    ANIMATION_INTERVAL_MS: int = 70 * 60 // GameConfig.FPS
    INITIAL_HP: int = 100

    HURT_DURATION_MS: int = 320

    # TODO: we have 7 sprites for ActionType.THROW but only use 2-3 now
    THROW_DURATION_MS: int = 170 * 60 // GameConfig.FPS
    TIME_UNTIL_ANOTHER_THROW_MS: int = 250

class PlayerHpBarConfig:
    X: int = 24
    Y: int = 44
    WIDTH: int = 250
    HEIGHT: int = 30

class PlayerInventoryConfig:
    X: int = 290
    Y: int = 44
    X_STEP: int = 60  # distance between 2 consecutive items

    # the simple vertical divider
    SPRITE_PATH: Path = ASSET_DIR / "items" / "player_inventory.png"
    SCALE: float = 1.3

    TILE_SIZE: int = 36


class PlayerBulletConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "player_bullet.png"
    SCALE: float = 0.65
    SPEED: int = 24
    JUMP_WITH_TRAMPOLINE_SPEED: int = 21
    GRAVITY: float = 1.7
    DAMAGE: int = 10

    # initial vertical movement
    INIT_DY: int = -10

    # the time between creation and deletion of entities of this type
    TTL_MS: int = 1000 * 60 // GameConfig.FPS


class ShadowConfig:
    SPRITE_PATH: Path = ASSET_DIR / "npcs" / "shadow"
    SCALE: float = 0.135
    ANIMATION_INTERVAL_MS: int = 200
    SPEED: int = 1
    DAMAGE: int = 10
    INVUL_DURATION_FOR_PLAYER_MS: int = 400

    ATTACK_INTERVAL_MS: int = 10000


class ShadowBossConfig:
    SPRITE_PATH: Path = ASSET_DIR / "npcs" / "shadow"
    SCALE: float = 0.45
    ANIMATION_INTERVAL_MS: int = 200
    SPEED: int = 1
    DAMAGE: int = 20
    INVUL_DURATION_FOR_PLAYER_MS: int = 2000
    INITIAL_HP: int = 500

    ANGRY_INTERVAL_MS: int = 4000
    ANGRY_DURATION_MS: int = 2000

    HURT_DURATION_MS: int = 500


class ShadowBulletConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "shadow_bullet.png"
    SCALE: float = 0.0375
    SPEED: int = 4
    JUMP_WITH_TRAMPOLINE_SPEED: int = 16
    GRAVITY: float = 0.4
    DAMAGE: int = 10
    INVUL_DURATION_FOR_PLAYER_MS: int = 1000

    # initial vertical movement
    INIT_DY: int = -15

    # the time between creation and deletion of entities of this type
    TTL_MS: int = 3000


class SpikesConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "spikes.png"
    SCALE: int = 1
    DAMAGE: int = 2
    INVUL_DURATION_FOR_PLAYER_MS: int = 650


class EndingBurgerConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "player_bullet.png"
    SCALE: float = 0.5
    JUMP_WITH_TRAMPOLINE_SPEED: int = 20
    GRAVITY: float = 2.1

    # the time between creation and deletion of entities of this type
    TTL_MS: int = 420


class TrampolineConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "trampoline"
    SCALE: float = 0.1875
    ANIMATION_INTERVAL_MS: int = 60
    ANIMATION_DURATION_MS: int = 700

class ExtraHpBoxConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "extra_hp_box.png"
    HP_BOOST: int = 20


@dataclass
class NpcConfig:
    entity_type: EntityType
    scale: float = 0.5
    animation_interval_ms: int = 2500
    default_alpha: int = 180  # 255 is fully opaque

    def __post_init__(self):
        with open(
            DATA_DIR / "dialogues" / f"{self.entity_type.name.lower()}.json", encoding="utf-8"
        ) as fin:
            data = json.load(fin)
            self.name = data["name"]
            self.dialogues = data["dialogues"]

        self.sprite_path = ASSET_DIR / "npcs" / self.entity_type.name.lower()


@dataclass
class WorldData:
    level_id: int
    data: Optional[List] = None
    bg_path: Optional[Path] = None

    def __post_init__(self):
        self.bg_path = ASSET_DIR / "backgrounds" / f"level_{self.level_id}.png"

        with open(DATA_DIR / "levels" / f"{self.level_id}.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            self.data = [
                [EntityType(int(tile or EntityType.EMPTY.value)) for tile in row] for row in reader
            ]
