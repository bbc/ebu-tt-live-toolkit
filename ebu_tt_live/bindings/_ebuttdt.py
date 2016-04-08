# ./ebu_tt_live/bindings/_ebuttdt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8fcd332e0844887c1425b5057e030b6db1849387
# Generated 2016-04-08 12:13:18.850899 by PyXB version 1.2.4 using Python 2.7.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e5be8dbd-fd7a-11e5-adc0-6c40089ad95e')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:ebu:tt:datatypes', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {urn:ebu:tt:datatypes}cellResolutionType
class cellResolutionType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cellResolutionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 9, 1)
    _Documentation = None
cellResolutionType._CF_pattern = pyxb.binding.facets.CF_pattern()
cellResolutionType._CF_pattern.addPattern(pattern='[1-9][0-9]*\\s[1-9][0-9]*')
cellResolutionType._InitializeFacetMap(cellResolutionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cellResolutionType', cellResolutionType)

# Atomic simple type: {urn:ebu:tt:datatypes}frameRateMultiplierType
class frameRateMultiplierType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frameRateMultiplierType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 14, 1)
    _Documentation = None
frameRateMultiplierType._CF_pattern = pyxb.binding.facets.CF_pattern()
frameRateMultiplierType._CF_pattern.addPattern(pattern='[1-9][0-9]*\\s[1-9][0-9]*')
frameRateMultiplierType._InitializeFacetMap(frameRateMultiplierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'frameRateMultiplierType', frameRateMultiplierType)

# Atomic simple type: {urn:ebu:tt:datatypes}extentType
class extentType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 19, 1)
    _Documentation = None
extentType._CF_pattern = pyxb.binding.facets.CF_pattern()
extentType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))')
extentType._InitializeFacetMap(extentType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'extentType', extentType)

# Atomic simple type: {urn:ebu:tt:datatypes}fontFamilyType
class fontFamilyType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fontFamilyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 24, 1)
    _Documentation = None
fontFamilyType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'fontFamilyType', fontFamilyType)

# Atomic simple type: {urn:ebu:tt:datatypes}fontSizeType
class fontSizeType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fontSizeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 27, 1)
    _Documentation = None
fontSizeType._CF_pattern = pyxb.binding.facets.CF_pattern()
fontSizeType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(px|c|%))|([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))')
fontSizeType._InitializeFacetMap(fontSizeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'fontSizeType', fontSizeType)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 36, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.normal = STD_ANON._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: {urn:ebu:tt:datatypes}originType
class originType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'originType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 48, 1)
    _Documentation = None
originType._CF_pattern = pyxb.binding.facets.CF_pattern()
originType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))')
originType._InitializeFacetMap(originType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'originType', originType)

# Atomic simple type: {urn:ebu:tt:datatypes}paddingType
class paddingType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paddingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 53, 1)
    _Documentation = None
paddingType._CF_pattern = pyxb.binding.facets.CF_pattern()
paddingType._CF_pattern.addPattern(pattern='([+-]?\\d*\\.?\\d+(px|c|%))|([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))|([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))|([+-]?\\d*\\.?\\d+(px|c|%))\\s([+-]?\\d*\\.?\\d+(px|c|%))')
paddingType._InitializeFacetMap(paddingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'paddingType', paddingType)

# Atomic simple type: {urn:ebu:tt:datatypes}smpteTimingType
class smpteTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smpteTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 64, 1)
    _Documentation = None
smpteTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
smpteTimingType._CF_pattern.addPattern(pattern='[0-2][0-9]:[0-5][0-9]:[0-5][0-9]:[0-9][0-9]')
smpteTimingType._InitializeFacetMap(smpteTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'smpteTimingType', smpteTimingType)

# Atomic simple type: {urn:ebu:tt:datatypes}clockTimingType
class clockTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'clockTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 69, 1)
    _Documentation = None
clockTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
clockTimingType._CF_pattern.addPattern(pattern='[0-2][0-9]:[0-5][0-9]:[0-5][0-9]:[0-9][0-9]')
clockTimingType._InitializeFacetMap(clockTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'clockTimingType', clockTimingType)

# Atomic simple type: {urn:ebu:tt:datatypes}timecountTimingType
class timecountTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timecountTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 77, 1)
    _Documentation = None
timecountTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
timecountTimingType._CF_pattern.addPattern(pattern='[0-9]+(\\.[0-9]+)?(h|m|s|ms)')
timecountTimingType._InitializeFacetMap(timecountTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'timecountTimingType', timecountTimingType)

