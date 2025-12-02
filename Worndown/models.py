class Characters:
    def __init__(self, name, pv, atk, defce ):
        self.name = name
        self.pv = pv
        self.atk = atk
        self.defce = defce

    def take_damage(self, dmg):
        self.pv -= max(0, dmg)

    def block
        
