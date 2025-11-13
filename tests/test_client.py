from communal.client import ClientProxy


def test_client_proxy():
    class MockClient:
        def __init__(self, a: str, b: int):
            self.a = a
            self.b = b

        def test(self):
            return f"{self.a}.{self.b}"

    class MockClientSession(ClientProxy):
        def __init__(self):
            pass

        def configure(self, a: str, b: int):
            self.client = MockClient(a, b)

    session = MockClientSession()
    session.configure("a", 1)

    assert session.test() == "a.1"
