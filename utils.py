from pathlib import Path
import json


def load_projects():
    projects_file = Path(__file__).parent / "projects.json"
    with open(projects_file, "r") as f:
        return json.load(f)


PROJECTS = load_projects()