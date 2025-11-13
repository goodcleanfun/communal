from communal.properties import cached_classproperty, cached_property, classproperty


def test_classproperty():
    class TestClass:
        @classproperty
        def prop(cls):
            return "value"

    assert TestClass.prop == "value"


def test_cached_classproperty():

    class TestClass:
        call_count = 0

        @cached_classproperty
        def prop(cls):
            cls.call_count += 1
            return "value"

    assert TestClass.prop == "value"
    assert TestClass.call_count == 1
    assert TestClass.prop == "value"
    assert TestClass.call_count == 1


def test_cached_property():

    class TestClass:
        call_count = 0

        @cached_property
        def prop(self):
            self.call_count += 1
            return self.call_count

    obj = TestClass()
    assert obj.prop == 1
    assert obj.call_count == 1
    assert obj.prop == 1
    assert obj.call_count == 1


def test_cached_property_delete():
    class TestClass:
        @cached_property
        def prop(self):
            return "value"

    obj = TestClass()
    assert obj.prop == "value"
    del obj.prop
    assert obj.prop == "value"


def test_cached_property_set():
    class TestClass:
        @cached_property
        def prop(self):
            return "original"

    obj = TestClass()
    assert obj.prop == "original"
    obj.prop = "new_value"
    assert obj.prop == "new_value"
