from collections import OrderedDict

import pytest

from blog.schema import schema

from tests.factories.entry import EntryFactory


def unorder(ordered_dict):
    if isinstance(ordered_dict, OrderedDict):
        return unorder(dict(ordered_dict))

    if isinstance(ordered_dict, dict):
        return {
            k: unorder(v)
            for k, v in ordered_dict.items()
        }

    if isinstance(ordered_dict, list):
        return [unorder(i) for i in ordered_dict]

    return ordered_dict


@pytest.mark.django_db
def test_basic():
    result = schema.execute(''' query{recentEntries{edges{node{title}}}}''')
    assert result.data['recentEntries'] == {'edges': []}


@pytest.mark.django_db
def test_all_entries():
    EntryFactory.create(slug="foo")

    result = schema.execute('''
        query{
            recentEntries{
                edges{
                    node{
                        slug
                    }
                }
            }
        }
    ''')

    assert unorder(result.data) == {
        'recentEntries': {
            'edges': [
                {
                    'node': {
                        'slug': 'foo',
                    }
                }
            ]
        }
    }


@pytest.mark.django_db
def test_entry():
    EntryFactory.create(slug="foo")

    result = schema.execute(
        '''
        query($slug: String!) {
            entry(slug: $slug) {
                slug
            }
        }
        ''',
        variables={
            'slug': 'foo',
        }
    )

    assert result.data['entry'] == {
        'slug': 'foo',
    }
