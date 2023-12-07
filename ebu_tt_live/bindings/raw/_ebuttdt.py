# ./ebu_tt_live/bindings/raw/_ebuttdt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8fcd332e0844887c1425b5057e030b6db1849387
# Generated 2023-10-04 16:45:22.901806 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace urn:ebu:tt:datatypes [xmlns:ebuttdt]

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
Namespace = pyxb.namespace.NamespaceForURI('urn:ebu:tt:datatypes', create_if_missing=True)
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


# Atomic simple type: {urn:ebu:tt:datatypes}cellResolutionType
class cellResolutionType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellResolutionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 13, 1)
    _Documentation = None
cellResolutionType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellResolutionType._CF_pattern.addPattern(pattern='[0]*[1-9][0-9]*\\s[0]*[1-9][0-9]*')
cellResolutionType._InitializeFacetMap(cellResolutionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellResolutionType', cellResolutionType)
_module_typeBindings.cellResolutionType = cellResolutionType

# Atomic simple type: {urn:ebu:tt:datatypes}frameRateMultiplierType
class frameRateMultiplierType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frameRateMultiplierType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 18, 1)
    _Documentation = None
frameRateMultiplierType._CF_pattern = pyxb.binding.facets.CF_pattern()
frameRateMultiplierType._CF_pattern.addPattern(pattern='[0]*[1-9][0-9]*\\s[0]*[1-9][0-9]*')
frameRateMultiplierType._InitializeFacetMap(frameRateMultiplierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'frameRateMultiplierType', frameRateMultiplierType)
_module_typeBindings.frameRateMultiplierType = frameRateMultiplierType

# Atomic simple type: {urn:ebu:tt:datatypes}cellExtentType
class cellExtentType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellExtentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 23, 1)
    _Documentation = None
cellExtentType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellExtentType._CF_pattern.addPattern(pattern='([+]?\\d*\\.?\\d+(c))\\s([+]?\\d*\\.?\\d+(c))')
cellExtentType._InitializeFacetMap(cellExtentType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellExtentType', cellExtentType)
_module_typeBindings.cellExtentType = cellExtentType

# Atomic simple type: {urn:ebu:tt:datatypes}percentageExtentType
class percentageExtentType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentageExtentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 28, 1)
    _Documentation = None
percentageExtentType._CF_pattern = pyxb.binding.facets.CF_pattern()
percentageExtentType._CF_pattern.addPattern(pattern='([+]?\\d*\\.?\\d+(%))\\s([+]?\\d*\\.?\\d+(%))')
percentageExtentType._InitializeFacetMap(percentageExtentType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'percentageExtentType', percentageExtentType)
_module_typeBindings.percentageExtentType = percentageExtentType

# Atomic simple type: {urn:ebu:tt:datatypes}pixelExtentType
class pixelExtentType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pixelExtentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 33, 1)
    _Documentation = None
pixelExtentType._CF_pattern = pyxb.binding.facets.CF_pattern()
pixelExtentType._CF_pattern.addPattern(pattern='([+]?\\d*\\.?\\d+(px))\\s([+]?\\d*\\.?\\d+(px))')
pixelExtentType._InitializeFacetMap(pixelExtentType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'pixelExtentType', pixelExtentType)
_module_typeBindings.pixelExtentType = pixelExtentType

# Atomic simple type: {urn:ebu:tt:datatypes}fontFamilyType
class fontFamilyType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fontFamilyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 43, 1)
    _Documentation = None
fontFamilyType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'fontFamilyType', fontFamilyType)
_module_typeBindings.fontFamilyType = fontFamilyType

# Atomic simple type: {urn:ebu:tt:datatypes}cellFontSizeType
class cellFontSizeType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellFontSizeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 46, 1)
    _Documentation = None
