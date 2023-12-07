# ./ebu_tt_live/bindings/raw/_ttp.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c65881712ea9b207722b99488f044fd57e8e6b05
# Generated 2023-10-04 16:45:22.904709 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace http://www.w3.org/ns/ttml#parameter [xmlns:ttp]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/ttml#parameter', create_if_missing=True)
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


# Atomic simple type: {http://www.w3.org/ns/ttml#parameter}timeBaseType
class timeBaseType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """The timebase defines the time coordinate system for all time
				expressions in EBU-TT."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 15, 1)
    _Documentation = 'The timebase defines the time coordinate system for all time\n\t\t\t\texpressions in EBU-TT.'
timeBaseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=timeBaseType)
timeBaseType.smpte = timeBaseType._CF_enumeration.addEnumeration(unicode_value='smpte', tag='smpte')
timeBaseType.media = timeBaseType._CF_enumeration.addEnumeration(unicode_value='media', tag='media')
timeBaseType.clock = timeBaseType._CF_enumeration.addEnumeration(unicode_value='clock', tag='clock')
timeBaseType._InitializeFacetMap(timeBaseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'timeBaseType', timeBaseType)
_module_typeBindings.timeBaseType = timeBaseType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 35, 2)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.nonDrop = STD_ANON._CF_enumeration.addEnumeration(unicode_value='nonDrop', tag='nonDrop')
STD_ANON.dropNTSC = STD_ANON._CF_enumeration.addEnumeration(unicode_value='dropNTSC', tag='dropNTSC')
STD_ANON.dropPAL = STD_ANON._CF_enumeration.addEnumeration(unicode_value='dropPAL', tag='dropPAL')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 44, 2)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_)
STD_ANON_.local = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='local', tag='local')
STD_ANON_.utc = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='utc', tag='utc')
STD_ANON_.gps = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='gps', tag='gps')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.positiveInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 57, 2)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 75, 2)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_3)
STD_ANON_3.discontinuous = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='discontinuous', tag='discontinuous')
STD_ANON_3.continuous = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='continuous', tag='continuous')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3
