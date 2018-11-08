import pytest

from blog.schema import schema
from tests.factories.entry import EntryFactory


@pytest.mark.django_db
def test_basic():
    result = schema.execute(''' query{allEntries{title}}''')

    assert result.data['allEntries'] == []


@pytest.mark.django_db
def test_all_entries():
    EntryFactory.create(slug="foo")

    result = schema.execute('''
        query{
            allEntries{
                slug
            }
        }
    ''')

    assert result.data['allEntries'] == [
        {
            'slug': 'foo',
        },
    ]


@pytest.mark.django_db
def test_entry():
    EntryFactory.create(slug="foo")

    result = schema.execute('''
        query($slug: String) {
            entry(slug: $slug) {
                slug
            }
        }
    ''',
    variables={
        'slug': 'foo',
    })

    assert result.data['entry'] == {
        'slug': 'foo',
    }


