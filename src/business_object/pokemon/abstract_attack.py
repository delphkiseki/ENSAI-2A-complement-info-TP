from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    """
    An attack
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power=None, name=None, description=None):
        # -----------------------------
        # Attributes
        # -----------------------------
        self.power: int = power
        self.name: str = name
        self.description: str = description

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def compute_damage(self, apkm) -> int:
        """
        Compute a damage

        Returns :
            int : the damage
        """
        pass
