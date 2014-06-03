===========
``vpython``
===========

Let's you run commands in a virtualenv, quickly. ``vpython`` does the
following:

* finds the ``requirements.txt`` file
* if a virtualenv in that directory named "env" doesn't exist:

  * create a Python virtualenv named "env"
  * ``pip install -r requirements.txt``

* Runs ``env/bin/python`` with your arguments.

For example, if you have a ``requirements.txt`` in ``~/code/project``, and
you're in ``~/code/project/tests/dir``, then running::

    vpython some_test.py

…will run ``~/code/project/env/bin/python some_test.py``; it'll create the
virtualenv if needed and if it does, ``pip install`` your requirements.txt.

``vipython`` acts similarly, but starts ``ipython``. (It'll ``pip install`` it
if needed.)

``venv`` runs arbitrary executables from the virtualenv's ``bin``, so ``venv
nosetests`` will run you're environments ``nosetests`` binary. (Since this
works on arbitrary binaries, it can't auto-install PyPI packages.)


Why?
====

I prefer to not source virtualenvs. Aside from feeling wrong, it messes up
Powerline in vim for me. It also prevents ``cd``-ing to a different env, and
forgetting to ``deactivate``.
