# -*- coding: utf-8 -*-
#
# Sphinx configuration for aiida-crystal17
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import subprocess
import sys
import time

import six
import aiida_crystal17

# -- AiiDA-related setup --------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Enable rtd mode via `export READTHEDOCS=True`
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_vscode = os.environ.get('VSCODE_LOGS', None) is not None
os.environ['DJANGO_SETTINGS_MODULE'] = 'rtd_settings'

# if on_rtd or on_vscode:
if True:
    # Back-end settings for readthedocs online documentation -
    sys.path.append(os.path.split(__file__)[0])  # to find rtd_settings.py
    from aiida.manage import configuration
    configuration.IN_RT_DOC_MODE = True
    configuration.BACKEND = "django"

else:
    # import and set the theme if we're building docs locally
    try:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    except ImportError:
        # No sphinx_rtd_theme installed
        pass
    # Load the database environment by first loading the profile and then loading the backend through the manager
    from aiida.manage.configuration import get_config, load_profile
    from aiida.manage.manager import get_manager
    config = get_config()
    load_profile(config.default_profile_name)
    get_manager().get_backend()

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.6'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'ipypublish.sphinx.notebook'
]

ipysphinx_export_config = "sphinx_ipypublish_all.ext.noexec"
ipysphinx_show_prompts = True
ipysphinx_input_prompt = "In:"
ipysphinx_output_prompt = "Out:"


git_commands = ["git", "rev-parse", "HEAD"]
try:
    git_commit = subprocess.check_output(git_commands).decode("utf8").strip()
except subprocess.CalledProcessError:
    git_commit = "v{}".format(aiida_crystal17.__version__)

ipysphinx_prolog = r"""
{{% set docname = env.doc2path(env.docname, base='docs/source') %}}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This page was generated from `{{{{ docname }}}}`__,
        with configuration: ``{{{{ env.config.ipysphinx_export_config }}}}``

    __ https://github.com/chrisjsewell/aiida-crystal17/blob/{git_commit}/{{{{ docname }}}}

""".format(git_commit=git_commit)  # noqa: E501


intersphinx_mapping = {
    'python': ('https://docs.python.org/3.6', None),
    'jsonshema': ("https://python-jsonschema.readthedocs.io/en/stable/", None),
    'aiida': ('http://aiida-core.readthedocs.io/en/latest/', None),
    'aiida_quantumespresso':
    ('http://aiida-quantumespresso.readthedocs.io/en/latest/', None),
    "ase": ('https://wiki.fysik.dtu.dk/ase/', None),
    "pathlib": ('https://pathlib.readthedocs.io/en/latest/', None),
    "spglib": ('https://atztogo.github.io/spglib/', None)
}

intersphinx_aliases = {
    ('py:class', 'json.encoder.JSONEncoder'): ('py:class', 'json.JSONEncoder'),
    ('py:class', 'aiida.StructureData'):
    ('py:class', 'aiida.orm.nodes.data.structure.StructureData'),
    ('py:class', 'aiida.orm.Dict'):
    ('py:class', 'aiida.orm.nodes.data.dict.Dict'),
    ('py:class', 'aiida.orm.ArrayData'):
    ('py:class', 'aiida.orm.nodes.data.array.array.ArrayData')
}

if six.PY2:
    intersphinx_aliases[('py:class', 'callable')] = ('py:class', 'dict')
else:
    intersphinx_aliases[('py:class', 'callable')] = ('py:class', 'collections.abc.Callable')


# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# General information about the project.
project = u'aiida-crystal17'
copyright_first_year = "2018"
copyright_owners = "Chris Sewell"

current_year = str(time.localtime().tm_year)
copyright_year_string = current_year if current_year == copyright_first_year else "{}-{}".format(
    copyright_first_year, current_year)
# pylint: disable=redefined-builtin
copyright = u'{}, {}. All rights reserved'.format(copyright_year_string,
                                                  copyright_owners)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = aiida_crystal17.__version__
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['**/.ipynb_checkpoints']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# Napoleon Docstring settings
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True