# Atomic simple type: {urn:ebu:tt:datatypes}fullClockTimingType
class fullClockTimingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fullClockTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 82, 1)
    _Documentation = None
fullClockTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
fullClockTimingType._CF_pattern.addPattern(pattern='[0-9][0-9][0-9]*:[0-5][0-9]:[0-6][0-9](\\.[0-9]+)?')
fullClockTimingType._InitializeFacetMap(fullClockTimingType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'fullClockTimingType', fullClockTimingType)

# Atomic simple type: {urn:ebu:tt:datatypes}lengthType
class lengthType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 87, 1)
    _Documentation = None
lengthType._CF_pattern = pyxb.binding.facets.CF_pattern()
lengthType._CF_pattern.addPattern(pattern='[+-]?\\d*\\.?\\d+(px|c|%)')
lengthType._InitializeFacetMap(lengthType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'lengthType', lengthType)

# Atomic simple type: {urn:ebu:tt:datatypes}rgbHexColorType
class rgbHexColorType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbHexColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 92, 1)
    _Documentation = None
rgbHexColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbHexColorType._CF_pattern.addPattern(pattern='#[a-fA-F\\d]{6}')
rgbHexColorType._InitializeFacetMap(rgbHexColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbHexColorType', rgbHexColorType)

# Atomic simple type: {urn:ebu:tt:datatypes}rgbaHexColorType
class rgbaHexColorType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbaHexColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 97, 1)
    _Documentation = None
rgbaHexColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbaHexColorType._CF_pattern.addPattern(pattern='#[a-fA-F\\d]{8}')
rgbaHexColorType._InitializeFacetMap(rgbaHexColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbaHexColorType', rgbaHexColorType)

# Atomic simple type: {urn:ebu:tt:datatypes}rgbColorType
class rgbColorType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 102, 1)
    _Documentation = None
rgbColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbColorType._CF_pattern.addPattern(pattern='rgb\\(\\d\\d?\\d?,\\s?\\d\\d?\\d?,\\s?\\d\\d?\\d?\\)')
rgbColorType._InitializeFacetMap(rgbColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbColorType', rgbColorType)

# Atomic simple type: {urn:ebu:tt:datatypes}rgbaColorType
class rgbaColorType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rgbaColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 107, 1)
    _Documentation = None
rgbaColorType._CF_pattern = pyxb.binding.facets.CF_pattern()
rgbaColorType._CF_pattern.addPattern(pattern='rgba\\(\\d\\d?\\d?,\\s?\\d\\d?\\d?,\\s?\\d\\d?\\d?,\\s?\\d\\d?\\d?\\)')
rgbaColorType._InitializeFacetMap(rgbaColorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'rgbaColorType', rgbaColorType)

# Atomic simple type: {urn:ebu:tt:datatypes}namedColorType
class namedColorType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'namedColorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 112, 1)
    _Documentation = None
namedColorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=namedColorType, enum_prefix=None)
namedColorType.transparent = namedColorType._CF_enumeration.addEnumeration(unicode_value='transparent', tag='transparent')
namedColorType.black = namedColorType._CF_enumeration.addEnumeration(unicode_value='black', tag='black')
namedColorType.silver = namedColorType._CF_enumeration.addEnumeration(unicode_value='silver', tag='silver')
namedColorType.gray = namedColorType._CF_enumeration.addEnumeration(unicode_value='gray', tag='gray')
namedColorType.white = namedColorType._CF_enumeration.addEnumeration(unicode_value='white', tag='white')
namedColorType.maroon = namedColorType._CF_enumeration.addEnumeration(unicode_value='maroon', tag='maroon')
namedColorType.red = namedColorType._CF_enumeration.addEnumeration(unicode_value='red', tag='red')
namedColorType.purple = namedColorType._CF_enumeration.addEnumeration(unicode_value='purple', tag='purple')
namedColorType.fuchsia = namedColorType._CF_enumeration.addEnumeration(unicode_value='fuchsia', tag='fuchsia')
namedColorType.magenta = namedColorType._CF_enumeration.addEnumeration(unicode_value='magenta', tag='magenta')
namedColorType.green = namedColorType._CF_enumeration.addEnumeration(unicode_value='green', tag='green')
namedColorType.lime = namedColorType._CF_enumeration.addEnumeration(unicode_value='lime', tag='lime')
namedColorType.olive = namedColorType._CF_enumeration.addEnumeration(unicode_value='olive', tag='olive')
namedColorType.yellow = namedColorType._CF_enumeration.addEnumeration(unicode_value='yellow', tag='yellow')
namedColorType.navy = namedColorType._CF_enumeration.addEnumeration(unicode_value='navy', tag='navy')
namedColorType.blue = namedColorType._CF_enumeration.addEnumeration(unicode_value='blue', tag='blue')
namedColorType.teal = namedColorType._CF_enumeration.addEnumeration(unicode_value='teal', tag='teal')
namedColorType.aqua = namedColorType._CF_enumeration.addEnumeration(unicode_value='aqua', tag='aqua')
namedColorType.cyan = namedColorType._CF_enumeration.addEnumeration(unicode_value='cyan', tag='cyan')
namedColorType._InitializeFacetMap(namedColorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'namedColorType', namedColorType)

