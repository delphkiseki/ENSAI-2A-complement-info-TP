import random
from abc import abstractmethod

from business_object.pokemon.abstract_attack import AbstractAttack


class AbstractFormulaAttack(AbstractAttack):
    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power=None, name=None, description=None):
        super().__init__(power=power, name=name, description=description)

    # -------------------------------------------------------------------------
    # Method
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_attack_stat(self, apkm) -> float:
        pass

    @abstractmethod
    def get_defense_stat(self, dpkm) -> float:
        pass

    def compute_damage(self, apkm, dpkm) -> int:
        r = random.random(0.85, 1)

        damage = (2 * apkm.level) / 5
        damage *= self.power * self.get_attack_stat(apkm)
        damage /= self.get_defence_stat(dpkm) * 50
        damage += 2
        damage *= r

        return damage
