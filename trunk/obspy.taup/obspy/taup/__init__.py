# -*- coding: utf-8 -*-
"""
obspy.taup - Travel time calculation tool
=========================================
The obspy.taup package contains Python wrappers for iaspei-tau - a travel time
library by Arthur Snoke (http://www.iris.edu/pub/programs/iaspei-tau/).
The library iaspei-tau is written in Fortran and interfaced via Python ctypes.

.. seealso:: [Snoke2009]_

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    Unknown
"""

from obspy.core.util import _getVersionString


__version__ = _getVersionString("obspy.taup")


if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)
