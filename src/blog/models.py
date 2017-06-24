import attr

from psycopg2cffi import OperationalError

from txpostgres import txpostgres

from blog import settings


class PG(object):
    def __init__(self):
        self._conn = txpostgres.Connection()

    async def query(self, querystring, params):
        try:
            await self._conn.connect(settings.DATABASE_URL)
        except txpostgres.AlreadyConnected:
            pass
        except OperationalError:
            return []

        return await self._conn.runQuery(querystring, params=params)


pg = PG()


@attr.s
class Entry(object):
    slug = attr.ib()
    title = attr.ib(repr=False)
    date = attr.ib(repr=False)
    md = attr.ib(repr=False)

    @classmethod
    async def get(cls, slug):
        assert isinstance(slug, str)
        queryset = await pg.query(
            r"""
                SELECT slug,title,date,md
                FROM core_entry
                WHERE slug = %(slug)s
                LIMIT 1;
            """,
            {"slug": slug}
        )

        if queryset:
            return cls(*queryset[0])
