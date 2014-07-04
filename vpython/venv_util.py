import os as _os
from os import path as _path
import subprocess as _subprocess


class RequirementsNotFound(Exception):
    pass


def find_requirements(path=None):
    if path is None:
        path = _os.getcwd()

    while True:
        if _path.exists(_path.join(path, 'requirements.txt')):
            return path
        if path == '/':
            raise RequirementsNotFound()
        path = _path.dirname(path)


def looks_like_venv(path):
    if not _path.exists(_path.join(path, 'bin')):
        return False
    if not _path.exists(_path.join(path, 'bin', 'python')):
        return False
    return True


def exec_in_venv(venv_path, bin_name, args):
    bin_path = _path.join(venv_path, 'bin', bin_name)
    _os.execv(bin_path, [bin_path] + args)


def run_in_venv(venv_path, bin_name, args):
    bin_path = _path.join(venv_path, 'bin', bin_name)
    _subprocess.check_call([bin_path] + args)
