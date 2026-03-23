import air

app = air.Air()


@app.page
def index(request: air.Request):
    return app.jinja(request, "index.html", title="PythonAsia Open Source")
