import importlib.util
import pathlib
import types


def import_submodules(package, recursive=True):
    """Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """

    if isinstance(package, types.ModuleType):
        package = package.__name__
    elif not isinstance(package, str):
        raise ValueError(f"Invalid package: {package}")

    if package.endswith(".py"):
        package = package[:-3]

    if package.endswith(".__init__"):
        package = package.rsplit(".", 1)[0]

    spec = importlib.util.find_spec(package)
    if spec is None or not spec.submodule_search_locations:
        raise ValueError(f"{package} is not a package")
    parent_path = pathlib.Path(spec.submodule_search_locations[0])
    if recursive:
        paths = parent_path.rglob("*.py")
    else:
        paths = parent_path.glob("*.py")

    results = {}

    for path in paths:
        rel_path = path.relative_to(parent_path).with_suffix("")
        module_name = ".".join([package] + list(rel_path.parts))
        results[module_name] = importlib.import_module(module_name)

    return results
