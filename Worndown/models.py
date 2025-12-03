class characters:
    def __init__(self, name, pv, atk, defce ):
        self.name = name
        self.pv = pv
        self.atk = atk
        self.defce = defce

    def take_damage(self, dmg):
        self.pv -= max(0, dmg)

    def block(self, dmg):
        reduced = max(0, dmg - self.defce)
        self.take_damage(reduced)

class monster:
    def __init__(self, name, pv, atk, defce, race):
        super().__init__(name, pv, atk, defce)
        self.race = race
        
