from klein import Klein

from blog.models import Entry

app = Klein()


def escape(s):
    return s.translate({
        ord('<'): '&lt;',
        ord('>'): '&gt;',
    })


@app.route("/")
def index(request):
    return b"Hello World!\n"


@app.route("/<slug>")
async def slug(request, slug):
    entry = await Entry.get(slug)
    if not entry:
        request.setResponseCode(404)
        return 'Not Found'

    return escape(f"{slug}: {entry.title}")
