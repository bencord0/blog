import asyncio

import pytest

from twisted.internet.defer import fail, succeed


# This is what a normal pytest check looks like
def test_basic():
    assert True


# Deferrds can be checked directly
def test_deferred():
    d = succeed(True)
    assert d.result


# Deferreds are awaitable
@pytest.mark.asyncio
async def test_async():
    assert await succeed(True)


# Coroutines can be used interchangably
@pytest.mark.asyncio
async def test_await():
    async def _succeed(val):
        return val

    assert await _succeed(True)


# yield from is there if you need it too
@pytest.mark.asyncio
@asyncio.coroutine
def test_yield_from():
    @asyncio.coroutine
    def _succeed(val):
        return val

    assert (yield from _succeed(True))


def test_fail():
    try:
        1 / 0
    except ZeroDivisionError as e:
        d = fail(e)

    assert isinstance(d.result.value, ZeroDivisionError)

    try:
        1 / 0
    except ZeroDivisionError as e:
        ee = e

    assert isinstance(ee, ZeroDivisionError)


@pytest.mark.asyncio
async def test_async_fail():

    def _fail():
        try:
            1 / 0
        except ZeroDivisionError as e:
            return fail(e)

    with pytest.raises(ZeroDivisionError):
        await _fail()

    async def _fail_again():
        1 / 0

    with pytest.raises(ZeroDivisionError):
        await _fail_again()
