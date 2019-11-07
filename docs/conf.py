#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import inspect


def abspath(rel):
    """
    Take paths relative to the current file and
    convert them to absolute paths.

    Parameters
    ------------
    rel : str
      Relative path, IE '../stuff'

    Returns
    -------------
    abspath : str
      Absolute path, IE '/home/user/stuff'
    """

    # current working directory
    cwd = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    return os.path.abspath(os.path.join(cwd, rel))


extensions = [
    'sphinx.ext.napoleon',
    'autodocsumm',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'trimesh'
copyright = '2017, Michael Dawson-Haggerty'
author = 'Michael Dawson-Haggerty'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# grab from trimesh without installing
exec(open(abspath('../trimesh/version.py')).read())
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output --------------------------------------

# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []

# Output file base name for HTML help builder.
htmlhelp_basename = 'trimeshdoc'

# -- Extensions configuration ----------------------------------------

autodoc_default_options = {
    'autosummary': True,
}
