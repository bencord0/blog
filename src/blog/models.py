from contextlib import closing
from txpostgres import txpostgres

import attr

from blog import settings

@attr.s
class Entry(object):
    slug = attr.ib()
    title = attr.ib(repr=False)
    date = attr.ib(repr=False)
    md = attr.ib(repr=False)

    @classmethod
    async def get(cls, slug):
        query = r"""
            SELECT slug,title,date,md
            FROM core_entry
            WHERE slug = %(slug)s
            LIMIT 1;
        """
        
        with closing(txpostgres.Connection()) as conn:
            await conn.connect(settings.DATABASE_URL)
            queryset = await conn.runQuery(query, params={"slug": slug})

        if queryset:
            return cls(*queryset[0])
