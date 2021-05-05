# Copyright (C) 2016-2021 Ben Cordero <bencord0@condi.me>
#
# This file is part of blog.condi.me.
#
# blog.condi.me is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# blog.condi.me is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with blog.condi.me.  If not, see <http://www.gnu.org/licenses/>.

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
        variable_values={
            'slug': 'foo',
        }
    )

    assert result.data['entry'] == {
        'slug': 'foo',
    }
