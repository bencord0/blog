from klein import Klein

app = Klein()

@app.route("/")
def index(request):
    return b"Hello World!\n"
