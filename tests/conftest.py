import os
import pytest


@pytest.fixture
def treq():
    from treq.testing import StubTreq
    from blog import app

    return StubTreq(app.resource())


@pytest.fixture
def db():
    import psycopg2cffi
    conn = psycopg2cffi.connect(os.getenv("DATABASE_URL", '')
    cur = conn.cursor()

    cur.execute(r"""
        CREATE TABLE IF NOT EXISTS core_entry (
            slug varchar(128) PRIMARY KEY,
            title varchar(128) NOT NULL,
            date date,
            md text
    );""")
    conn.commit()

    yield cur

    cur.execute("DROP TABLE core_entry;")

    conn.commit()
    conn.close()
