# ./ebu_tt_live/bindings/raw/_tts.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a2d910a114a33d4de15f8fc406e6fadc3e499c20
# Generated 2023-10-04 16:45:22.902426 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace http://www.w3.org/ns/ttml#styling [xmlns:tts]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9bb88651-48ec-4447-927f-cd1113ebcec5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/ttml#styling', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 15, 2)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.ltr = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ltr', tag='ltr')
STD_ANON.rtl = STD_ANON._CF_enumeration.addEnumeration(unicode_value='rtl', tag='rtl')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 41, 2)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_)
STD_ANON_.left = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='left', tag='left')
STD_ANON_.center = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_.right = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
STD_ANON_.start = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='start', tag='start')
STD_ANON_.end = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='end', tag='end')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 65, 2)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_2)
STD_ANON_2.normal = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
STD_ANON_2.italic = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='italic', tag='italic')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 76, 2)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_3)
STD_ANON_3.normal = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
STD_ANON_3.bold = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='bold', tag='bold')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 87, 2)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_4)
STD_ANON_4.none = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_4.underline = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='underline', tag='underline')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 99, 2)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_5)
STD_ANON_5.normal = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
STD_ANON_5.embed = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='embed', tag='embed')
STD_ANON_5.bidiOverride = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='bidiOverride', tag='bidiOverride')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 112, 2)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_6)
STD_ANON_6.wrap = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='wrap', tag='wrap')
STD_ANON_6.noWrap = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='noWrap', tag='noWrap')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 123, 2)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_7)
STD_ANON_7.before = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='before', tag='before')
STD_ANON_7.center = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_7.after = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='after', tag='after')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 136, 2)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_8)
STD_ANON_8.lrtb = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='lrtb', tag='lrtb')
STD_ANON_8.rltb = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='rltb', tag='rltb')
STD_ANON_8.tbrl = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='tbrl', tag='tbrl')
STD_ANON_8.tblr = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='tblr', tag='tblr')
STD_ANON_8.lr = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='lr', tag='lr')
STD_ANON_8.rl = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='rl', tag='rl')
STD_ANON_8.tb = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='tb', tag='tb')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 153, 2)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_9)
STD_ANON_9.always = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='always', tag='always')
STD_ANON_9.whenActive = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='whenActive', tag='whenActive')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 165, 2)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_10)
STD_ANON_10.visible = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='visible', tag='visible')
STD_ANON_10.hidden = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='hidden', tag='hidden')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)
_module_typeBindings.STD_ANON_10 = STD_ANON_10
