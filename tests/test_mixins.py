from communal.mixins import MixinHooks


def test_mixin_hooks_all_base_classes():
    class Base1:
        pass

    class Base2(MixinHooks):
        pass

    class Child(Base1, Base2):
        pass

    bases = Child.all_base_classes(with_cls=False)
    assert Base1 in bases
    assert Base2 in bases
    assert Child not in bases

    bases_with_cls = Child.all_base_classes()
    assert Child in bases_with_cls


def test_mixin_hooks_call_mixin_hooks():
    called = []

    class Base1(MixinHooks):
        @classmethod
        def mixin_hook(cls, target, **kwargs):
            called.append(("Base1", target, kwargs))

    class Base2(MixinHooks):
        @classmethod
        def mixin_hook(cls, target, **kwargs):
            called.append(("Base2", target, kwargs))

    class Child(Base1, Base2):
        pass

    Child.call_mixin_hooks(test_arg="value")
    assert len(called) == 2
    assert any(c[0] == "Base1" for c in called)
    assert any(c[0] == "Base2" for c in called)
