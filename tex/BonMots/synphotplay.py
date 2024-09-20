#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# (wg-astroconda-pdb)
# (wg-python-fix-pdbrc)
#
#
# (compile (format "python -m py_compile %s" (buffer-file-name)))
# (compile (format "pydoc3 %s" (buffer-file-name)))
#
#############################################################################
### HEREHEREHERE

import os
import optparse
import sys
import re
import numpy as np
import synphot
from astropy import units as u
from synphot import units, SourceSpectrum
from synphot.models import BlackBodyNorm1D, GaussianFlux1D
from synphot.utils import download_data
from synphot.config import conf



from astropy.io import fits


__FSDEBUG = [False,True][os.getenv('FSDEBUG') == '']

# to handle the Unicode filenames from Win1X
_encoding = 'utf-8'                         # deal with nt's UTF issues.
if(os.name == 'nt'):
    _encoding = 'utf-16'
# with io.open(listname,'r',encoding=_encoding) as f:

# (wg-python-types)
#############################################################################
#
#
#  /home/wayne/play/sasiraf/doc/BonMots/synphotplay.py
# (wg-python-emacs-help)
#
# (wg-python-toc)
#
#
#############################################################################

__doc__ = """

/home/wayne/play/sasiraf/doc/BonMots/synphotplay.py
[options] files...



"""


__author__  = 'Wayne Green'
__version__ = '0.1'
__all__     = ['','']   # list of quoted items to export



##############################################################################
#                                    Main
#                               Regression Tests
##############################################################################
# HEREHEREHERE
if __name__ == "__main__":
    opts = optparse.OptionParser(usage="%prog "+__doc__)

    opts.add_option("-v", "--verbose", action="store_true", dest="verboseflag",
                   default=False,
                   help="<bool>     be verbose about work.")

    (options, args) = opts.parse_args()



g_abs = SourceSpectrum(GaussianFlux1D, amplitude=1*u.mJy,mean=4000, stddev=20)

g_em = SourceSpectrum(GaussianFlux1D, total_flux=3.5e-13*u.erg/(u.cm**2 * u.s),
                      mean=3000, fwhm=100)

bb = SourceSpectrum(BlackBodyNorm1D, temperature=6000)
sp = 2 * bb + g_em - g_abs







    # (wg-python-atfiles)
    for filename in args:
        with open(filename,'r') if filename else sys.stdin as f:
            for l in f:
                if('#' in l):
                    continue
                parts = map(str.strip,l.split())

