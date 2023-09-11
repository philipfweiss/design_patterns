class Character:
    weapon_behaviour = None
    def fight(self):
        self.weapon_behaviour.use_weapon()

class WeaponBehaviour:
    def use_weapon(self): ...

class SwordBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print('swoosh!')

class AxeBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print('chop!')

class KnifeBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print('stab!')

class BowBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print('ping!')

class Queen(Character):
    def fight(self):
        self.weapon_behaviour.use_weapon()

class King(Character):
    weapon_behaviour = BowBehaviour()

class Troll(Character):
    weapon_behaviour = AxeBehaviour()

class Knight(Character):
    weapon_behaviour = SwordBehaviour()

class Queen(Character):
    weapon_behaviour = KnifeBehaviour()

King().fight()
Troll().fight()
Knight().fight()
Queen().fight()
