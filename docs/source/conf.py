# -*- coding: utf-8 -*-
#
# EnTAP documentation build configuration file, created by
# sphinx-quickstart on Fri Jun 23 12:05:06 2017.
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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme


# -- General configuration ------------------------------------------------

# extensions = ['sphinx.ext.githubpages', "sphinx_rtd_theme"]
extensions = ['sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'EnTAP'
copyright = u'2017-2020, Alex Hart, Jill Wegrzyn'
author = u'Alex Hart, Jill Wegrzyn'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.10.4'
# The full version, including alpha/beta/rc tags.
release = u'beta/0.10.4'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

#html_theme = 'sphinx_rtd_theme'
html_theme = 'default'
html_theme_options = {
    'logo_only': True,
    'prev_next_buttons_location': 'None',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
}

html_logo = 'ENTAP_white.jpg'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'EnTAPdoc'


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
    (master_doc, 'EnTAP.tex', u'EnTAP Documentation',
     u'Alex Hart, Jill Wegrzyn', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Entap', u'EnTAP Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'EnTAP', u'EnTAP Documentation',
     author, 'EnTAP', 'One line description of project.',
     'Miscellaneous'),
]

# -- Global Variables ------------------------------------------------------
rst_prolog = """
.. |ref_comp| replace:: ftp://ftp.ncbi.nlm.nih.gov/refseq/release/complete/
.. |ref_plant| replace:: ftp://ftp.ncbi.nlm.nih.gov/refseq/release/plant/
.. |ref_mamm| replace:: ftp://ftp.ncbi.nlm.nih.gov/refseq/release/vertebrate_mammalian/
.. |ref_nr| replace:: ftp://ftp.ncbi.nlm.nih.gov/blast/db/
.. |uni_swiss| replace:: ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
.. |uni_trembl| replace:: ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
.. |entap_bin_ftp| replace:: https://treegenesdb.org/FTP/EnTAP/latest/databases/entap_database.bin.gz
.. |entap_sql_ftp| replace:: https://treegenesdb.org/FTP/EnTAP/latest/databases/entap_database.db.gz
.. |eggnog_sql_ftp| replace:: http://eggnog5.embl.de/download/eggnog_4.1/eggnog-mapper-data/eggnog.db.gz
.. |eggnog_fasta_ftp| replace:: http://eggnog5.embl.de/download/eggnog_4.1/eggnog-mapper-data/eggnog4.clustered_proteins.fa.gz
.. |config_file| replace:: entap_config.ini
.. |out_dir| replace:: /entap_outfiles
.. |libs_dir| replace:: /libs
.. |entap_dir| replace:: /EnTAP
.. |src_dir| replace:: /src
.. |config_file| replace:: entap_config.ini
.. |bin_dir| replace:: /bin
.. |test_dir| replace:: /test_data
.. |data_dir| replace:: /databases
.. |tax_file| replace:: download_tax.pl
.. |graph_file| replace:: entap_graphing.py
.. |go_term| replace:: go_term.entp
.. |tax_bin| replace:: ncbi_tax_bin.entp
.. |tax_data| replace:: ncbi_tax.entp
.. |flag_path| replace:: ini
.. |flag_taxon| replace:: taxon
"""