# Union simple type: {urn:ebu:tt:datatypes}lineHeightType
# superclasses pyxb.binding.datatypes.anySimpleType
class lineHeightType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of lengthType, STD_ANON."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineHeightType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 34, 1)
    _Documentation = None

    _MemberTypes = ( lengthType, STD_ANON, )
lineHeightType._CF_pattern = pyxb.binding.facets.CF_pattern()
lineHeightType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lineHeightType)
lineHeightType.normal = 'normal'                  # originally STD_ANON.normal
lineHeightType._InitializeFacetMap(lineHeightType._CF_pattern,
   lineHeightType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lineHeightType', lineHeightType)

# Union simple type: {urn:ebu:tt:datatypes}colorType
# superclasses pyxb.binding.datatypes.anySimpleType
class colorType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of rgbHexColorType, rgbaHexColorType, rgbColorType, rgbaColorType, namedColorType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'colorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 43, 1)
    _Documentation = None

    _MemberTypes = ( rgbHexColorType, rgbaHexColorType, rgbColorType, rgbaColorType, namedColorType, )
colorType._CF_pattern = pyxb.binding.facets.CF_pattern()
colorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=colorType)
colorType.transparent = 'transparent'             # originally namedColorType.transparent
colorType.black = 'black'                         # originally namedColorType.black
colorType.silver = 'silver'                       # originally namedColorType.silver
colorType.gray = 'gray'                           # originally namedColorType.gray
colorType.white = 'white'                         # originally namedColorType.white
colorType.maroon = 'maroon'                       # originally namedColorType.maroon
colorType.red = 'red'                             # originally namedColorType.red
colorType.purple = 'purple'                       # originally namedColorType.purple
colorType.fuchsia = 'fuchsia'                     # originally namedColorType.fuchsia
colorType.magenta = 'magenta'                     # originally namedColorType.magenta
colorType.green = 'green'                         # originally namedColorType.green
colorType.lime = 'lime'                           # originally namedColorType.lime
colorType.olive = 'olive'                         # originally namedColorType.olive
colorType.yellow = 'yellow'                       # originally namedColorType.yellow
colorType.navy = 'navy'                           # originally namedColorType.navy
colorType.blue = 'blue'                           # originally namedColorType.blue
colorType.teal = 'teal'                           # originally namedColorType.teal
colorType.aqua = 'aqua'                           # originally namedColorType.aqua
colorType.cyan = 'cyan'                           # originally namedColorType.cyan
colorType._InitializeFacetMap(colorType._CF_pattern,
   colorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'colorType', colorType)

# Union simple type: {urn:ebu:tt:datatypes}timingType
# superclasses pyxb.binding.datatypes.anySimpleType
class timingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of smpteTimingType, timecountTimingType, fullClockTimingType, clockTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 60, 1)
    _Documentation = None

    _MemberTypes = ( smpteTimingType, timecountTimingType, fullClockTimingType, clockTimingType, )
timingType._CF_pattern = pyxb.binding.facets.CF_pattern()
timingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timingType)
timingType._InitializeFacetMap(timingType._CF_pattern,
   timingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'timingType', timingType)

# Union simple type: {urn:ebu:tt:datatypes}mediaTimingType
# superclasses pyxb.binding.datatypes.anySimpleType
class mediaTimingType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of timecountTimingType, fullClockTimingType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_datatypes.xsd', 74, 1)
    _Documentation = None

    _MemberTypes = ( timecountTimingType, fullClockTimingType, )
mediaTimingType._CF_pattern = pyxb.binding.facets.CF_pattern()
mediaTimingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=mediaTimingType)
mediaTimingType._InitializeFacetMap(mediaTimingType._CF_pattern,
   mediaTimingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'mediaTimingType', mediaTimingType)
