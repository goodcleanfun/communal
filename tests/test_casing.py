from communal.casing import camel_to_snake_case, to_camel_case, to_title_case


def test_camel_to_snake():
    s = "ToSnakeCase"
    assert camel_to_snake_case(s) == "to_snake_case"


def test_snake_to_camel():
    s = "to_snake_case"
    assert to_camel_case(s) == "ToSnakeCase"


def test_to_title_case():
    sl = "lower"
    assert to_title_case(sl) == "Lower"
    su = "UPPER"
    assert to_title_case(su) == "Upper"
    sm = "MixedCase"
    assert to_title_case(sm) == "MixedCase"
