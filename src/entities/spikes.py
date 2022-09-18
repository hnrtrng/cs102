from entities.base_entity import BaseEntity

class Spikes(BaseEntity):
    def __init__(self,damage,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.damage: int = damage