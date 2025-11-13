from communal.enum import StringEnum


def test_string_enum():
    class Status(StringEnum):
        ACTIVE = "active"
        INACTIVE = "inactive"
        PENDING = "pending"

    assert str(Status.ACTIVE) == "active"
    assert Status.ACTIVE == "active"
    assert Status.ACTIVE.display == "Active"
    assert Status.INACTIVE.display == "Inactive"
    assert Status.PENDING.display == "Pending"

    assert Status.display_name(Status.ACTIVE) == "ACTIVE"

    choices = Status.choices()
    assert len(choices) == 3
    assert ("active", "ACTIVE") in choices

    assert Status.from_value("active") == Status.ACTIVE