cellFontSizeType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellFontSizeType._CF_pattern.addPattern(pattern='([+]?\\d*\\.?\\d+(c))(\\s([+]?\\d*\\.?\\d+(c)))?')
cellFontSizeType._InitializeFacetMap(cellFontSizeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellFontSizeType', cellFontSizeType)
_module_typeBindings.cellFontSizeType = cellFontSizeType

# Atomic simple type: {urn:ebu:tt:datatypes}percentageFontSizeType
class percentageFontSizeType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentageFontSizeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 53, 1)
    _Documentation = None
percentageFontSizeType._CF_pattern = pyxb.binding.facets.CF_pattern()
percentageFontSizeType._CF_pattern.addPattern(pattern='([+]?\\d*\\.?\\d+(%))(\\s([+]?\\d*\\.?\\d+(%)))?')
percentageFontSizeType._InitializeFacetMap(percentageFontSizeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'percentageFontSizeType', percentageFontSizeType)
_module_typeBindings.percentageFontSizeType = percentageFontSizeType

# Atomic simple type: {urn:ebu:tt:datatypes}pixelFontSizeType
class pixelFontSizeType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pixelFontSizeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 60, 1)
    _Documentation = None
pixelFontSizeType._CF_pattern = pyxb.binding.facets.CF_pattern()
pixelFontSizeType._CF_pattern.addPattern(pattern='([+]?\\d*\\.?\\d+(px))(\\s([+]?\\d*\\.?\\d+(px)))?')
pixelFontSizeType._InitializeFacetMap(pixelFontSizeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'pixelFontSizeType', pixelFontSizeType)
_module_typeBindings.pixelFontSizeType = pixelFontSizeType

# Atomic simple type: {urn:ebu:tt:datatypes}fontStyleType
class fontStyleType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fontStyleType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 72, 1)
    _Documentation = None
fontStyleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=fontStyleType)
fontStyleType.normal = fontStyleType._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
fontStyleType.italic = fontStyleType._CF_enumeration.addEnumeration(unicode_value='italic', tag='italic')
fontStyleType._InitializeFacetMap(fontStyleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fontStyleType', fontStyleType)
_module_typeBindings.fontStyleType = fontStyleType

# Atomic simple type: {urn:ebu:tt:datatypes}fontWeightType
class fontWeightType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fontWeightType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 78, 1)
    _Documentation = None
fontWeightType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=fontWeightType)
fontWeightType.normal = fontWeightType._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
fontWeightType.bold = fontWeightType._CF_enumeration.addEnumeration(unicode_value='bold', tag='bold')
fontWeightType._InitializeFacetMap(fontWeightType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fontWeightType', fontWeightType)
_module_typeBindings.fontWeightType = fontWeightType

# Atomic simple type: {urn:ebu:tt:datatypes}cellLineHeightType
class cellLineHeightType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellLineHeightType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 84, 1)
    _Documentation = None
cellLineHeightType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellLineHeightType._CF_pattern.addPattern(pattern='\\d*\\.?\\d+(c)')
cellLineHeightType._InitializeFacetMap(cellLineHeightType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellLineHeightType', cellLineHeightType)
_module_typeBindings.cellLineHeightType = cellLineHeightType

# Atomic simple type: {urn:ebu:tt:datatypes}percentageLineHeightType
class percentageLineHeightType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentageLineHeightType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 89, 1)
    _Documentation = None
percentageLineHeightType._CF_pattern = pyxb.binding.facets.CF_pattern()
percentageLineHeightType._CF_pattern.addPattern(pattern='\\d*\\.?\\d+(%)')
percentageLineHeightType._InitializeFacetMap(percentageLineHeightType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'percentageLineHeightType', percentageLineHeightType)
_module_typeBindings.percentageLineHeightType = percentageLineHeightType

# Atomic simple type: {urn:ebu:tt:datatypes}pixelLineHeightType
class pixelLineHeightType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pixelLineHeightType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 94, 1)
    _Documentation = None
