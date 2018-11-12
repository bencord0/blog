import pytest

from blog.schema import schema
from tests.factories.entry import EntryFactory


@pytest.mark.django_db
def test_basic():
    result = schema.execute(''' query{recentEntries{title}}''')

    assert result.data['recentEntries'] == []


@pytest.mark.django_db
def test_all_entries():
    EntryFactory.create(slug="foo")

    result = schema.execute('''
        query{
            recentEntries{
                slug
            }
        }
    ''')

    assert result.data['recentEntries'] == [
        {
            'slug': 'foo',
        },
    ]


@pytest.mark.django_db
def test_entry():
    EntryFactory.create(slug="foo")

    result = schema.execute('''
        query($slug: String!) {
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


