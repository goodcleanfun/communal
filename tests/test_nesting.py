from communal.nesting import deep_merge, nested_get, nested_getattr, nested_set


def test_deep_merge():
    d1 = {"a": 1, "b": {"c": 2, "d": 3}}
    d2 = {"b": {"c": 4, "e": 5}, "f": 6}
    d3 = {"b": {"d": 7}}
    d4 = {"b": {"d": 8, "e": 9}}

    d2 = deep_merge(d1, d2)
    assert d2 == {"a": 1, "b": {"c": 4, "d": 3, "e": 5}, "f": 6}

    d2 = deep_merge(d2, d3)
    assert d2 == {"a": 1, "b": {"c": 4, "d": 7, "e": 5}, "f": 6}

    d2 = deep_merge(d2, d4)
    assert d2 == {"a": 1, "b": {"c": 4, "d": 8, "e": 9}, "f": 6}


def test_nested_getattr():
    class A:
        def __init__(self):
            self.b = B()

    class B:
        def __init__(self):
            self.c = C()

    class C:
        def __init__(self):
            self.d = 1

    a = A()
    assert nested_getattr(a, "b.c.d") == 1

    class D:
        def __init__(self):
            self.b = B()

    class E:
        def __init__(self):
            self.c = [D(), D(), D()]

    e = E()
    assert nested_getattr(e, "c.0.b.c.d") == 1
    assert nested_getattr(e, "c.*.b.c.d") == [1, 1, 1]


def test_nested_get():
    d = {"a": 1, "b": {"c": 2, "d": 3}}
    assert nested_get(d, "b.c") == 2

    d = {"a": 1, "b": {"c": [{"d": 2}, {"d": 3}, {"d": 4}]}}
    assert nested_get(d, "b.c.*.d") == [2, 3, 4]

    d = {"a": 1, "b": {"c": None}}

    class Default:
        pass

    assert nested_get(d, "b.c.d", default=Default) == Default
    assert nested_get(d, "b.c.*.d", default=Default) == Default


def test_nested_set():
    d = {"a": 1, "b": {"c": 2, "d": 3}}
    nested_set(d, "b.c", 4)
    assert d == {"a": 1, "b": {"c": 4, "d": 3}}

    d = {"a": 1, "b": {"c": [{"d": 2}, {"d": 3}, {"d": 4}]}}

    nested_set(d, "b.c.1.d", 6)
    assert d == {"a": 1, "b": {"c": [{"d": 2}, {"d": 6}, {"d": 4}]}}

    d = {"a": 1, "b": {"c": None}}
    nested_set(d, "b.c.d", 7)
    assert d == {"a": 1, "b": {"c": {"d": 7}}}