pixelLineHeightType._CF_pattern = pyxb.binding.facets.CF_pattern()
pixelLineHeightType._CF_pattern.addPattern(pattern='\\d*\\.?\\d+(px)')
pixelLineHeightType._InitializeFacetMap(pixelLineHeightType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'pixelLineHeightType', pixelLineHeightType)
_module_typeBindings.pixelLineHeightType = pixelLineHeightType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 101, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.normal = STD_ANON._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:ebu:tt:datatypes}cellOriginType
class cellOriginType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellOriginType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 113, 1)
    _Documentation = None
cellOriginType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellOriginType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(c))\\s([+-]?\\d*\\.?\\d+(c))')
cellOriginType._InitializeFacetMap(cellOriginType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellOriginType', cellOriginType)
_module_typeBindings.cellOriginType = cellOriginType

# Atomic simple type: {urn:ebu:tt:datatypes}percentageOriginType
class percentageOriginType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentageOriginType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 118, 1)
    _Documentation = None
percentageOriginType._CF_pattern = pyxb.binding.facets.CF_pattern()
percentageOriginType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(%))\\s([+-]?\\d*\\.?\\d+(%))')
percentageOriginType._InitializeFacetMap(percentageOriginType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'percentageOriginType', percentageOriginType)
_module_typeBindings.percentageOriginType = percentageOriginType

# Atomic simple type: {urn:ebu:tt:datatypes}pixelOriginType
class pixelOriginType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pixelOriginType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 123, 1)
    _Documentation = None
pixelOriginType._CF_pattern = pyxb.binding.facets.CF_pattern()
pixelOriginType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(px))\\s([+-]?\\d*\\.?\\d+(px))')
pixelOriginType._InitializeFacetMap(pixelOriginType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'pixelOriginType', pixelOriginType)
_module_typeBindings.pixelOriginType = pixelOriginType

# Atomic simple type: {urn:ebu:tt:datatypes}paddingType
class paddingType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paddingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 133, 1)
    _Documentation = None
paddingType._CF_pattern = pyxb.binding.facets.CF_pattern()
paddingType._CF_pattern.addPattern(pattern='([+-]?\\d*(\\.\\d+)?(px|c|%))(\\s([+-]?\\d*(\\.\\d+)?(px|c|%)))?(\\s([+-]?\\d*(\\.\\d+)?(px|c|%)))?(\\s([+-]?\\d*(\\.\\d+)?(px|c|%)))?')
paddingType._InitializeFacetMap(paddingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'paddingType', paddingType)
_module_typeBindings.paddingType = paddingType

# Atomic simple type: {urn:ebu:tt:datatypes}smpteTimingType
class smpteTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smpteTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 148, 1)
    _Documentation = None
smpteTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
smpteTimingType._CF_pattern.addPattern(pattern='([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]:[0-9][0-9]')
smpteTimingType._InitializeFacetMap(smpteTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'smpteTimingType', smpteTimingType)
_module_typeBindings.smpteTimingType = smpteTimingType

# Atomic simple type: {urn:ebu:tt:datatypes}timecountTimingType
class timecountTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timecountTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 163, 1)
    _Documentation = None
timecountTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
timecountTimingType._CF_pattern.addPattern(pattern='[0-9]+(\\.[0-9]+)?(h|ms|s|m)')
timecountTimingType._InitializeFacetMap(timecountTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'timecountTimingType', timecountTimingType)
_module_typeBindings.timecountTimingType = timecountTimingType

# Atomic simple type: {urn:ebu:tt:datatypes}authoringDelayType
class authoringDelayType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authoringDelayType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 168, 1)
    _Documentation = None
authoringDelayType._CF_pattern = pyxb.binding.facets.CF_pattern()
authoringDelayType._CF_pattern.addPattern(pattern='[+-]?[0-9]+(\\.[0-9]+)?(h|ms|s|m)')
authoringDelayType._InitializeFacetMap(authoringDelayType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'authoringDelayType', authoringDelayType)
_module_typeBindings.authoringDelayType = authoringDelayType

