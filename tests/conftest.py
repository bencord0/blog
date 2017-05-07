import pytest


@pytest.fixture
def treq():
    from treq.testing import StubTreq
    from blog import app

    return StubTreq(app.resource())
