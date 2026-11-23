#!/usr/bin/env python3
"""Package shim delegating to root validate_machinefirst.py."""
from __future__ import annotations

import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from validate_machinefirst import *  # noqa: F401,F403
from validate_machinefirst import main

if __name__ == "__main__":
    sys.exit(main())