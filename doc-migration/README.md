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
- `furo` (The Sphinx theme)

To install these (see [Sphinx Docs](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html#setting-up-your-project-and-development-environment)):

```sh
# Generate a Python env:
$ python3 -m venv .venv
$ source .venv/bin/activate
# Install deps
$ python3 -m pip install -U lxml
$ python3 -m pip install -U sphinx
$ python3 -m pip install -U sphinxcontrib-globalsubs
$ python3 -m pip install -U furo
$ cd doc-migration && ./convert.sh
```

## Transformation Process

You can run the entire process with `./convert.sh` in the `doc-migration` folder. The individual steps are:

### 1. Docbook to `rst`

Use the `db2rst.py` script to convert a single Docbook file to `rst`:

```sh
# in the `doc-migration` folder:
$ python3 db2rst.py ../man/busctl.xml >source/busctl.rst
```

This file parses Docbook elements, does some string transformation to the contents of each, and glues them all back together again. It will also output info on unhandled elements, so we know whether our converter is feature complete and can achieve parity with the old docs.

### 2. `rst` to Sphinx

```sh
# in the `/doc-migration` folder
$ rm -rf build
# ☝️ if you already have a build
$ make html man
```

- The `html` files end up in `/doc-migration/build/html`. Open the `index.html` there to browse the docs.
- The `man` files end up in `/doc-migration/build/man`. Preview an individual file with `$ mandoc -l build/man/busctl.1`

#### Sphinx Extensions

We use the following Sphinx extensions to achieve parity with the old docs:

##### sphinxcontrib-globalsubs

Allows referencing variables in the `global_substitutions` object in `/doc-migrations/source/conf.py` (the Sphinx config file).

## The `rst` file

### Includes

1. Versions
   In the Docbook files you may find lines like these: `<xi:include href="version-info.xml" xpointer="v205"/>` which would render into `Added in version 205` in the docs. This is now archived with the existing [sphinx directive ".. versionadded::"](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionadded) and represented as `.. versionadded:: 205` in the rst file

2. Code Snippets
These can be included with the [literalinclude directive](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude) when living in their own file.
Example:
```
.. literalinclude:: ./check-os-release-simple.py
:language: python

```

There is also the option to include a [code block](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block) directly in the rst file.
Example:
```
.. code-block:: sh

a{sv} 3 One s Eins Two u 2 Yes b true

```
3. Text Snippets

There are a few xml files were sections of these files are reused in multiple other files. While it is no problem to include a whole other rst file the concept of only including a part of that file is a bit more tricky. You can choose to include text partial that starts after a specific text and also to stop before reaching another text. So we decided it would be best to add start and stop markers to define the section in these source files. These markers are: `.. inclusion-marker-do-not-remove` / ``
So that a `<xi:include href="standard-options.xml" xpointer="no-pager" />` turns into:
```
.. include:: ./standard-options.rst
  :start-after: .. inclusion-marker-do-not-remove no-pager
  :end-before: .. inclusion-end-marker-do-not-remove no-pager
```

Files that only have content that will be included in other files and therefore should not be part of the index have the `:orphan:` tag. This will suppress warnings about this file not being in the toctree.

## Todo:

An incomplete list.

- [ ] Custom Link transformations:
  - [ ] `custom-man.xsl`
  - [x] `custom-html.xsl`
- [ ] See whether `tools/tools/xml_helper.py` does anything we don’t do, this also contains useful code for:
  - [ ] Build a man index, as in `tools/make-man-index.py`
  - [ ] Build a directives index, as in `tools/make-directive-index.py`
- [ ] See whether `tools/update-man-rules.py` does anything we don’t do
- [ ] Make sure the `man_pages` we generate for Sphinx’s `conf.py` match the Meson rules in `man/rules/meson.build`
