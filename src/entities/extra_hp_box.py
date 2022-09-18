from entities.base_entity import BaseEntity

class ExtraHpBox(BaseEntity):
    def __init__(self, hp_boost: int,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.hp_boost: int = hp_boost