# Atomic simple type: {urn:ebu:tt:datatypes}limitedClockTimingType
class limitedClockTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'limitedClockTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 173, 1)
    _Documentation = None
limitedClockTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
limitedClockTimingType._CF_pattern.addPattern(pattern='[0-9][0-9]:[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?')
limitedClockTimingType._InitializeFacetMap(limitedClockTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'limitedClockTimingType', limitedClockTimingType)
_module_typeBindings.limitedClockTimingType = limitedClockTimingType

# Atomic simple type: {urn:ebu:tt:datatypes}fullClockTimingType
class fullClockTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fullClockTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 178, 1)
    _Documentation = None
fullClockTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
fullClockTimingType._CF_pattern.addPattern(pattern='[0-9][0-9]+:[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?')
fullClockTimingType._InitializeFacetMap(fullClockTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'fullClockTimingType', fullClockTimingType)
_module_typeBindings.fullClockTimingType = fullClockTimingType

# Atomic simple type: {urn:ebu:tt:datatypes}cellLengthType
class cellLengthType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellLengthType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 183, 1)
    _Documentation = None
cellLengthType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellLengthType._CF_pattern.addPattern(pattern='[+-]?\\d*\\.?\\d+(c)')
cellLengthType._InitializeFacetMap(cellLengthType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellLengthType', cellLengthType)
_module_typeBindings.cellLengthType = cellLengthType

# Atomic simple type: {urn:ebu:tt:datatypes}percentageLengthType
class percentageLengthType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentageLengthType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 188, 1)
    _Documentation = None
percentageLengthType._CF_pattern = pyxb.binding.facets.CF_pattern()
percentageLengthType._CF_pattern.addPattern(pattern='[+-]?\\d*\\.?\\d+(%)')
percentageLengthType._InitializeFacetMap(percentageLengthType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'percentageLengthType', percentageLengthType)
_module_typeBindings.percentageLengthType = percentageLengthType

# Atomic simple type: {urn:ebu:tt:datatypes}pixelLengthType
class pixelLengthType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pixelLengthType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 193, 1)
    _Documentation = None
pixelLengthType._CF_pattern = pyxb.binding.facets.CF_pattern()
pixelLengthType._CF_pattern.addPattern(pattern='[+-]?\\d*\\.?\\d+(px)')
pixelLengthType._InitializeFacetMap(pixelLengthType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'pixelLengthType', pixelLengthType)
_module_typeBindings.pixelLengthType = pixelLengthType

# Atomic simple type: {urn:ebu:tt:datatypes}rgbHexColorType
class rgbHexColorType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbHexColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 203, 1)
    _Documentation = None
rgbHexColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbHexColorType._CF_pattern.addPattern(pattern='#[a-fA-F\\d]{6}')
rgbHexColorType._InitializeFacetMap(rgbHexColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbHexColorType', rgbHexColorType)
_module_typeBindings.rgbHexColorType = rgbHexColorType

# Atomic simple type: {urn:ebu:tt:datatypes}rgbaHexColorType
class rgbaHexColorType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbaHexColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 208, 1)
    _Documentation = None
rgbaHexColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbaHexColorType._CF_pattern.addPattern(pattern='#[a-fA-F\\d]{8}')
rgbaHexColorType._InitializeFacetMap(rgbaHexColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbaHexColorType', rgbaHexColorType)
_module_typeBindings.rgbaHexColorType = rgbaHexColorType

# Atomic simple type: {urn:ebu:tt:datatypes}rgbColorType
class rgbColorType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 213, 1)
    _Documentation = None
rgbColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbColorType._CF_pattern.addPattern(pattern='rgb\\(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]),\\s?([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]),\\s?([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\\)')
rgbColorType._InitializeFacetMap(rgbColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbColorType', rgbColorType)
_module_typeBindings.rgbColorType = rgbColorType

# Atomic simple type: {urn:ebu:tt:datatypes}rgbaColorType
class rgbaColorType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbaColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 218, 1)
    _Documentation = None
rgbaColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbaColorType._CF_pattern.addPattern(pattern='rgba\\(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]),\\s?([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]),\\s?([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]),\\s?([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\\)')
rgbaColorType._InitializeFacetMap(rgbaColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbaColorType', rgbaColorType)
_module_typeBindings.rgbaColorType = rgbaColorType

# Atomic simple type: {urn:ebu:tt:datatypes}namedColorType
class namedColorType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'namedColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 223, 1)
    _Documentation = None
namedColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
namedColorType._CF_pattern.addPattern(pattern='[Tt][Rr][Aa][Nn][Ss][Pp][Aa][Rr][Ee][Nn][Tt]')
namedColorType._CF_pattern.addPattern(pattern='[Bb][Ll][Aa][Cc][Kk]')
namedColorType._CF_pattern.addPattern(pattern='[Ss][Ii][Ll][Vv][Ee][Rr]')
namedColorType._CF_pattern.addPattern(pattern='[Gg][Rr][Aa][Yy]')
namedColorType._CF_pattern.addPattern(pattern='[Ww][Hh][Ii][Tt][Ee]')
namedColorType._CF_pattern.addPattern(pattern='[Mm][Aa][Rr][Oo][Oo][Nn]')
namedColorType._CF_pattern.addPattern(pattern='[Rr][Ee][Dd]')
namedColorType._CF_pattern.addPattern(pattern='[Pp][Uu][Rr][Pp][Ll][Ee]')
namedColorType._CF_pattern.addPattern(pattern='[Ff][Uu][Cc][Hh][Ss][Ii][Aa]')
namedColorType._CF_pattern.addPattern(pattern='[Mm][Aa][Gg][Ee][Nn][Tt][Aa]')
namedColorType._CF_pattern.addPattern(pattern='[Gg][Rr][Ee][Ee][Nn]')
namedColorType._CF_pattern.addPattern(pattern='[Ll][Ii][Mm][Ee]')
namedColorType._CF_pattern.addPattern(pattern='[Oo][Ll][Ii][Vv][Ee]')
namedColorType._CF_pattern.addPattern(pattern='[Yy][Ee][Ll][Ll][Oo][Ww]')
namedColorType._CF_pattern.addPattern(pattern='[Nn][Aa][Vv][Yy]')
namedColorType._CF_pattern.addPattern(pattern='[Bb][Ll][Uu][Ee]')
namedColorType._CF_pattern.addPattern(pattern='[Tt][Ee][Aa][Ll]')
namedColorType._CF_pattern.addPattern(pattern='[Aa][Qq][Uu][Aa]')
namedColorType._CF_pattern.addPattern(pattern='[Cc][Yy][Aa][Nn]')
namedColorType._InitializeFacetMap(namedColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'namedColorType', namedColorType)
_module_typeBindings.namedColorType = namedColorType

# Atomic simple type: {urn:ebu:tt:datatypes}transitionStyleAttributeType
class transitionStyleAttributeType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transitionStyleAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 247, 1)
    _Documentation = None
transitionStyleAttributeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=transitionStyleAttributeType)
transitionStyleAttributeType.block = transitionStyleAttributeType._CF_enumeration.addEnumeration(unicode_value='block', tag='block')
transitionStyleAttributeType.line = transitionStyleAttributeType._CF_enumeration.addEnumeration(unicode_value='line', tag='line')
transitionStyleAttributeType.word = transitionStyleAttributeType._CF_enumeration.addEnumeration(unicode_value='word', tag='word')
transitionStyleAttributeType.partOfWord = transitionStyleAttributeType._CF_enumeration.addEnumeration(unicode_value='partOfWord', tag='partOfWord')
transitionStyleAttributeType.groupOfWords = transitionStyleAttributeType._CF_enumeration.addEnumeration(unicode_value='groupOfWords', tag='groupOfWords')
transitionStyleAttributeType._InitializeFacetMap(transitionStyleAttributeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'transitionStyleAttributeType', transitionStyleAttributeType)
_module_typeBindings.transitionStyleAttributeType = transitionStyleAttributeType

