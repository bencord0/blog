import pytest


@pytest.fixture
def dj_cache():
    from django.core.cache import cache
    cache.clear()
    return cache
