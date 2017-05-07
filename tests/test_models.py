import pytest

from blog.models import Entry


@pytest.mark.asyncio
async def test_get_nonexistant_entry():
    
   assert await Entry.get("nonexistant") is None 
