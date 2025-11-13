from communal.collections import is_hashable, is_mapping, unique_list


def test_unique_list():
    assert unique_list([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert unique_list([3, 1, 2, 1, 3]) == [3, 1, 2]
    assert unique_list([]) == []
    assert unique_list([1]) == [1]
    assert unique_list(["a", "b", "a"]) == ["a", "b"]


def test_is_mapping():
    assert is_mapping({}) is True
    assert is_mapping({"key": "value"}) is True
    from collections import OrderedDict

    assert is_mapping(OrderedDict()) is True
    assert is_mapping([]) is False
    assert is_mapping("string") is False
    assert is_mapping(123) is False


def test_is_hashable():
    assert is_hashable(1) is True
    assert is_hashable("string") is True
    assert is_hashable((1, 2, 3)) is True
    assert is_hashable(frozenset([1, 2])) is True
    assert is_hashable([]) is False
    assert is_hashable({}) is False
    assert is_hashable(set()) is False
