import pytest


@pytest.mark.asyncio
async def test_index(treq):
    response = await treq.get("http://localhost/")
    assert response.code == 200

    content = await response.content()
    assert content == b'Hello World!\n'


@pytest.mark.asyncio
async def test_404(treq):
    response = await treq.get("http://localhost/nonexistant")
    assert response.code == 404
