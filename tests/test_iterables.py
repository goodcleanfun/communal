from communal.iterables import (
    argmax,
    batch_iter,
    combine_lists,
    flatten,
    flatten_args,
    is_iterable,
    is_sequence,
    iter_len,
    iterify,
    listify,
    merge_values_at_indices,
    pairwise,
    partition,
    powerset,
    round_robin,
    split_index_on_condition,
    split_on_condition,
    split_on_indices,
)


def test_is_sequence():
    assert is_sequence([1, 2, 3]) is True
    assert is_sequence((1, 2, 3)) is True
    assert is_sequence("string") is False
    assert is_sequence(b"bytes") is False
    assert is_sequence(123) is False


def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable({1, 2, 3}) is True
    assert is_iterable("string") is False
    assert is_iterable(b"bytes") is False
    assert is_iterable(123) is False


def test_iterify():
    assert list(iterify(5)) == [5]
    assert list(iterify([1, 2, 3])) == [1, 2, 3]
    assert list(iterify(None)) == []
    assert list(iterify(None, empty_list_if_none=False)) == [None]


def test_listify():
    assert listify(5) == [5]
    assert listify([1, 2, 3]) == [1, 2, 3]
    assert list(listify((1, 2, 3))) == [1, 2, 3]
    assert listify(range(3)) == [0, 1, 2]
    assert listify(None) == []


def test_flatten():
    assert list(flatten([[1, 2], [3, 4]])) == [1, 2, 3, 4]
    assert list(flatten([[1], [2, 3]])) == [1, 2, 3]


def test_flatten_args():
    assert flatten_args(1, 2, 3) == [1, 2, 3]
    assert flatten_args([1, 2], 3) == [1, 2, 3]
    assert flatten_args(1, [2, 3]) == [1, 2, 3]


def test_combine_lists():
    assert combine_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert combine_lists([1], [2], [3]) == [1, 2, 3]


def test_pairwise():
    assert list(pairwise([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4)]
    assert list(pairwise([])) == []
    assert list(pairwise([1])) == []


def test_partition():
    odds, evens = partition(lambda x: x % 2 == 0, range(10))
    assert list(evens) == [0, 2, 4, 6, 8]
    assert list(odds) == [1, 3, 5, 7, 9]


def test_powerset():
    result = list(powerset([1, 2, 3]))
    assert len(result) == 8  # 2^3
    assert () in result
    assert (1,) in result
    assert (1, 2, 3) in result


def test_round_robin():
    result = list(round_robin("ABC", "D", "EF"))
    assert result == ["A", "D", "E", "B", "F", "C"]


def test_batch_iter():
    batches = list(batch_iter([1, 2, 3, 4, 5], 2))
    assert batches == [[1, 2], [3, 4], [5]]

    batches2 = list(batch_iter([1, 2, 3, 4], 2))
    assert batches2 == [[1, 2], [3, 4]]


def test_iter_len():
    assert iter_len([1, 2, 3, 4, 5]) == 5
    assert iter_len(range(10)) == 10
    assert iter_len([]) == 0


def test_argmax():
    assert argmax([1, 5, 3, 2, 4]) == 1
    assert argmax([10, 20, 30]) == 2
    assert argmax([5]) == 0


def test_split_index_on_condition():
    vals = [1, 2, 3, 4, 5]
    true_indices, false_indices = split_index_on_condition(vals, lambda x: x % 2 == 0)
    for i in true_indices:
        assert vals[i] % 2 == 0
    for i in false_indices:
        assert vals[i] % 2 != 0


def test_split_on_condition():
    evens, odds = split_on_condition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert evens == [2, 4]
    assert odds == [1, 3, 5]


def test_split_on_indices():
    match, no_match = split_on_indices([0, 1, 2, 3, 4], [1, 3])
    assert match == [1, 3]
    assert no_match == [0, 2, 4]


def test_merge_values_at_indices():
    result = merge_values_at_indices([0, 1, 2, 3, 4], [1, 3], [10, 30])
    assert result == [0, 10, 1, 2, 30, 3, 4]
