# -*- coding: utf-8 -*-
"""
This module holds the EBU-TT-Live XML bindings. The package contains a raw subpackage, which the PyXB generator should
fill with the appropriate content based on the XSD provided in the package. The raw subpackage is imported and
extended/overridden by the bindings package to refine the way the bindings work. Many validation features of XML
are not available in PyXB such as assertions. PyXB does the basic validation very well but the referential semantics
are beyond its scope at the time of writing. Those validations and additional features should be covered in here.
"""

from .raw import *
from . import raw

# Let's import customizations
from . import _ebuttdt as ebuttdt
from . import _ebuttm as ebuttm
from . import _ebuttp as ebuttp
from . import _ebutts as ebutts
from . import _ttm as ttm
from . import _ttp as ttp
from . import _tts as tts

from pyxb.utils.domutils import BindingDOMSupport

namespace_prefix_map = {
    'tt': raw.Namespace,
    'ebuttdt': ebuttdt.Namespace,
    'ttp': ttp.Namespace,
    'tts': tts.Namespace,
    'ttm': ttm.Namespace,
    'ebuttm': ebuttm.Namespace,
    'ebutts': ebutts.Namespace,
    'ebuttp': ebuttp.Namespace
}


class tt_type(raw.tt_type):

    @classmethod
    def __check_bds(cls, bds):
        if bds:
            return bds
        else:
            return BindingDOMSupport(
                default_namespace=raw.Namespace,
                namespace_prefix_map=namespace_prefix_map
            )

    def toDOM(self, bds=None, parent=None, element_name=None):
        return super(tt_type, self).toDOM(
            bds=self.__check_bds(bds),
            parent=parent,
            element_name=element_name
        )

    def toxml(self, encoding=None, bds=None, root_only=False, element_name=None):
        dom = self.toDOM(self.__check_bds(bds), element_name=element_name)
        if root_only:
            dom = dom.documentElement
        return dom.toprettyxml(
            encoding=encoding,
            indent='  '
        )

raw.tt_type._SetSupersedingClass(tt_type)

# Namespace.setPrefix('tt')
# _Namespace_ttm.setPrefix('ttm')
# _Namespace_ttp.setPrefix('ttp')
# _Namespace_tts.setPrefix('tts')
# _Namespace_ebuttm.setPrefix('ebuttm')
# _Namespace_ebuttp.setPrefix('ebuttp')
# _Namespace_ebutts.setPrefix('ebutts')
