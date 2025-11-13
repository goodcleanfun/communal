from communal.functions import (
    ChainedFunction,
    FunctionMap,
    FunctionZipMap,
    Pipeline,
    VectorFunction,
    all_attrs_not_none,
    all_keys_not_none,
    argmax,
    argmin,
    attr_get,
    attr_or_key_getter,
    equal_to,
    greater_than,
    greater_than_or_equal_to,
    has_all_attrs,
    has_all_keys,
    hybridmethod,
    if_none,
    is_none,
    item_get,
    less_than,
    less_than_or_equal_to,
    map_values,
    nop,
    not_equal_to,
    not_none,
    regex_sub,
    stop_on_conditions,
    stop_on_input_values,
    str_to_bool,
)


def test_nop():
    assert nop(5) == 5
    assert nop("test") == "test"
    assert nop(None) is None


def test_equal_to():
    eq_5 = equal_to(5)
    assert eq_5(5) is True
    assert eq_5(3) is False


def test_not_equal_to():
    ne_5 = not_equal_to(5)
    assert ne_5(5) is False
    assert ne_5(3) is True


def test_argmin():
    assert argmin([5, 2, 8, 1, 9]) == 3
    assert argmin([10]) == 0


def test_argmax():
    assert argmax([5, 2, 8, 1, 9]) == 4
    assert argmax([10]) == 0


def test_is_none():
    assert is_none(None) is True
    assert is_none(0) is False
    assert is_none("") is False


def test_not_none():
    assert not_none(None) is False
    assert not_none(0) is True
    assert not_none("") is True


def test_if_none():
    default_5 = if_none(5)
    assert default_5(None) == 5
    assert default_5(10) == 10
    assert default_5(0) == 0


def test_stop_on_input_values():
    @stop_on_input_values(None, default=0)
    def add_one(x):
        return x + 1

    assert add_one(5) == 6
    assert add_one(None) == 0

    @stop_on_input_values(0, -1, default=None)
    def divide(x):
        return 10 / x

    assert divide(2) == 5.0
    assert divide(0) is None
    assert divide(-1) is None


def test_stop_on_conditions():
    @stop_on_conditions(lambda x: x > 0, default=0)
    def square(x):
        return x * x

    assert square(5) == 25
    assert square(-5) == 0


def test_str_to_bool():
    assert str_to_bool("TRUE") is True
    assert str_to_bool("true") is True
    assert str_to_bool("T") is True
    assert str_to_bool("YES") is True
    assert str_to_bool("1") is True
    assert str_to_bool("FALSE") is False
    assert str_to_bool("false") is False
    assert str_to_bool("NO") is False
    assert str_to_bool("0") is False
    assert str_to_bool("maybe") is None
    assert str_to_bool("") is None


def test_attr_get():
    class Obj:
        def __init__(self):
            self.name = "Zora"
            self.age = 30

    obj = Obj()
    get_name = attr_get("name")
    assert get_name(obj) == "Zora"

    get_name_age = attr_get("name", "age")
    assert get_name_age(obj) == ["Zora", 30]


def test_item_get():
    d = {"name": "Langston", "age": 25}
    get_name = item_get("name")
    assert get_name(d) == "Langston"

    get_name_age = item_get("name", "age")
    assert get_name_age(d) == ["Langston", 25]


def test_attr_or_key_getter():
    class Obj:
        def __init__(self):
            self.last_name = "Robeson"

    obj = Obj()
    getter = attr_or_key_getter("last_name")
    assert getter(obj) == "Robeson"

    d = {"last_name": "Robeson"}
    assert getter(d) == "Robeson"


def test_has_all_attrs():
    class Obj:
        def __init__(self):
            self.name = "Zora"
            self.age = 30

    obj = Obj()
    has_name = has_all_attrs("name")
    assert has_name(obj) is True

    has_name_age = has_all_attrs("name", "age")
    assert has_name_age(obj) is True
    assert has_name_age(Obj()) is True


def test_all_attrs_not_none():
    class Obj:
        def __init__(self):
            self.name = "Zora"
            self.age = None

    obj = Obj()
    check_name = all_attrs_not_none("name")
    assert check_name(obj) is True

    check_name_age = all_attrs_not_none("name", "age")
    assert check_name_age(obj) is False


def test_has_all_keys():
    d = {"name": "Langston", "age": 25}
    has_name = has_all_keys("name")
    assert has_name(d) is True

    has_name_age = has_all_keys("name", "age")
    assert has_name_age(d) is True
    assert has_name_age({"name": "Langston"}) is False


def test_all_keys_not_none():
    d = {"name": "Langston", "age": None}
    check_name = all_keys_not_none("name")
    assert check_name(d) is True

    check_name_age = all_keys_not_none("name", "age")
    assert check_name_age(d) is False


def test_map_values():
    mapper = map_values({1: "one", 2: "two"})
    assert mapper(1) == "one"
    assert mapper(2) == "two"
    assert mapper(3) == 3


def test_less_than():
    lt_5 = less_than(5)
    assert lt_5(3) is True
    assert lt_5(5) is False
    assert lt_5(7) is False


def test_greater_than():
    gt_5 = greater_than(5)
    assert gt_5(7) is True
    assert gt_5(5) is False
    assert gt_5(3) is False


def test_less_than_or_equal_to():
    lte_5 = less_than_or_equal_to(5)
    assert lte_5(3) is True
    assert lte_5(5) is True
    assert lte_5(7) is False


def test_greater_than_or_equal_to():
    gte_5 = greater_than_or_equal_to(5)
    assert gte_5(7) is True
    assert gte_5(5) is True
    assert gte_5(3) is False


def test_regex_sub():
    subber = regex_sub(r"\d+", "$NUMBER$")
    assert subber("abc123def") == "abc$NUMBER$def"
    assert subber("test456test") == "test$NUMBER$test"


def test_pipeline():
    pipeline = Pipeline(lambda x: x * 2, lambda x: x + 1)
    assert pipeline(5) == 11  # 5 * 2 + 1


def test_function_map():
    func_map = FunctionMap(lambda x: x * 2, lambda x: x + 1)
    result = func_map(5)
    assert result == (10, 6)

    func_map_list = FunctionMap(lambda x: x * 2, use_tuple=False)
    result = func_map_list(5)
    assert result == [10]


def test_function_zip_map():
    func_zip = FunctionZipMap(lambda x: x * 2, lambda x: x + 1)
    result = func_zip([5, 10])
    assert result == (10, 11)


def test_vector_function():
    vec_func = VectorFunction(lambda x: x * 2)
    result = vec_func([1, 2, 3, 4])
    assert result == [2, 4, 6, 8]


def test_chained_function():
    chain_func = ChainedFunction(lambda x: x**2)
    result = chain_func([[1, 2, 3], 4, [5, 6, 7], 8, 9])
    assert result == [1, 4, 9, 16, 25, 36, 49, 64, 81]


def test_hybridmethod():
    class TestClass:
        @hybridmethod
        def method(cls_or_self, x):
            return cls_or_self, x

    result = TestClass.method(5)
    assert result[0] == TestClass
    assert result[1] == 5

    obj = TestClass()
    result = obj.method(5)
    assert result[0] == obj
    assert result[1] == 5
