import pytest

from blog.models import Entry


@pytest.mark.django_db
class TestEntry(object):
    def test_entry(self):
        assert not Entry.objects.exists()

        e = Entry.objects.create(
            slug="the-slug",
            title="My Title",
            md="""
this is some text

more text goes in this paragraph
""")

        assert e.html == (
            "<p>this is some text</p>\n"
            "<p>more text goes in this paragraph</p>"
        )
        assert e.summary == "<p>this is some text"
        assert e.fuzzy_date == "just now"
        assert e.get_absolute_url() == "/the-slug/"
