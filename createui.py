#! /usr/bin/env python
from PyQt4 import uic
import os

ui = open(os.path.abspath(os.curdir) + "/gui.ui", "r")
pyui = open(os.path.abspath(os.curdir) + "/gui.py","w")
uic.compileUi(ui,pyui)
