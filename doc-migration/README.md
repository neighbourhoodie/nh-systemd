# Migration of Documentation from Docbook to Sphinx

- [Migration of Documentation from Docbook to Sphinx](#migration-of-documentation-from-docbook-to-sphinx)
  - [Prerequisites](#prerequisites)
  - [Transformation Process](#transformation-process)
    - [1. Docbook to `rst`](#1-docbook-to-rst)
    - [2. `rst` to Sphinx](#2-rst-to-sphinx)
      - [Sphinx Extensions](#sphinx-extensions)
        - [sphinxcontrib-globalsubs](#sphinxcontrib-globalsubs)
  - [Todo:](#todo)
  - [A Strategy for embedding DocBook html pages in Sphinx](#a-strategy-for-embedding-docbook-html-pages-in-sphinx)

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
$ python3 db2rst.py ../man/busctl.xml > source/busctl.rst
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

## A Strategy for embedding DocBook html pages in Sphinx

This would need to be automated:

1. Get a rendered page from DocBook and save it in `/doc-migration/source/_static`
2. Remove everything from the `jQuery` script tag to the `<hr>` tag at the end of the navi
3. Add an `rst` file with the same name as the `html` file to `/doc-migration/source`
4. Somehow figure out the manvolnum for this file and then generate these lines in that `rst`, for example for `coredumpctl(1)`, this will enable Sphinx to autolink this page from actual Sphinx pages:
  ```rst
  .. meta::
      :title: coredumpctl

  .. meta::
      :manvolnum: 1

  .. _coredumpctl(1):

  ==============
  coredumpctl(1)
  ==============

  .. raw:: html
    :file: _static/coredumpctl.html
  ```
5. Add the file(name) to the `source/index.rst`, however we end up generating this file
6. Make sure these `rst` files _are not_ used to generate `man` pages, those should still come from DocBook.
