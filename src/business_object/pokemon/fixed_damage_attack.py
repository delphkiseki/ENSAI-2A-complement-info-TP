from business_object.pokemon.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power=None, name=None, description=None):
        super().__init__(power=power, name=name, description=description)

    # -------------------------------------------------------------------------
    # Method
    # -------------------------------------------------------------------------

    def compute_damage(self) -> int:
        return self.power
