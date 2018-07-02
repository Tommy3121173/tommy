# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:29:29 2018

@author: tommy_mizuki
"""

try:
    import ipywidgets
except ImportError:
    try:
        !{sys.executable} -m pip -q install ipywidgets
        import ipywidgets
    except ImportError:
        !{sys.executable} -m pip -q --user install ipywidgets
    finally:
        !jupyter nbextension enable --py widgetsnbextension
        print("You will need to refresh your browser page")        
from ipywidgets import interact