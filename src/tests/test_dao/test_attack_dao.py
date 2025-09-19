import time

from dao.attack_dao import AttackDao
from business_object.attack.special_attack import SpecialFormulaAttack

class TestAttackDao:
    def test_find_attack_by_id(self):
        # GIVEN
        existing_id_attack = 1

        # WHEN
        attack = AttackDao().find_attack_by_id(existing_id_attack)

        # THEN
        assert attack is not None
        assert attack.id == existing_id_attack

    def test_add_attack_ok(self):
        # GIVEN
        attack_dao = AttackDao()
        attack = SpecialFormulaAttack(
            power=25,
            name=f"test{time.time()}",
            description="ceci est un test",
            accuracy=10,
            element="eau",
        )
        # WHEN
        created = attack_dao.add_attack(attack)

        # THEN
        assert created
        assert attack.id is not None

    def test_update_attack(self):
        # GIVEN
        attack_dao = AttackDao()
        attack = SpecialFormulaAttack(
            id=1,
            power=25,
            name=f"test{time.time()}",
            description="ceci est un test",
            accuracy=10,
            element="eau",
        )

        # WHEN
        updated = attack_dao.update_attack(attack)

        # THEN
        assert updated

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])