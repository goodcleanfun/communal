from communal import submodules


def test_import_submodules():
    # Test importing submodules of communal package
    modules = submodules.import_submodules("communal", recursive=True)
    assert isinstance(modules, dict)
    assert len(modules) > 0
    # Should include some known modules
    assert (
        "communal.submodules" in modules
        and modules["communal.submodules"] is submodules
    )


def test_import_submodules_with_module_object():
    import communal

    modules = submodules.import_submodules(communal, recursive=True)
    assert isinstance(modules, dict)


def test_import_submodules_invalid():
    try:
        submodules.import_submodules("123-456.package.that.does.not.exist")
        raise AssertionError("Should have raised ValueError")
    except (ValueError, ModuleNotFoundError):
        pass
