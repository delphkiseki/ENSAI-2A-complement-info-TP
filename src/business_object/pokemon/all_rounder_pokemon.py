from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None) -> None:
        super().__init__(
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            type_pk="AllRounder",
        )

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon of type AllRounder.

        Returns :
            float : the multiplier
        """

        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200

        return multiplier
