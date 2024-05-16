This website uses [Jekyll](https://jekyllrb.com/), a static site generator.
It uses [Liquid](https://shopify.github.io/liquid/basics/introduction/) as a template engine.

### systemd.io

Markdown files found under `docs/` are automatically published on the
[systemd.io](https://systemd.io) website using Github Pages. A minimal unit test
to ensure the formatting doesn't have errors is included in the
`meson test -C build/ github-pages` run as part of the CI.

## Prerequisites

Before running the website, make sure you have the following installed:

- Ruby: [Installation Guide](https://www.ruby-lang.org/en/documentation/installation/)
- Jekyll: [Installation Guide](https://jekyllrb.com/docs/installation/)

## Getting Started

1. Navigate to the website directory:

```
cd docs
```

2. Start the local development server:

```
jekyll serve --livereload
```

3. Open your web browser and visit `http://localhost:4000` to view the website.
