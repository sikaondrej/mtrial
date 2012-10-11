#!/usr/bin/python
# -*- coding: utf-8 -*-

# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

s = lambda cmd: os.system(cmd)
normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
execfile_ = lambda path, *args, **kwargs: execfile(path, dict(__file__=path))
PROJECT_ROOT = normpath(__file__, "..", "..", "..")

### START OF SCRIPT
print "> PROJECT_ROOT/_dv_djnagovoid/extensions/setup.py"

pip = normpath(PROJECT_ROOT, "env/bin/pip")
requires_ext = normpath(PROJECT_ROOT, "project/extensions/setup/requires.txt")

s("%(pip)s install -r %(requires)s"%{"pip": pip, "requires":requires_ext, })