"""
adjusts module path to account for virtual namespace

This is required primarily for testing.
"""

import sys
import os


if sys.version_info[0] < 3:
    VIRTUAL_NAMESPACE = "tiddlywebplugins"

    local_package = os.path.abspath(VIRTUAL_NAMESPACE)
    sys.modules[VIRTUAL_NAMESPACE].__dict__["__path__"].insert(0, local_package)
