# PythonAsia Open Source Showcase

A showcase website highlighting open source projects maintained or sprinted on by Python developers across Asia. This platform celebrates the vibrant Python community in Asia and provides a space to discover and share amazing OSS projects.

## Tech Stack

Built with [Air](https://airwebframework.org/), a modern, lightweight Python web framework designed for simplicity and performance.

## Getting Started

### Prerequisites

- Python >=3.13,<3.15
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd osspyasia
```

2. Install dependencies:
```bash
uv sync
```

3. Start the development server:
```bash
air run
```

4. Visit the application:
```
http://localhost:8000
```

The development server will automatically reload when you make changes to the code.

## Project Structure

```
osspyasia/
├── main.py           # Main application file with routes and logic
├── templates/        # Jinja2 templates for server-side rendering
│   ├── base.html    # Base template with common layout
│   └── index.html   # Homepage template
├── static/          # Static assets (CSS, JavaScript, images)
│   └── css/
│       └── style.css
├── mockups/         # Design mockups and prototypes
├── pyproject.toml   # Project dependencies and configuration
└── README.md        # This file
```

### Key Files

- **`main.py`**: Contains the Air application instance, route handlers, data models, and form definitions. Includes routes for the homepage, project submission form, and dynamic project views.

- **`templates/`**: Air automatically detects this directory for Jinja2 templates. No configuration needed.

- **`static/`**: Air automatically serves static files from this directory at the `/static/` URL path.

- **`pyproject.toml`**: Defines project metadata and dependencies. The `[tool.fastapi]` section with `app = "main:app"` enables Air's auto-detection of the application instance.

## Features

- 📋 Browse open source projects in card view


## About Air Framework

Air is a modern Python web framework that emphasizes:
- **Simplicity**: Clean, intuitive API
- **Performance**: Fast and lightweight
- **Convention over Configuration**: Auto-detection of templates and static files
- **Type Safety**: Built-in support for type hints and validation

Learn more at [Air Documentation](https://docs.airwebframework.org/)

## About PythonAsia

PythonAsia is a community initiative connecting Python developers across Asia. We organize conferences, sprints, and community events to foster collaboration and knowledge sharing.

Visit us at: [https://pythonasia.org](https://pythonasia.org)

## License

[Add your license here]

## Contact

For questions or suggestions, please open an issue or reach out to the PythonAsia community.

---

Made with ❤️ by the PythonAsia community
