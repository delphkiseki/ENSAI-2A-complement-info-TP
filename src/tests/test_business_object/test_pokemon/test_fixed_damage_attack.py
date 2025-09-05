from business_object.pokemon.fixed_damage_attack import FixedDamageAttack


class TestFixedDamageAttack:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = FixedDamageAttack(power=10)

        # WHEN
        damage = snorlax.compute_damage()

        # THEN
        assert damage == 10


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
