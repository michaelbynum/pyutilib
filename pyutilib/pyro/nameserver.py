#  _________________________________________________________________________
#
#  PyUtilib: A Python utility library.
#  Copyright (c) 2008 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  _________________________________________________________________________

__all__ = ('start_ns', 'start_nsc')

import sys

import pyutilib.pyro
from pyutilib.pyro.util import set_maxconnections

def start_ns(max_connections=None):
    if pyutilib.pyro.Pyro is not None:
        set_maxconnections(max_connections=max_connections)
        pyutilib.pyro.Pyro.naming.main(sys.argv[1:])
    else:
        raise ImportError("Pyro or Pyro4 is not installed")

def start_nsc():
    if pyutilib.pyro.Pyro is not None:
        if pyutilib.pyro.using_pyro4:
            import Pyro4
            import Pyro4.nsc
        else:
            import Pyro
            import Pyro3.nsc
        pyutilib.pyro.Pyro.nsc.main(sys.argv[1:])
    else:
        raise ImportError("Pyro or Pyro4 is not installed")
