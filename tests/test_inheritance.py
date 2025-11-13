from communal.inheritance import update_from_bases


def test_update_from_bases():
    class Base1:
        items = {"a": 1, "b": 2}

    class Base2:
        items = {"c": 3, "d": 4}

    class Child(Base1, Base2):
        items = {"e": 5}

    result = update_from_bases(Child, "items", Child.__bases__)
    assert result == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


def test_update_from_bases_override():
    class Base1:
        items = {"a": 1}

    class Child(Base1):
        items = {"b": 2}

    result = update_from_bases(
        Child, "items", Child.__bases__, override_with_child=True
    )
    assert result == {"b": 2}


def test_update_from_bases_no_update():
    class Base1:
        items = {"a": 1}

    class Child(Base1):
        items = {"b": 2}

    result = update_from_bases(Child, "items", Child.__bases__, update_with_child=False)
    assert result == {"a": 1}
