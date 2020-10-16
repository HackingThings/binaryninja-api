# -*- coding: utf-8 -*-
#
# Binary Ninja Documentation build configuration file, created by
# sphinx-quickstart on Tue Jun 28 23:02:45 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import platform
import inspect

if (platform.system() == "Darwin"):
	bnpath=os.path.join(os.path.abspath('.'), "..", "..", "..", "build", "out", "binaryninja.app", "Contents", "Resources", "python")
else:
	bnpath=os.path.join(os.path.abspath('.'), "..", "..", "..", "build", "out", "python")

if not os.path.exists(bnpath):
	if (platform.system() == "Darwin"):
		bnpath=os.path.join(os.path.abspath('.'), "..", "..", "..", "out", "binaryninja.app", "Contents", "Resources", "python")
	else:
		bnpath=os.path.join(os.path.abspath('.'), "..", "..", "..", "out", "python")

sys.path.insert(0, bnpath)
import binaryninja
binaryninja._init_plugins() #force license check

def setup(app):
	app.add_css_file('css/other.css')
	app.is_parallel_allowed('write')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.autosummary',
	'sphinx.ext.intersphinx',
	'sphinx.ext.viewcode',
	'breathe',
	'exhale'
]

breathe_projects = { "BinaryNinja": "./xml/" }
'''
breathe_projects_source = {
		"BinaryNinja": ("../../", ["binaryninjaapi.h", "binaryninjacore.h"])
	}
'''
breathe_default_project = "BinaryNinja"

import glob
inputfiles = glob.glob("../../*.h") + glob.glob("../../*.cpp") + glob.glob("../../ui/*.h") + glob.glob("../../ui/*.cpp")
inputfiles = ' '.join([x for x in inputfiles if not "progressindicator" in x])

exhale_args = {
	# These arguments are required
	"containmentFolder":     "./api",
	"rootFileName":          "library_root.rst",
	"rootFileTitle":         "Binary Ninja C++ API",
	"doxygenStripFromPath":  "..",
	# Suggested optional arguments
	"createTreeView":        True,
	# TIP: if using the sphinx-bootstrap-theme, you need
	# "treeViewIsBootstrap": True,
	"exhaleExecutesDoxygen": True,
	"exhaleDoxygenStdin":    f'''RECURSIVE = NO
INPUT = {inputfiles}
WARN_IF_UNDOCUMENTED = NO
'''
}


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'api/library_root'

# General information about the project.
project = u'Binary Ninja C++ API'
copyright = u'2015-2020, Vector 35 Inc'
author = u'Vector 35 Inc'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'.'.join(str(binaryninja.core_version()).split('.')[0:2])
release = str(binaryninja.core_version())

language = 'en'

exclude_patterns = []

add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
add_module_names = False


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [os.path.join(os.path.abspath("."), "..", "..", "sphinx_rtd_theme")]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
	'display_version': True,
	'style_external_links': True,
	'titles_only': True
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = u'Binary Ninja C++ API Documentation v' + version

# A shorter title for the navigation bar.  Default is the same as html_title.
#
html_short_title = u'BN C++ API'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = u'../../docs/img/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'BinaryNinjaAPIDocumentation'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
	 # The paper size ('letterpaper' or 'a4paper').
	 #
	 # 'papersize': 'letterpaper',

	 # The font size ('10pt', '11pt' or '12pt').
	 #
	 # 'pointsize': '10pt',

	 # Additional stuff for the LaTeX preamble.
	 #
	 # 'preamble': '',

	 # Latex figure (float) alignment
	 #
	 # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	(master_doc, 'BinaryNinjaAPIDocumentation.tex', u'Binary Ninja API Documentation',
	 u'Vector 35 Inc', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
	(master_doc, 'binaryninjaapi', u'Binary Ninja API Documentation',
	 [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
	(master_doc, 'BinaryNinjaAPIDocumentation', u'Binary Ninja API Documentation',
	 author, 'BinaryNinjaAPIDocumentation', 'One line description of project.',
	 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

