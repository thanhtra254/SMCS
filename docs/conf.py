# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# sys.path.insert(0, os.path.abspath('.'))
import datetime
import sphinx_rtd_theme
import sys
import os

# -- Project information -----------------------------------------------------

project = 'SAS Macros for Credit Scoring'
copyright = '%s, Nguyen Thanh Tra' % str(datetime.datetime.now().year)
author = 'trant6@vpbank.com.vn'

# The full version, including alpha/beta/rc tags
release = '2020-12-12'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'recommonmark',
	'sphinx.ext.mathjax',
	'sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

CURR_PATH = os.path.abspath(os.path.dirname(__file__))
html_logo = os.path.join(CURR_PATH, 'logo', 'SMCS_Logo_Big_White.png')
html_favicon = os.path.join(CURR_PATH, 'logo', 'favicon.ico')
latex_logo = os.path.join(CURR_PATH, 'logo', 'SMCS_Logo_Small.png')

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'


html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = 'sphinx_rtd_theme'
pygments_style = 'sphinx'
latex_engine = 'xelatex'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_css_file('my_theme.css')
