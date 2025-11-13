from communal.nulls import DoesNotExist, Omitted, obj_or_none


def test_omitted():
    assert bool(Omitted) is False
    assert not Omitted
    assert Omitted is Omitted
    assert Omitted == Omitted


def test_does_not_exist():
    assert bool(DoesNotExist) is False
    assert not DoesNotExist
    assert DoesNotExist is DoesNotExist
    assert DoesNotExist == DoesNotExist


def test_obj_or_none():
    assert obj_or_none(None) is None
    assert obj_or_none(0) is None
    assert obj_or_none("") is None
    assert obj_or_none([]) is None
    assert obj_or_none(1) == 1
    assert obj_or_none("test") == "test"
    assert obj_or_none([1, 2]) == [1, 2]
