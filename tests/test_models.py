import pytest

from blog import settings
from blog.models import Entry


@pytest.mark.asyncio
async def test_get_nonexistant_entry(db):
    assert await Entry.get("nonexistant") is None