# Union simple type: {urn:ebu:tt:datatypes}extentType
# superclasses pyxb.binding.datatypes.anySimpleType
class extentType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of cellExtentType, percentageExtentType, pixelExtentType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 38, 1)
    _Documentation = None

    _MemberTypes = ( cellExtentType, percentageExtentType, pixelExtentType, )
extentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=extentType)
extentType._CF_pattern = pyxb.binding.facets.CF_pattern()
extentType._InitializeFacetMap(extentType._CF_enumeration,
   extentType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'extentType', extentType)
_module_typeBindings.extentType = extentType

# Union simple type: {urn:ebu:tt:datatypes}fontSizeType
# superclasses pyxb.binding.datatypes.anySimpleType
class fontSizeType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of cellFontSizeType, percentageFontSizeType, pixelFontSizeType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fontSizeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 67, 1)
    _Documentation = None

    _MemberTypes = ( cellFontSizeType, percentageFontSizeType, pixelFontSizeType, )
fontSizeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fontSizeType)
fontSizeType._CF_pattern = pyxb.binding.facets.CF_pattern()
fontSizeType._InitializeFacetMap(fontSizeType._CF_enumeration,
   fontSizeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'fontSizeType', fontSizeType)
_module_typeBindings.fontSizeType = fontSizeType

# Union simple type: {urn:ebu:tt:datatypes}lineHeightType
# superclasses pyxb.binding.datatypes.anySimpleType
class lineHeightType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of percentageLineHeightType, cellLineHeightType, pixelLineHeightType, STD_ANON."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineHeightType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 99, 1)
    _Documentation = None

    _MemberTypes = ( percentageLineHeightType, cellLineHeightType, pixelLineHeightType, STD_ANON, )
lineHeightType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lineHeightType)
lineHeightType._CF_pattern = pyxb.binding.facets.CF_pattern()
lineHeightType.normal = 'normal'                  # originally STD_ANON.normal
lineHeightType._InitializeFacetMap(lineHeightType._CF_enumeration,
   lineHeightType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'lineHeightType', lineHeightType)
_module_typeBindings.lineHeightType = lineHeightType

# Union simple type: {urn:ebu:tt:datatypes}colorType
# superclasses pyxb.binding.datatypes.anySimpleType
class colorType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of rgbHexColorType, rgbaHexColorType, rgbColorType, rgbaColorType, namedColorType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'colorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 108, 1)
    _Documentation = None

    _MemberTypes = ( rgbHexColorType, rgbaHexColorType, rgbColorType, rgbaColorType, namedColorType, )
colorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=colorType)
colorType._CF_pattern = pyxb.binding.facets.CF_pattern()
colorType._InitializeFacetMap(colorType._CF_enumeration,
   colorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'colorType', colorType)
_module_typeBindings.colorType = colorType

# Union simple type: {urn:ebu:tt:datatypes}originType
# superclasses pyxb.binding.datatypes.anySimpleType
class originType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of cellOriginType, pixelOriginType, percentageOriginType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'originType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 128, 1)
    _Documentation = None

    _MemberTypes = ( cellOriginType, pixelOriginType, percentageOriginType, )
originType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=originType)
originType._CF_pattern = pyxb.binding.facets.CF_pattern()
originType._InitializeFacetMap(originType._CF_enumeration,
   originType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'originType', originType)
_module_typeBindings.originType = originType

