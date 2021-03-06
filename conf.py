# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized CoFEA document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'pysph/docs/source`.

"""
import os

from sphinx.util.pycompat import execfile_

absdir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.join(absdir, "pysph/docs/source")
execfile_(os.path.join(basedir, "conf.py"), globals())
locale_dirs = [os.path.join(basedir, "../../../locale/")]


def setup(app):
    app.srcdir = basedir
    app.confdir = app.srcdir