# Warnings to ignore when using the -n (nitpicky) option
# We should ignore any python built-in exception, for instance
nitpick_ignore = [('py:exc', 'ArithmeticError'), ('py:exc', 'AssertionError'),
                  ('py:exc', 'AttributeError'), ('py:exc', 'BaseException'),
                  ('py:exc', 'BufferError'), ('py:exc', 'DeprecationWarning'),
                  ('py:exc', 'EOFError'), ('py:exc', 'EnvironmentError'),
                  ('py:exc', 'Exception'), ('py:exc', 'FloatingPointError'),
                  ('py:exc', 'FutureWarning'), ('py:exc', 'GeneratorExit'),
                  ('py:exc', 'IOError'), ('py:exc', 'ImportError'),
                  ('py:exc', 'ImportWarning'), ('py:exc', 'IndentationError'),
                  ('py:exc', 'IndexError'), ('py:exc', 'KeyError'),
                  ('py:exc', 'KeyboardInterrupt'), ('py:exc', 'LookupError'),
                  ('py:exc', 'MemoryError'), ('py:exc', 'NameError'),
                  ('py:exc', 'NotImplementedError'), ('py:exc', 'OSError'),
                  ('py:exc', 'OverflowError'),
                  ('py:exc', 'PendingDeprecationWarning'),
                  ('py:exc', 'ReferenceError'), ('py:exc', 'RuntimeError'),
                  ('py:exc', 'RuntimeWarning'), ('py:exc', 'StandardError'),
                  ('py:exc', 'StopIteration'), ('py:exc', 'SyntaxError'),
                  ('py:exc', 'SyntaxWarning'), ('py:exc', 'SystemError'),
                  ('py:exc', 'SystemExit'), ('py:exc', 'TabError'),
                  ('py:exc', 'TypeError'), ('py:exc', 'UnboundLocalError'),
                  ('py:exc', 'UnicodeDecodeError'),
                  ('py:exc', 'UnicodeEncodeError'), ('py:exc', 'UnicodeError'),
                  ('py:exc', 'UnicodeTranslateError'),
                  ('py:exc', 'UnicodeWarning'), ('py:exc', 'UserWarning'),
                  ('py:exc', 'VMSError'), ('py:exc', 'ValueError'),
                  ('py:exc', 'Warning'), ('py:exc', 'WindowsError'),
                  ('py:exc', 'ZeroDivisionError'),
                  ('py:class', '_abcoll.MutableMapping'),
                  ('py:class', 'tuple'),
                  ('py:obj', 'str'),
                  ('py:obj', 'list'),
                  ('py:obj', 'tuple'),
                  ('py:obj', 'int'),
                  ('py:obj', 'float'),
                  ('py:obj', 'bool'),
                  ('py:obj', 'Mapping'),
                  ('py:obj', 'MutableMapping'),
                  ]

# autodoc options, see
# http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autoclass_content = 'both'


def run_apidoc(_):
    """Runs sphinx-apidoc when building the documentation.
    Needs to be done in conf.py in order to include the APIdoc in the
    build on readthedocs.
    See also https://github.com/rtfd/readthedocs.org/issues/1139
    """
    source_dir = os.path.abspath(os.path.dirname(__file__))
    apidoc_dir = os.path.join(source_dir, 'apidoc')
    package_dir = os.path.join(
        source_dir, os.pardir, os.pardir, 'aiida_crystal17')

    # In #1139, they suggest the route below, but this ended up
    # calling sphinx-build, not sphinx-apidoc
    # from sphinx.apidoc import main
    # main([None, '-e', '-o', apidoc_dir, package_dir, '--force'])

    import subprocess
    cmd_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        cmd_path = os.path.abspath(os.path.join(
            sys.prefix, 'bin', 'sphinx-apidoc'))

    options = [
        '-o', apidoc_dir, package_dir,
        '--private',
        '--force',
        '--no-toc',
    ]

    # See https://stackoverflow.com/a/30144019
    env = os.environ.copy()
    env["SPHINX_APIDOC_OPTIONS"] = 'members,undoc-members,show-inheritance'
    subprocess.check_call([cmd_path] + options, env=env)


def add_intersphinx_aliases_to_inv(app):
    """see https://github.com/sphinx-doc/sphinx/issues/5603"""
    from sphinx.ext.intersphinx import InventoryAdapter
    inventories = InventoryAdapter(app.builder.env)

    for alias, target in app.config.intersphinx_aliases.items():
        alias_domain, alias_name = alias
        target_domain, target_name = target
        try:
            found = inventories.main_inventory[target_domain][target_name]
            try:
                inventories.main_inventory[alias_domain][alias_name] = found
            except KeyError:
                continue
        except KeyError:
            continue


def setup(app):
    app.connect('builder-inited', run_apidoc)
    app.add_config_value('intersphinx_aliases', {}, 'env')
    app.connect('builder-inited', add_intersphinx_aliases_to_inv)


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# ~ html_theme = 'basicstrap'
# SET BELOW

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# ~ html_theme_options = {
# ~ 'inner_theme': True,
# ~ 'inner_theme_name': 'bootswatch-darkly',
# ~ 'nav_fixed_top': False
# ~ }

# Add any paths that contain custom themes here, relative to this directory.
# ~ html_theme_path = ["."]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "images/.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# ~ html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = 'http://aiida-crystal17.readthedocs.io'

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# Output file base name for HTML help builder.
htmlhelp_basename = 'aiida-crystal17-doc'
