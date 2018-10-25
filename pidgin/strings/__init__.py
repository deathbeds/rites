with __import__('importnb').Notebook():
    from . import base
    from . import _doctest
    from . import _graphviz
    from . import _matplotlib
    from . import phrases
    from . import embed
    from . import flexlist
    
modules = _doctest, _graphviz, base, _matplotlib, flexlist, embed, phrases

def load_ipython_extension(ip):
    from . import _pidgin
    for module in modules + (_pidgin,):
        getattr(module, 'load_ipython_extension', lambda x: x)(ip)

def unload_ipython_extension(ip):
    from . import _pidgin
    for module in modules + (_pidgin,):
        getattr(module, 'unload_ipython_extension', lambda x: x)(ip)