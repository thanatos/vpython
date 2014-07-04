from os import path as _path
import sys as _sys

from . import venv_util as _venv_util


_DEFAULT_ENV_NAMES = ('env', 'venv')


def find_venv():
    try:
        requirements_path = _venv_util.find_requirements()
    except _venv_util.RequirementsNotFound:
        _sys.stderr.write('Failed to find a "requirements.txt".\n')
        _sys.exit(1)

    names_to_try = _DEFAULT_ENV_NAMES
    for name in names_to_try:
        venv_path = _path.join(requirements_path, name)
        # If it looks like a venv…
        if _venv_util.looks_like_venv(venv_path):
            break
    else:
        _sys.stderr.write(
            'Found a requirements.txt file at "{}", but couldn\'t find a'
            ' virtual environment in that path under any of these names:'
            ' {}\n'.format(
                requirements_path, ', '.join(names_to_try),
            )
        )
        _sys.exit(1)

    return venv_path


def find_and_run(bin_name, args):
    venv_path = find_venv()
    _venv_util.exec_in_venv(venv_path, bin_name, args)
