from blog.core import Response
from blog.utils import get_recent_entries, render_template


async def Http404(request):
    await Response(
        request,
        body=render_template('404.html.j2'),
        code=404,
    )


class IndexView:
    async def GET(self, request):
        recent_entries = get_recent_entries(10)

        body = render_template(
            'index.html.j2',
            recent_entries=recent_entries)

        await Response(request, body=body)
