from ._version import version_info, __version__

from .widgets import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-track',
        'require': 'jupyter-track/extension'
    }]
