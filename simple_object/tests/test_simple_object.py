from simple_object import SimpleObject


def test_default_object():
    default_object = SimpleObject()
    assert default_object.get_value() == 'Initial value'
    assert default_object.get_value() != 'Something else'
    assert default_object.get_last_version() == 0


def test_change_default_object():
    default_object = SimpleObject()
    default_object = default_object.set_value(4)
    assert default_object.get_value() == 4
    assert default_object.get_value() != 'Something else'
    assert default_object.get_last_version() == 1


def test_change_value_with_version():
    default_object = SimpleObject()
    default_object = default_object.set_value(42, version=16)
    assert default_object.get_value() == 42
    assert default_object.get_last_version() == 16


def test_unable_to_specify_lower_value():
    default_object = SimpleObject()
    default_object = default_object.set_value(42, version=16)
    default_object = default_object.set_value(43, version=15)
    assert default_object.get_value() == 42
    assert default_object.get_last_version() == 16


def test_get_random_version_value():
    default_object = SimpleObject()
    default_object = default_object.set_value(42, version=16)
    assert default_object.get_value(version=15) == 'Initial value'
    assert default_object.get_value(version=16) == 42
    assert default_object.get_value(version=312) == 42
    assert default_object.get_last_version() == 16


def test_that_impossible_set_version_zero_or_less():
    default_object = SimpleObject()
    default_object = default_object.set_value(14, version=0)
    assert default_object.get_value() == 'Initial value'
    default_object = default_object.set_value(15, version=-4)
    assert default_object.get_value() == 'Initial value'
    assert default_object.get_last_version() == 0
