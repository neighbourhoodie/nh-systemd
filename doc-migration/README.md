# Migration of Documentation from Docbook to Sphinx

- [Migration of Documentation from Docbook to Sphinx](#migration-of-documentation-from-docbook-to-sphinx)
  - [Prerequisites](#prerequisites)
  - [Transformation Process](#transformation-process)
    - [1. Docbook to `rst`](#1-docbook-to-rst)
    - [2. `rst` to Sphinx](#2-rst-to-sphinx)
      - [Sphinx Extensions](#sphinx-extensions)
        - [sphinxcontrib-globalsubs](#sphinxcontrib-globalsubs)
  - [Todo:](#todo)

## Prerequisites

Python dependencies for parsing docbook files and generating `rst`:

- `lxml`

Python dependencies for generating `html` and `man` pages from `rst`:
- `sphinx`
- `sphinxcontrib-globalsubs`

To install these (see [Sphinx Docs](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html#setting-up-your-project-and-development-environment)):

```sh
# Generate a Python env:
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install -U lxml
$ python3 -m pip install -U sphinx
$ python3 -m pip install -U sphinxcontrib-globalsubs
```

## Transformation Process

### 1. Docbook to `rst`

Use the `db2rst-python3.py` script to convert a single Docbook file to `rst`:

```sh
$ python3 man/db2rst-python3.py man/busctl.xml > docs/source/busctl-db2rst.rst
```

This file parses Docbook elements, does some string transformation to the contents of each, and glues them all back together again. It will also output info on unhandled elements, so we know whether our converter is feature complete and can achieve parity with the old docs.

### 2. `rst` to Sphinx

```sh
# in the `/doc-migration` folder
$ rm -rf build
# ☝️ if you already have a build
$ make html
```

The built `html` files end up in `/doc-migration/build/html`. Open the `index.html` there to browse the docs.

#### Sphinx Extensions

We use the following Sphinx extensions to achieve parity with the old docs:

##### sphinxcontrib-globalsubs

Allows referencing variables in the `global_substitutions` object in `/doc-migrations/source/conf.py` (the Sphinx config file). This is used for version information, analogous to how `<xi:includes>` worked in Docbook.

```xml
<!-- Docbook version include -->
<xi:include href="version-info.xml" xpointer="v209"/></listitem>
```

…becomes this in `rst`:

```
|v209|
```

And outputs `Added in version 209`.

## Todo:

- [ ] Custom Link transformations:
  - [ ] `custom-man.xsl`
  - [ ] `custom-html.xsl`

  Can we use [intersphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html#intersphinx) for the external links? Are they all Sphinx docs?
