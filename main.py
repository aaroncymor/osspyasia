import air

app = air.Air()


@app.page
def index(request: air.Request):
    return app.jinja(request, "index.html", title="PythonAsia Open Source")


@app.get("/projects/{view_type}")
def get_projects(view_type: str, request: air.Request):
    projects_data = [
        {
            "number": "01",
            "tag": "Framework",
            "tag_class": "framework",
            "name": "Air",
            "description": "A modern, lightweight web framework for Python. Built for simplicity and performance, Air provides an elegant API for building web applications quickly.",
            "meta": [("Python", "Web Framework", "Feldroy")],
            "links": [
                ("https://airwebframework.org/", "Website", "link-website"),
                ("https://github.com/feldroy/air", "GitHub", "link-github")
            ]
        },
        {
            "number": "02",
            "tag": "Generator",
            "tag_class": "generator",
            "name": "Render Engine",
            "description": "A flexible Python-based static site generator. Create beautiful, fast websites with a powerful templating system and plugin architecture.",
            "meta": [("Python", "Static Sites")],
            "links": [
                ("https://github.com/render-engine/render-engine", "GitHub", "link-github")
            ]
        },
        {
            "number": "03",
            "tag": "Tools",
            "tag_class": "tools",
            "name": "Organizer Toolkit",
            "description": "A collection of tools and resources for organizing Python community events. Built by the Python Software Foundation to help event organizers succeed.",
            "meta": [("Python", "Community", "PSF")],
            "links": [
                ("https://github.com/psf/organizer-toolkit", "GitHub", "link-github")
            ]
        },
        {
            "number": "04",
            "tag": "Community",
            "tag_class": "community",
            "name": "Cardiff",
            "description": "An open source contribution from the Filipino Python community at Z-California PH. Explore and contribute to this growing project.",
            "meta": [("Python", "Philippines")],
            "links": [
                ("https://github.com/zcalifornia-ph/cardiff", "GitHub", "link-github")
            ]
        }
    ]

    github_icon = air.Raw('<svg class="link-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>')
    website_icon = air.Raw('<svg class="link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>')

    if view_type == "list":
        projects = []
        for p in projects_data:
            meta_items = []
            for i, item in enumerate(p["meta"][0]):
                meta_items.append(air.Span(item, class_="meta-item"))
                if i < len(p["meta"][0]) - 1:
                    meta_items.append(air.Span(class_="meta-dot"))
            
            link_items = []
            for url, text, link_class in p["links"]:
                icon = github_icon if "github" in link_class else website_icon
                link_items.append(
                    air.A(
                        icon,
                        text,
                        href=url,
                        class_=f"project-link {link_class}",
                        target="_blank" if url.startswith("http") else None,
                        rel="noopener" if url.startswith("http") else None,
                    )
                )
            
            projects.append(
                air.Article(
                    air.Div(
                        air.Span(p["number"], class_="project-number"),
                        air.Span(p["tag"], class_=f"project-tag {p['tag_class']}"),
                        class_="list-header",
                    ),
                    air.Div(
                        air.H3(p["name"], class_="project-name"),
                        air.P(p["description"], class_="project-description"),
                        class_="list-content",
                    ),
                    air.Div(
                        air.Div(*meta_items, class_="project-meta"),
                        air.Div(*link_items, class_="project-links"),
                        class_="list-footer",
                    ),
                    class_="project-list-item",
                )
            )
        return air.Children(*projects)
    else:
        projects = []
        for p in projects_data:
            meta_items = []
            for i, item in enumerate(p["meta"][0]):
                meta_items.append(air.Span(item, class_="meta-item"))
                if i < len(p["meta"][0]) - 1:
                    meta_items.append(air.Span(class_="meta-dot"))
            
            link_items = []
            for url, text, link_class in p["links"]:
                icon = github_icon if "github" in link_class else website_icon
                link_items.append(
                    air.A(
                        icon,
                        text,
                        href=url,
                        class_=f"project-link {link_class}",
                        target="_blank" if url.startswith("http") else None,
                        rel="noopener" if url.startswith("http") else None,
                    )
                )
            
            projects.append(
                air.Article(
                    air.Div(
                        air.Span(p["number"], class_="project-number"),
                        air.Span(p["tag"], class_=f"project-tag {p['tag_class']}"),
                        class_="card-header",
                    ),
                    air.H3(p["name"], class_="project-name"),
                    air.P(p["description"], class_="project-description"),
                    air.Div(*meta_items, class_="project-meta"),
                    air.Div(*link_items, class_="project-links"),
                    class_="project-card",
                )
            )
        return air.Children(*projects)