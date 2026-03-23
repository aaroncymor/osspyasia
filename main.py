import air
from utils import PROJECTS

app = air.Air()


@app.page
def index(request: air.Request):
    return app.jinja(request, "index.html", title="PythonAsia Open Source", projects=PROJECTS)