# Union simple type: {urn:ebu:tt:datatypes}timingType
# superclasses pyxb.binding.datatypes.anySimpleType
class timingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of smpteTimingType, timecountTimingType, fullClockTimingType, limitedClockTimingType, timecountTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 140, 1)
    _Documentation = None

    _MemberTypes = ( smpteTimingType, timecountTimingType, fullClockTimingType, limitedClockTimingType, timecountTimingType, )
timingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timingType)
timingType._CF_pattern = pyxb.binding.facets.CF_pattern()
timingType._InitializeFacetMap(timingType._CF_enumeration,
   timingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'timingType', timingType)
_module_typeBindings.timingType = timingType

# Union simple type: {urn:ebu:tt:datatypes}durationTimingType
# superclasses pyxb.binding.datatypes.anySimpleType
class durationTimingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of limitedClockTimingType, timecountTimingType, timecountTimingType, fullClockTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'durationTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 144, 1)
    _Documentation = None

    _MemberTypes = ( limitedClockTimingType, timecountTimingType, timecountTimingType, fullClockTimingType, )
durationTimingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=durationTimingType)
durationTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
durationTimingType._InitializeFacetMap(durationTimingType._CF_enumeration,
   durationTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'durationTimingType', durationTimingType)
_module_typeBindings.durationTimingType = durationTimingType

# Union simple type: {urn:ebu:tt:datatypes}startOfProgrammeTimingType
# superclasses pyxb.binding.datatypes.anySimpleType
class startOfProgrammeTimingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of limitedClockTimingType, timecountTimingType, smpteTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'startOfProgrammeTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 153, 1)
    _Documentation = None

    _MemberTypes = ( limitedClockTimingType, timecountTimingType, smpteTimingType, )
startOfProgrammeTimingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=startOfProgrammeTimingType)
startOfProgrammeTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
startOfProgrammeTimingType._InitializeFacetMap(startOfProgrammeTimingType._CF_enumeration,
   startOfProgrammeTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'startOfProgrammeTimingType', startOfProgrammeTimingType)
_module_typeBindings.startOfProgrammeTimingType = startOfProgrammeTimingType

# Union simple type: {urn:ebu:tt:datatypes}clockTimingType
# superclasses pyxb.binding.datatypes.anySimpleType
class clockTimingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of limitedClockTimingType, timecountTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'clockTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 157, 1)
    _Documentation = None

    _MemberTypes = ( limitedClockTimingType, timecountTimingType, )
clockTimingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=clockTimingType)
clockTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
clockTimingType._InitializeFacetMap(clockTimingType._CF_enumeration,
   clockTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'clockTimingType', clockTimingType)
_module_typeBindings.clockTimingType = clockTimingType

# Union simple type: {urn:ebu:tt:datatypes}mediaTimingType
# superclasses pyxb.binding.datatypes.anySimpleType
class mediaTimingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of timecountTimingType, fullClockTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 160, 1)
    _Documentation = None

    _MemberTypes = ( timecountTimingType, fullClockTimingType, )
mediaTimingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=mediaTimingType)
mediaTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
mediaTimingType._InitializeFacetMap(mediaTimingType._CF_enumeration,
   mediaTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'mediaTimingType', mediaTimingType)
_module_typeBindings.mediaTimingType = mediaTimingType

# Union simple type: {urn:ebu:tt:datatypes}lengthType
# superclasses pyxb.binding.datatypes.anySimpleType
class lengthType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of cellLengthType, percentageLengthType, pixelLengthType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 198, 1)
    _Documentation = None

    _MemberTypes = ( cellLengthType, percentageLengthType, pixelLengthType, )
lengthType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lengthType)
lengthType._CF_pattern = pyxb.binding.facets.CF_pattern()
lengthType._InitializeFacetMap(lengthType._CF_enumeration,
   lengthType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'lengthType', lengthType)
_module_typeBindings.lengthType = lengthType
