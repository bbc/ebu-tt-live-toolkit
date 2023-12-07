# ./ebu_tt_live/bindings/raw/_ebuttm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ca3389a21c0cafded0139f24017756c1e6ca4da7
# Generated 2023-10-04 16:45:22.904511 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace urn:ebu:tt:metadata [xmlns:ebuttm]

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
import ebu_tt_live.bindings._ebuttdt as _ImportedBinding_ebu_tt_live_bindings__ebuttdt
import ebu_tt_live.bindings._ttm as _ImportedBinding_ebu_tt_live_bindings__ttm
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:ebu:tt:metadata', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ttm = _ImportedBinding_ebu_tt_live_bindings__ttm.Namespace
_Namespace_ttm.configureCategories(['typeBinding', 'elementBinding'])

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
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 29, 6)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.BASE64 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='BASE64', tag='BASE64')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 83, 5)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_)
STD_ANON_.v1_0 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='v1.0', tag='v1_0')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 147, 9)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_2)
STD_ANON_2.topBottom = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='topBottom', tag='topBottom')
STD_ANON_2.leftRight = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='leftRight', tag='leftRight')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 228, 5)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_3)
STD_ANON_3.live = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='live', tag='live')
STD_ANON_3.prepared = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='prepared', tag='prepared')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 441, 5)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_4)
STD_ANON_4.has = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='has', tag='has')
STD_ANON_4.unknown = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_4.has_not = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='has_not', tag='has_not')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 469, 5)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_5)
STD_ANON_5.all_has = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='all_has', tag='all_has')
STD_ANON_5.mixed = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='mixed', tag='mixed')
STD_ANON_5.all_has_not = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='all_has_not', tag='all_has_not')
STD_ANON_5.unspecified = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 526, 2)
    _Documentation = None
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_minLength)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Complex type {urn:ebu:tt:metadata}documentMetadata with content type ELEMENT_ONLY
class documentMetadata (pyxb.binding.basis.complexTypeDefinition):
    """EBU-TT specific metadata that applies to the whole EBU-TT
				document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentMetadata')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 65, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ebu:tt:metadata}conformsToStandard uses Python identifier conformsToStandard
    __conformsToStandard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conformsToStandard'), 'conformsToStandard', '__urnebuttmetadata_documentMetadata_urnebuttmetadataconformsToStandard', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 71, 4), )

    
    conformsToStandard = property(__conformsToStandard.value, __conformsToStandard.set, None, 'Indicates the conformance with a specific standard that is\n\t\t\t\t\t\t\tderived from TTML.')

    
    # Element {urn:ebu:tt:metadata}documentEbuttVersion uses Python identifier documentEbuttVersion
    __documentEbuttVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentEbuttVersion'), 'documentEbuttVersion', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentEbuttVersion', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 78, 4), )

    
    documentEbuttVersion = property(__documentEbuttVersion.value, __documentEbuttVersion.set, None, 'The version of the EBU-TT standard used by the document\n\t\t\t\t\t\t\tinstance.')

    
    # Element {urn:ebu:tt:metadata}documentIdentifier uses Python identifier documentIdentifier
    __documentIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentIdentifier'), 'documentIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentIdentifier', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 89, 4), )

    
    documentIdentifier = property(__documentIdentifier.value, __documentIdentifier.set, None, 'Identifier for an EBU-TT document that may be used as\n\t\t\t\t\t\t\texternal reference to an EBU-TT document.')

    
    # Element {urn:ebu:tt:metadata}documentOriginatingSystem uses Python identifier documentOriginatingSystem
    __documentOriginatingSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentOriginatingSystem'), 'documentOriginatingSystem', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentOriginatingSystem', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 95, 4), )

    
    documentOriginatingSystem = property(__documentOriginatingSystem.value, __documentOriginatingSystem.set, None, 'Software and version used to create the EBU-TT\n\t\t\t\t\t\t\tdocument.')

    
    # Element {urn:ebu:tt:metadata}documentCopyright uses Python identifier documentCopyright
    __documentCopyright = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCopyright'), 'documentCopyright', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentCopyright', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4), )

    
    documentCopyright = property(__documentCopyright.value, __documentCopyright.set, None, 'The copyright of the document.')

    
    # Element {urn:ebu:tt:metadata}documentReadingSpeed uses Python identifier documentReadingSpeed
    __documentReadingSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentReadingSpeed'), 'documentReadingSpeed', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentReadingSpeed', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 106, 4), )

    
    documentReadingSpeed = property(__documentReadingSpeed.value, __documentReadingSpeed.set, None, 'The intended reading speed for the subtitles in words per\n\t\t\t\t\t\t\tminute.')

    
    # Element {urn:ebu:tt:metadata}documentTargetAspectRatio uses Python identifier documentTargetAspectRatio
    __documentTargetAspectRatio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTargetAspectRatio'), 'documentTargetAspectRatio', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTargetAspectRatio', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 112, 4), )

    
    documentTargetAspectRatio = property(__documentTargetAspectRatio.value, __documentTargetAspectRatio.set, None, 'The aspect ratio of the video the EBU-TT document was\n\t\t\t\t\t\t\tauthored for, in width by height.')

    
    # Element {urn:ebu:tt:metadata}documentTargetActiveFormatDescriptor uses Python identifier documentTargetActiveFormatDescriptor
    __documentTargetActiveFormatDescriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTargetActiveFormatDescriptor'), 'documentTargetActiveFormatDescriptor', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTargetActiveFormatDescriptor', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 118, 4), )

    
    documentTargetActiveFormatDescriptor = property(__documentTargetActiveFormatDescriptor.value, __documentTargetActiveFormatDescriptor.set, None, 'The code for the Active Format Descriptor (AFD) that\n\t\t\t\t\t\t\tspecifies the active image in the active video (see “Definitions of\n\t\t\t\t\t\t\tterms”). The code shall be one of the AFD codes specified in SMPTE ST\n\t\t\t\t\t\t\t2016 1:2009 “Format for Active Format Description and Bar Data” Table\n\t\t\t\t\t\t\t1.')

    
    # Element {urn:ebu:tt:metadata}documentIntendedTargetBarData uses Python identifier documentIntendedTargetBarData
    __documentIntendedTargetBarData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetBarData'), 'documentIntendedTargetBarData', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentIntendedTargetBarData', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 127, 4), )

    
    documentIntendedTargetBarData = property(__documentIntendedTargetBarData.value, __documentIntendedTargetBarData.set, None, 'When an ebuttm:documentTargetActiveFormatDescriptor\n\t\t\t\t\t\t\telement is used in an EBU-TT document, an\n\t\t\t\t\t\t\tebuttm:documentIntendedTargetBarData element may be used whenever the\n\t\t\t\t\t\t\tAFD alone is insufficient to describe the extent of the image (i.e. AFD\n\t\t\t\t\t\t\tvalues 0000 and 0100). The Bar Data shall be specified in accordance\n\t\t\t\t\t\t\twith SMPTE ST 2016 1:2009 “Format for Active Format Description and Bar\n\t\t\t\t\t\t\tData” Table 3.')

    
    # Element {urn:ebu:tt:metadata}documentIntendedTargetFormat uses Python identifier documentIntendedTargetFormat
    __documentIntendedTargetFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetFormat'), 'documentIntendedTargetFormat', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentIntendedTargetFormat', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 204, 4), )

    
    documentIntendedTargetFormat = property(__documentIntendedTargetFormat.value, __documentIntendedTargetFormat.set, None, 'Indicates the subtitle format an author had in mind when\n\t\t\t\t\t\t\tauthoring an EBU-TT document or transforming another format to an EBU-TT\n\t\t\t\t\t\t\tdocument.')

    
    # Element {urn:ebu:tt:metadata}documentCreationMode uses Python identifier documentCreationMode
    __documentCreationMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCreationMode'), 'documentCreationMode', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentCreationMode', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 223, 4), )

    
    documentCreationMode = property(__documentCreationMode.value, __documentCreationMode.set, None, 'Identifies the overall workflow used to create the content\n\t\t\t\t\t\t\tin the document.')

    
    # Element {urn:ebu:tt:metadata}documentContentType uses Python identifier documentContentType
    __documentContentType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentContentType'), 'documentContentType', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentContentType', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 235, 4), )

    
    documentContentType = property(__documentContentType.value, __documentContentType.set, None, None)

    
    # Element {urn:ebu:tt:metadata}sourceMediaIdentifier uses Python identifier sourceMediaIdentifier
    __sourceMediaIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceMediaIdentifier'), 'sourceMediaIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadatasourceMediaIdentifier', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 249, 7), )

    
    sourceMediaIdentifier = property(__sourceMediaIdentifier.value, __sourceMediaIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}relatedMediaIdentifier uses Python identifier relatedMediaIdentifier
    __relatedMediaIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaIdentifier'), 'relatedMediaIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadatarelatedMediaIdentifier', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 250, 4), )

    
    relatedMediaIdentifier = property(__relatedMediaIdentifier.value, __relatedMediaIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}relatedObjectIdentifier uses Python identifier relatedObjectIdentifier
    __relatedObjectIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedObjectIdentifier'), 'relatedObjectIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadatarelatedObjectIdentifier', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4), )

    
    relatedObjectIdentifier = property(__relatedObjectIdentifier.value, __relatedObjectIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}relatedMediaDuration uses Python identifier relatedMediaDuration
    __relatedMediaDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaDuration'), 'relatedMediaDuration', '__urnebuttmetadata_documentMetadata_urnebuttmetadatarelatedMediaDuration', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 256, 4), )

    
    relatedMediaDuration = property(__relatedMediaDuration.value, __relatedMediaDuration.set, None, None)

    
    # Element {urn:ebu:tt:metadata}documentBeginDate uses Python identifier documentBeginDate
    __documentBeginDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentBeginDate'), 'documentBeginDate', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentBeginDate', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 257, 4), )

    
    documentBeginDate = property(__documentBeginDate.value, __documentBeginDate.set, None, None)

    
    # Element {urn:ebu:tt:metadata}localTimeOffset uses Python identifier localTimeOffset
    __localTimeOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'localTimeOffset'), 'localTimeOffset', '__urnebuttmetadata_documentMetadata_urnebuttmetadatalocalTimeOffset', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 258, 4), )

    
    localTimeOffset = property(__localTimeOffset.value, __localTimeOffset.set, None, None)

    
    # Element {urn:ebu:tt:metadata}referenceClockIdentifier uses Python identifier referenceClockIdentifier
    __referenceClockIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referenceClockIdentifier'), 'referenceClockIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadatareferenceClockIdentifier', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 259, 4), )

    
    referenceClockIdentifier = property(__referenceClockIdentifier.value, __referenceClockIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}broadcastServiceIdentifier uses Python identifier broadcastServiceIdentifier
    __broadcastServiceIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcastServiceIdentifier'), 'broadcastServiceIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadatabroadcastServiceIdentifier', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4), )

    
    broadcastServiceIdentifier = property(__broadcastServiceIdentifier.value, __broadcastServiceIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}documentTransitionStyle uses Python identifier documentTransitionStyle
    __documentTransitionStyle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTransitionStyle'), 'documentTransitionStyle', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTransitionStyle', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 266, 7), )

    
    documentTransitionStyle = property(__documentTransitionStyle.value, __documentTransitionStyle.set, None, None)

    
    # Element {urn:ebu:tt:metadata}documentOriginalProgrammeTitle uses Python identifier documentOriginalProgrammeTitle
    __documentOriginalProgrammeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalProgrammeTitle'), 'documentOriginalProgrammeTitle', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentOriginalProgrammeTitle', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 267, 4), )

    
    documentOriginalProgrammeTitle = property(__documentOriginalProgrammeTitle.value, __documentOriginalProgrammeTitle.set, None, 'The programme title in the original language. STL mapping:\n\t\t\t\t\t\t\tOriginal Programme Title (OPT).')

    
    # Element {urn:ebu:tt:metadata}documentOriginalEpisodeTitle uses Python identifier documentOriginalEpisodeTitle
    __documentOriginalEpisodeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalEpisodeTitle'), 'documentOriginalEpisodeTitle', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentOriginalEpisodeTitle', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 273, 4), )

    
    documentOriginalEpisodeTitle = property(__documentOriginalEpisodeTitle.value, __documentOriginalEpisodeTitle.set, None, 'The title of the episode of the programme in the original\n\t\t\t\t\t\t\tlanguage. STL mapping: Original Episode Title (OET).')

    
    # Element {urn:ebu:tt:metadata}documentTranslatedProgrammeTitle uses Python identifier documentTranslatedProgrammeTitle
    __documentTranslatedProgrammeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedProgrammeTitle'), 'documentTranslatedProgrammeTitle', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTranslatedProgrammeTitle', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 279, 4), )

    
    documentTranslatedProgrammeTitle = property(__documentTranslatedProgrammeTitle.value, __documentTranslatedProgrammeTitle.set, None, 'The programme title in the local language. STL mapping:\n\t\t\t\t\t\t\tTranslated Programme Title (TPT).')

    
    # Element {urn:ebu:tt:metadata}documentTranslatedEpisodeTitle uses Python identifier documentTranslatedEpisodeTitle
    __documentTranslatedEpisodeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedEpisodeTitle'), 'documentTranslatedEpisodeTitle', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTranslatedEpisodeTitle', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 285, 4), )

    
    documentTranslatedEpisodeTitle = property(__documentTranslatedEpisodeTitle.value, __documentTranslatedEpisodeTitle.set, None, 'The title of the episode of the programme in the local\n\t\t\t\t\t\t\tlanguage. STL mapping: Translated Episode Title\n\t\t\t\t\t\t\t(TET).')

    
    # Element {urn:ebu:tt:metadata}documentTranslatorsName uses Python identifier documentTranslatorsName
    __documentTranslatorsName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsName'), 'documentTranslatorsName', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTranslatorsName', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 292, 4), )

    
    documentTranslatorsName = property(__documentTranslatorsName.value, __documentTranslatorsName.set, None, "Name of the translator. STL mapping: Translator's Name\n\t\t\t\t\t\t\t(TN). ")

    
    # Element {urn:ebu:tt:metadata}documentTranslatorsContactDetails uses Python identifier documentTranslatorsContactDetails
    __documentTranslatorsContactDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsContactDetails'), 'documentTranslatorsContactDetails', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTranslatorsContactDetails', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 298, 4), )

    
    documentTranslatorsContactDetails = property(__documentTranslatorsContactDetails.value, __documentTranslatorsContactDetails.set, None, "The translator's contact details. STL mapping:\n\t\t\t\t\t\t\tTranslator's Contact Details (TCD).")

    
    # Element {urn:ebu:tt:metadata}documentSubtitleListReferenceCode uses Python identifier documentSubtitleListReferenceCode
    __documentSubtitleListReferenceCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentSubtitleListReferenceCode'), 'documentSubtitleListReferenceCode', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentSubtitleListReferenceCode', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 304, 4), )

    
    documentSubtitleListReferenceCode = property(__documentSubtitleListReferenceCode.value, __documentSubtitleListReferenceCode.set, None, 'Free-format character string which may be used to provide\n\t\t\t\t\t\t\tan additional reference for the subtitle list. Note: This attribute is\n\t\t\t\t\t\t\tprovided to support conversion of STL subtitle files and to retain the\n\t\t\t\t\t\t\tmetadata from the GSI block. STL mapping: Subtitle List Reference Code\n\t\t\t\t\t\t\t(SLR)')

    
    # Element {urn:ebu:tt:metadata}documentCreationDate uses Python identifier documentCreationDate
    __documentCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCreationDate'), 'documentCreationDate', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentCreationDate', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 313, 4), )

    
    documentCreationDate = property(__documentCreationDate.value, __documentCreationDate.set, None, 'The date of creation of the EBU-TT document.\n\t\t\t\t\t\t')

    
    # Element {urn:ebu:tt:metadata}documentRevisionDate uses Python identifier documentRevisionDate
    __documentRevisionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionDate'), 'documentRevisionDate', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentRevisionDate', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 319, 4), )

    
    documentRevisionDate = property(__documentRevisionDate.value, __documentRevisionDate.set, None, 'The date of the most-recent modifications to the EBU-TT\n\t\t\t\t\t\t\tdocument. ')

    
    # Element {urn:ebu:tt:metadata}documentRevisionNumber uses Python identifier documentRevisionNumber
    __documentRevisionNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionNumber'), 'documentRevisionNumber', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentRevisionNumber', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 325, 4), )

    
    documentRevisionNumber = property(__documentRevisionNumber.value, __documentRevisionNumber.set, None, 'The revision number of the EBU-TT document may be used to\n\t\t\t\t\t\t\tspecify a particular version of the subtitle list. ')

    
    # Element {urn:ebu:tt:metadata}documentTotalNumberOfSubtitles uses Python identifier documentTotalNumberOfSubtitles
    __documentTotalNumberOfSubtitles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTotalNumberOfSubtitles'), 'documentTotalNumberOfSubtitles', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentTotalNumberOfSubtitles', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 331, 4), )

    
    documentTotalNumberOfSubtitles = property(__documentTotalNumberOfSubtitles.value, __documentTotalNumberOfSubtitles.set, None, 'The number of subtitles. STL mapping: Total Number of\n\t\t\t\t\t\t\tSubtitles (TNS).')

    
    # Element {urn:ebu:tt:metadata}documentMaximumNumberOfDisplayableCharacterInAnyRow uses Python identifier documentMaximumNumberOfDisplayableCharacterInAnyRow
    __documentMaximumNumberOfDisplayableCharacterInAnyRow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentMaximumNumberOfDisplayableCharacterInAnyRow'), 'documentMaximumNumberOfDisplayableCharacterInAnyRow', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentMaximumNumberOfDisplayableCharacterInAnyRow', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 337, 4), )

    
    documentMaximumNumberOfDisplayableCharacterInAnyRow = property(__documentMaximumNumberOfDisplayableCharacterInAnyRow.value, __documentMaximumNumberOfDisplayableCharacterInAnyRow.set, None, 'Maximum number of displayable rows per television frame\n\t\t\t\t\t\t\twhich could be occupied at any one time by the subtitles defined in the\n\t\t\t\t\t\t\tTTI blocks. STL mapping: Maximum Number of Displayable Characters in any\n\t\t\t\t\t\t\ttext row (MNC). ')

    
    # Element {urn:ebu:tt:metadata}documentStartOfProgramme uses Python identifier documentStartOfProgramme
    __documentStartOfProgramme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentStartOfProgramme'), 'documentStartOfProgramme', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentStartOfProgramme', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 345, 4), )

    
    documentStartOfProgramme = property(__documentStartOfProgramme.value, __documentStartOfProgramme.set, None, 'The time code of the first frame of the recorded video\n\t\t\t\t\t\t\tsignal which is intended for transmission. Note: When the referenced\n\t\t\t\t\t\t\tstart timecode of the video material the subtitles were authored for is\n\t\t\t\t\t\t\tgreater than 00:00:00:00 (e.g. 10:00:00:00) it is recommended to specify\n\t\t\t\t\t\t\tthe attribute ebuttm:documentStartOfPrograme. STL mapping: Timecode:\n\t\t\t\t\t\t\tStart-of-Programme (TCP).')

    
    # Element {urn:ebu:tt:metadata}documentCountryOfOrigin uses Python identifier documentCountryOfOrigin
    __documentCountryOfOrigin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCountryOfOrigin'), 'documentCountryOfOrigin', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentCountryOfOrigin', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 355, 4), )

    
    documentCountryOfOrigin = property(__documentCountryOfOrigin.value, __documentCountryOfOrigin.set, None, 'The country of origin of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tCountry of Origin (CO). ')

    
    # Element {urn:ebu:tt:metadata}documentPublisher uses Python identifier documentPublisher
    __documentPublisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentPublisher'), 'documentPublisher', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentPublisher', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4), )

    
    documentPublisher = property(__documentPublisher.value, __documentPublisher.set, None, 'Name of the publisher of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tPublisher (PUB).')

    
    # Element {urn:ebu:tt:metadata}documentEditorsName uses Python identifier documentEditorsName
    __documentEditorsName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsName'), 'documentEditorsName', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentEditorsName', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4), )

    
    documentEditorsName = property(__documentEditorsName.value, __documentEditorsName.set, None, "Name of the editor of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tEditor's Name (EN).")

    
    # Element {urn:ebu:tt:metadata}documentEditorsContactDetails uses Python identifier documentEditorsContactDetails
    __documentEditorsContactDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsContactDetails'), 'documentEditorsContactDetails', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentEditorsContactDetails', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4), )

    
    documentEditorsContactDetails = property(__documentEditorsContactDetails.value, __documentEditorsContactDetails.set, None, "Information about the editor named in the metadata element\n\t\t\t\t\t\t\tdocumentEditorsName. STL mapping: Editor's Contact Details (ECD).\n\t\t\t\t\t\t")

    
    # Element {urn:ebu:tt:metadata}documentUserDefinedArea uses Python identifier documentUserDefinedArea
    __documentUserDefinedArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentUserDefinedArea'), 'documentUserDefinedArea', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentUserDefinedArea', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 380, 4), )

    
    documentUserDefinedArea = property(__documentUserDefinedArea.value, __documentUserDefinedArea.set, None, 'This field may be used to carry information about the\n\t\t\t\t\t\t\tprogramme or subtitle list, or other relevant details. STL mapping:\n\t\t\t\t\t\t\tUser-Defined Area (UDA).')

    
    # Element {urn:ebu:tt:metadata}stlCreationDate uses Python identifier stlCreationDate
    __stlCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stlCreationDate'), 'stlCreationDate', '__urnebuttmetadata_documentMetadata_urnebuttmetadatastlCreationDate', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 387, 4), )

    
    stlCreationDate = property(__stlCreationDate.value, __stlCreationDate.set, None, '')

    
    # Element {urn:ebu:tt:metadata}stlRevisionDate uses Python identifier stlRevisionDate
    __stlRevisionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionDate'), 'stlRevisionDate', '__urnebuttmetadata_documentMetadata_urnebuttmetadatastlRevisionDate', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 392, 4), )

    
    stlRevisionDate = property(__stlRevisionDate.value, __stlRevisionDate.set, None, '')

    
    # Element {urn:ebu:tt:metadata}stlRevisionNumber uses Python identifier stlRevisionNumber
    __stlRevisionNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionNumber'), 'stlRevisionNumber', '__urnebuttmetadata_documentMetadata_urnebuttmetadatastlRevisionNumber', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 397, 4), )

    
    stlRevisionNumber = property(__stlRevisionNumber.value, __stlRevisionNumber.set, None, '')

    
    # Element {urn:ebu:tt:metadata}subtitleZero uses Python identifier subtitleZero
    __subtitleZero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subtitleZero'), 'subtitleZero', '__urnebuttmetadata_documentMetadata_urnebuttmetadatasubtitleZero', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 402, 4), )

    
    subtitleZero = property(__subtitleZero.value, __subtitleZero.set, None, None)

    
    # Element {urn:ebu:tt:metadata}originalSourceServiceIdentifier uses Python identifier originalSourceServiceIdentifier
    __originalSourceServiceIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalSourceServiceIdentifier'), 'originalSourceServiceIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadataoriginalSourceServiceIdentifier', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4), )

    
    originalSourceServiceIdentifier = property(__originalSourceServiceIdentifier.value, __originalSourceServiceIdentifier.set, None, '\n\t\t\t\t\t\t\tThe ebuttm:originalSourceServiceIdentifier may be used to identify the stream of\n\t\t\t\t\t\t\taudio-visual content that was used as the source for authoring the document.\n\t\t\t\t\t\t')

    
    # Element {urn:ebu:tt:metadata}intendedDestinationServiceIdentifier uses Python identifier intendedDestinationServiceIdentifier
    __intendedDestinationServiceIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intendedDestinationServiceIdentifier'), 'intendedDestinationServiceIdentifier', '__urnebuttmetadata_documentMetadata_urnebuttmetadataintendedDestinationServiceIdentifier', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 411, 4), )

    
    intendedDestinationServiceIdentifier = property(__intendedDestinationServiceIdentifier.value, __intendedDestinationServiceIdentifier.set, None, '\n\t\t\t\t\t\t\tThe ebuttm:intendedDestinationServiceIdentifier may be used to identify the streams of destination audio-visual\n\t\t\t\t\t\t\tcontent for which the document is intended to apply.\n\t\t\t\t\t\t')

    
    # Element {urn:ebu:tt:metadata}documentFacet uses Python identifier documentFacet
    __documentFacet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentFacet'), 'documentFacet', '__urnebuttmetadata_documentMetadata_urnebuttmetadatadocumentFacet', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 419, 4), )

    
    documentFacet = property(__documentFacet.value, __documentFacet.set, None, None)

    
    # Element {urn:ebu:tt:metadata}appliedProcessing uses Python identifier appliedProcessing
    __appliedProcessing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing'), 'appliedProcessing', '__urnebuttmetadata_documentMetadata_urnebuttmetadataappliedProcessing', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 420, 4), )

    
    appliedProcessing = property(__appliedProcessing.value, __appliedProcessing.set, None, None)

    _ElementMap.update({
        __conformsToStandard.name() : __conformsToStandard,
        __documentEbuttVersion.name() : __documentEbuttVersion,
        __documentIdentifier.name() : __documentIdentifier,
        __documentOriginatingSystem.name() : __documentOriginatingSystem,
        __documentCopyright.name() : __documentCopyright,
        __documentReadingSpeed.name() : __documentReadingSpeed,
        __documentTargetAspectRatio.name() : __documentTargetAspectRatio,
        __documentTargetActiveFormatDescriptor.name() : __documentTargetActiveFormatDescriptor,
        __documentIntendedTargetBarData.name() : __documentIntendedTargetBarData,
        __documentIntendedTargetFormat.name() : __documentIntendedTargetFormat,
        __documentCreationMode.name() : __documentCreationMode,
        __documentContentType.name() : __documentContentType,
        __sourceMediaIdentifier.name() : __sourceMediaIdentifier,
        __relatedMediaIdentifier.name() : __relatedMediaIdentifier,
        __relatedObjectIdentifier.name() : __relatedObjectIdentifier,
        __relatedMediaDuration.name() : __relatedMediaDuration,
        __documentBeginDate.name() : __documentBeginDate,
        __localTimeOffset.name() : __localTimeOffset,
        __referenceClockIdentifier.name() : __referenceClockIdentifier,
        __broadcastServiceIdentifier.name() : __broadcastServiceIdentifier,
        __documentTransitionStyle.name() : __documentTransitionStyle,
        __documentOriginalProgrammeTitle.name() : __documentOriginalProgrammeTitle,
        __documentOriginalEpisodeTitle.name() : __documentOriginalEpisodeTitle,
        __documentTranslatedProgrammeTitle.name() : __documentTranslatedProgrammeTitle,
        __documentTranslatedEpisodeTitle.name() : __documentTranslatedEpisodeTitle,
        __documentTranslatorsName.name() : __documentTranslatorsName,
        __documentTranslatorsContactDetails.name() : __documentTranslatorsContactDetails,
        __documentSubtitleListReferenceCode.name() : __documentSubtitleListReferenceCode,
        __documentCreationDate.name() : __documentCreationDate,
        __documentRevisionDate.name() : __documentRevisionDate,
        __documentRevisionNumber.name() : __documentRevisionNumber,
        __documentTotalNumberOfSubtitles.name() : __documentTotalNumberOfSubtitles,
        __documentMaximumNumberOfDisplayableCharacterInAnyRow.name() : __documentMaximumNumberOfDisplayableCharacterInAnyRow,
        __documentStartOfProgramme.name() : __documentStartOfProgramme,
        __documentCountryOfOrigin.name() : __documentCountryOfOrigin,
        __documentPublisher.name() : __documentPublisher,
        __documentEditorsName.name() : __documentEditorsName,
        __documentEditorsContactDetails.name() : __documentEditorsContactDetails,
        __documentUserDefinedArea.name() : __documentUserDefinedArea,
        __stlCreationDate.name() : __stlCreationDate,
        __stlRevisionDate.name() : __stlRevisionDate,
        __stlRevisionNumber.name() : __stlRevisionNumber,
        __subtitleZero.name() : __subtitleZero,
        __originalSourceServiceIdentifier.name() : __originalSourceServiceIdentifier,
        __intendedDestinationServiceIdentifier.name() : __intendedDestinationServiceIdentifier,
        __documentFacet.name() : __documentFacet,
        __appliedProcessing.name() : __appliedProcessing
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.documentMetadata = documentMetadata
Namespace.addCategoryObject('typeBinding', 'documentMetadata', documentMetadata)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Indicates the subtitle format an author had in mind when
							authoring an EBU-TT document or transforming another format to an EBU-TT
							document."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 210, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_CTD_ANON_link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 213, 8)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 213, 8)
    
    link = property(__link.value, __link.set, None, 'Reference to a term in a classification\n\t\t\t\t\t\t\t\t\t\t\tscheme.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 236, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_CTD_ANON__link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 239, 8)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 239, 8)
    
    link = property(__link.value, __link.set, None, 'Reference to a term in a classification\n\t\t\t\t\t\t\t\t\t\t\tscheme.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 252, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnebuttmetadata_CTD_ANON_2_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 253, 6)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 253, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 261, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute serviceBegin uses Python identifier serviceBegin
    __serviceBegin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceBegin'), 'serviceBegin', '__urnebuttmetadata_CTD_ANON_3_serviceBegin', pyxb.binding.datatypes.dateTime, required=True)
    __serviceBegin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 262, 6)
    __serviceBegin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 262, 6)
    
    serviceBegin = property(__serviceBegin.value, __serviceBegin.set, None, None)

    
    # Attribute serviceEnd uses Python identifier serviceEnd
    __serviceEnd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceEnd'), 'serviceEnd', '__urnebuttmetadata_CTD_ANON_3_serviceEnd', pyxb.binding.datatypes.dateTime, required=True)
    __serviceEnd._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 263, 6)
    __serviceEnd._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 263, 6)
    
    serviceEnd = property(__serviceEnd.value, __serviceEnd.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __serviceBegin.name() : __serviceBegin,
        __serviceEnd.name() : __serviceEnd
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {urn:ebu:tt:metadata}appliedProcessing_type with content type ELEMENT_ONLY
class appliedProcessing_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}appliedProcessing_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 426, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute process uses Python identifier process
    __process = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'process'), 'process', '__urnebuttmetadata_appliedProcessing_type_process', pyxb.binding.datatypes.string, required=True)
    __process._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 430, 2)
    __process._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 430, 2)
    
    process = property(__process.value, __process.set, None, None)

    
    # Attribute generatedBy uses Python identifier generatedBy
    __generatedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generatedBy'), 'generatedBy', '__urnebuttmetadata_appliedProcessing_type_generatedBy', pyxb.binding.datatypes.anyURI, required=True)
    __generatedBy._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 431, 2)
    __generatedBy._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 431, 2)
    
    generatedBy = property(__generatedBy.value, __generatedBy.set, None, None)

    
    # Attribute sourceId uses Python identifier sourceId
    __sourceId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sourceId'), 'sourceId', '__urnebuttmetadata_appliedProcessing_type_sourceId', pyxb.binding.datatypes.anyURI)
    __sourceId._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 432, 2)
    __sourceId._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 432, 2)
    
    sourceId = property(__sourceId.value, __sourceId.set, None, None)

    
    # Attribute appliedDateTime uses Python identifier appliedDateTime
    __appliedDateTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'appliedDateTime'), 'appliedDateTime', '__urnebuttmetadata_appliedProcessing_type_appliedDateTime', pyxb.binding.datatypes.dateTime)
    __appliedDateTime._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 433, 2)
    __appliedDateTime._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 433, 2)
    
    appliedDateTime = property(__appliedDateTime.value, __appliedDateTime.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __process.name() : __process,
        __generatedBy.name() : __generatedBy,
        __sourceId.name() : __sourceId,
        __appliedDateTime.name() : __appliedDateTime
    })
_module_typeBindings.appliedProcessing_type = appliedProcessing_type
Namespace.addCategoryObject('typeBinding', 'appliedProcessing_type', appliedProcessing_type)


# Complex type {urn:ebu:tt:metadata}authoringTechnique_type with content type SIMPLE
class authoringTechnique_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}authoringTechnique_type with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 497, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_authoringTechnique_type_link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 500, 5)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 500, 5)
    
    link = property(__link.value, __link.set, None, 'Reference to a term in a classification\n\t\t\t\t\t\t\t\tscheme.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
_module_typeBindings.authoringTechnique_type = authoringTechnique_type
Namespace.addCategoryObject('typeBinding', 'authoringTechnique_type', authoringTechnique_type)


# Complex type {urn:ebu:tt:metadata}sourceMediaIdentifier_type with content type SIMPLE
class sourceMediaIdentifier_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}sourceMediaIdentifier_type with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sourceMediaIdentifier_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 533, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnebuttmetadata_sourceMediaIdentifier_type_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 536, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 536, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.sourceMediaIdentifier_type = sourceMediaIdentifier_type
Namespace.addCategoryObject('typeBinding', 'sourceMediaIdentifier_type', sourceMediaIdentifier_type)


# Complex type {urn:ebu:tt:metadata}anyMetadata_type with content type ELEMENT_ONLY
class anyMetadata_type (pyxb.binding.basis.complexTypeDefinition):
    """Container for metadata information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anyMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 550, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.anyMetadata_type = anyMetadata_type
Namespace.addCategoryObject('typeBinding', 'anyMetadata_type', anyMetadata_type)


# Complex type {urn:ebu:tt:metadata}metadataBase_type with content type ELEMENT_ONLY
class metadataBase_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}metadataBase_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'metadataBase_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 559, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml#metadata}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title'), 'title', '__urnebuttmetadata_metadataBase_type_httpwww_w3_orgnsttmlmetadatatitle', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 66, 2), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml#metadata}desc uses Python identifier desc
    __desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc'), 'desc', '__urnebuttmetadata_metadataBase_type_httpwww_w3_orgnsttmlmetadatadesc', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 67, 2), )

    
    desc = property(__desc.value, __desc.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __desc.name() : __desc
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.metadataBase_type = metadataBase_type
Namespace.addCategoryObject('typeBinding', 'metadataBase_type', metadataBase_type)


# Complex type {urn:ebu:tt:metadata}binaryData_type with content type SIMPLE
class binaryData_type (pyxb.binding.basis.complexTypeDefinition):
    """Binary data of the input formats or associated documents used to
				generate an EBU-TT document."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'binaryData_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 18, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute textEncoding uses Python identifier textEncoding
    __textEncoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'textEncoding'), 'textEncoding', '__urnebuttmetadata_binaryData_type_textEncoding', _module_typeBindings.STD_ANON, required=True)
    __textEncoding._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 25, 5)
    __textEncoding._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 25, 5)
    
    textEncoding = property(__textEncoding.value, __textEncoding.set, None, 'Text encoding of the binary data.')

    
    # Attribute binaryDataType uses Python identifier binaryDataType
    __binaryDataType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'binaryDataType'), 'binaryDataType', '__urnebuttmetadata_binaryData_type_binaryDataType', pyxb.binding.datatypes.string, required=True)
    __binaryDataType._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 35, 5)
    __binaryDataType._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 35, 5)
    
    binaryDataType = property(__binaryDataType.value, __binaryDataType.set, None, 'Internal format of the binary data.')

    
    # Attribute fileName uses Python identifier fileName
    __fileName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fileName'), 'fileName', '__urnebuttmetadata_binaryData_type_fileName', pyxb.binding.datatypes.string)
    __fileName._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 40, 5)
    __fileName._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 40, 5)
    
    fileName = property(__fileName.value, __fileName.set, None, 'A filename that may be used to identify the original\n\t\t\t\t\t\t\t\tfilename of the tunnelled binary data.')

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnebuttmetadata_binaryData_type_creationDate', pyxb.binding.datatypes.date)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 46, 5)
    __creationDate._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 46, 5)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, '')

    
    # Attribute revisionDate uses Python identifier revisionDate
    __revisionDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'revisionDate'), 'revisionDate', '__urnebuttmetadata_binaryData_type_revisionDate', pyxb.binding.datatypes.date)
    __revisionDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 51, 5)
    __revisionDate._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 51, 5)
    
    revisionDate = property(__revisionDate.value, __revisionDate.set, None, '')

    
    # Attribute revisionNumber uses Python identifier revisionNumber
    __revisionNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'revisionNumber'), 'revisionNumber', '__urnebuttmetadata_binaryData_type_revisionNumber', pyxb.binding.datatypes.nonNegativeInteger)
    __revisionNumber._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 56, 5)
    __revisionNumber._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 56, 5)
    
    revisionNumber = property(__revisionNumber.value, __revisionNumber.set, None, '')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __textEncoding.name() : __textEncoding,
        __binaryDataType.name() : __binaryDataType,
        __fileName.name() : __fileName,
        __creationDate.name() : __creationDate,
        __revisionDate.name() : __revisionDate,
        __revisionNumber.name() : __revisionNumber
    })
_module_typeBindings.binaryData_type = binaryData_type
Namespace.addCategoryObject('typeBinding', 'binaryData_type', binaryData_type)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """When an ebuttm:documentTargetActiveFormatDescriptor
							element is used in an EBU-TT document, an
							ebuttm:documentIntendedTargetBarData element may be used whenever the
							AFD alone is insufficient to describe the extent of the image (i.e. AFD
							values 0000 and 0100). The Bar Data shall be specified in accordance
							with SMPTE ST 2016 1:2009 “Format for Active Format Description and Bar
							Data” Table 3."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 137, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__urnebuttmetadata_CTD_ANON_4_position', _module_typeBindings.STD_ANON_2, required=True)
    __position._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 140, 8)
    __position._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 140, 8)
    
    position = property(__position.value, __position.set, None, 'Bar Data is defined in pairs, either top\n\t\t\t\t\t\t\t\t\t\t\tand bottom bars or left and right bars, but not both\n\t\t\t\t\t\t\t\t\t\t\tpairs at once. Bars may be unequal in size. One bar of a\n\t\t\t\t\t\t\t\t\t\t\tpair may be zero width or height.')

    
    # Attribute lineNumberEndOfTopBar uses Python identifier lineNumberEndOfTopBar
    __lineNumberEndOfTopBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lineNumberEndOfTopBar'), 'lineNumberEndOfTopBar', '__urnebuttmetadata_CTD_ANON_4_lineNumberEndOfTopBar', pyxb.binding.datatypes.nonNegativeInteger)
    __lineNumberEndOfTopBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 154, 8)
    __lineNumberEndOfTopBar._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 154, 8)
    
    lineNumberEndOfTopBar = property(__lineNumberEndOfTopBar.value, __lineNumberEndOfTopBar.set, None, 'Last line of a horizontal letter box bar\n\t\t\t\t\t\t\t\t\t\t\tarea at the top of the reconstructed frame. Designation\n\t\t\t\t\t\t\t\t\t\t\tof line numbers shall be based on the video standards\n\t\t\t\t\t\t\t\t\t\t\tand information specified in accordance with SMPTE ST\n\t\t\t\t\t\t\t\t\t\t\t2016 1:2009. All Bar Data values shall be stated in\n\t\t\t\t\t\t\t\t\t\t\tvalues appropriate to a progressive frame\n\t\t\t\t\t\t\t\t\t\t\tsystem.')

    
    # Attribute lineNumberStartOfBottomBar uses Python identifier lineNumberStartOfBottomBar
    __lineNumberStartOfBottomBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lineNumberStartOfBottomBar'), 'lineNumberStartOfBottomBar', '__urnebuttmetadata_CTD_ANON_4_lineNumberStartOfBottomBar', pyxb.binding.datatypes.nonNegativeInteger)
    __lineNumberStartOfBottomBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 166, 8)
    __lineNumberStartOfBottomBar._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 166, 8)
    
    lineNumberStartOfBottomBar = property(__lineNumberStartOfBottomBar.value, __lineNumberStartOfBottomBar.set, None, 'First line of a horizontal letter box bar\n\t\t\t\t\t\t\t\t\t\t\tarea at the bottom of the reconstructed frame.\n\t\t\t\t\t\t\t\t\t\t\tDesignation of line numbers shall be based on the video\n\t\t\t\t\t\t\t\t\t\t\tstandards and information specified in accordance with\n\t\t\t\t\t\t\t\t\t\t\tSMPTE ST 2016 1:2009. All Bar Data values shall be\n\t\t\t\t\t\t\t\t\t\t\tstated in values appropriate to a progressive frame\n\t\t\t\t\t\t\t\t\t\t\tsystem.')

    
    # Attribute pixelNumberEndOfLeftBar uses Python identifier pixelNumberEndOfLeftBar
    __pixelNumberEndOfLeftBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pixelNumberEndOfLeftBar'), 'pixelNumberEndOfLeftBar', '__urnebuttmetadata_CTD_ANON_4_pixelNumberEndOfLeftBar', pyxb.binding.datatypes.nonNegativeInteger)
    __pixelNumberEndOfLeftBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 178, 8)
    __pixelNumberEndOfLeftBar._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 178, 8)
    
    pixelNumberEndOfLeftBar = property(__pixelNumberEndOfLeftBar.value, __pixelNumberEndOfLeftBar.set, None, 'Last horizontal luminance sample of a\n\t\t\t\t\t\t\t\t\t\t\tvertical pillar box bar area at the left side of the\n\t\t\t\t\t\t\t\t\t\t\treconstructed frame. Pixels shall be numbered from zero,\n\t\t\t\t\t\t\t\t\t\t\tstarting with the leftmost pixel, based on the video\n\t\t\t\t\t\t\t\t\t\t\tstandards and information specified in accordance with\n\t\t\t\t\t\t\t\t\t\t\tSMPTE ST 2016 1:2009.')

    
    # Attribute pixelNumberStartOfRightBar uses Python identifier pixelNumberStartOfRightBar
    __pixelNumberStartOfRightBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pixelNumberStartOfRightBar'), 'pixelNumberStartOfRightBar', '__urnebuttmetadata_CTD_ANON_4_pixelNumberStartOfRightBar', pyxb.binding.datatypes.nonNegativeInteger)
    __pixelNumberStartOfRightBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 189, 8)
    __pixelNumberStartOfRightBar._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 189, 8)
    
    pixelNumberStartOfRightBar = property(__pixelNumberStartOfRightBar.value, __pixelNumberStartOfRightBar.set, None, 'First horizontal luminance sample of a\n\t\t\t\t\t\t\t\t\t\t\tvertical pillar box bar area at the right side of the\n\t\t\t\t\t\t\t\t\t\t\treconstructed frame. Pixels shall be numbered from zero,\n\t\t\t\t\t\t\t\t\t\t\tstarting with the leftmost pixel, based on the video\n\t\t\t\t\t\t\t\t\t\t\tstandards and information specified in accordance with\n\t\t\t\t\t\t\t\t\t\t\tSMPTE ST 2016 1:2009.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __position.name() : __position,
        __lineNumberEndOfTopBar.name() : __lineNumberEndOfTopBar,
        __lineNumberStartOfBottomBar.name() : __lineNumberStartOfBottomBar,
        __pixelNumberEndOfLeftBar.name() : __pixelNumberEndOfLeftBar,
        __pixelNumberStartOfRightBar.name() : __pixelNumberStartOfRightBar
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {urn:ebu:tt:metadata}facet_type with content type SIMPLE
class facet_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}facet_type with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'facet_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 436, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_facet_type_link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 439, 4)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 439, 4)
    
    link = property(__link.value, __link.set, None, None)

    
    # Attribute expresses uses Python identifier expresses
    __expresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expresses'), 'expresses', '__urnebuttmetadata_facet_type_expresses', _module_typeBindings.STD_ANON_4)
    __expresses._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 440, 4)
    __expresses._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 440, 4)
    
    expresses = property(__expresses.value, __expresses.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link,
        __expresses.name() : __expresses
    })
_module_typeBindings.facet_type = facet_type
Namespace.addCategoryObject('typeBinding', 'facet_type', facet_type)


# Complex type {urn:ebu:tt:metadata}documentFacet_type with content type SIMPLE
class documentFacet_type (pyxb.binding.basis.complexTypeDefinition):
    """
				The documentFacet element indicates a document level summary of a facet that applies to the document's content
				as defined by the facet element. The value may be the name of a term in a classification scheme,
				whose term should be identified by the link attribute. Each distinctly identified facet that is summarised
				shall have a separate documentFacet element. Empty documentFacet elements should have a link attribute.
				Documents shall NOT contain more than one documentFacet element referring to the same term,
				where the term is identified by the combination of the element contents and the value of the link attribute.
			"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentFacet_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 453, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_documentFacet_type_link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 467, 4)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 467, 4)
    
    link = property(__link.value, __link.set, None, None)

    
    # Attribute summary uses Python identifier summary
    __summary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summary'), 'summary', '__urnebuttmetadata_documentFacet_type_summary', _module_typeBindings.STD_ANON_5)
    __summary._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 468, 4)
    __summary._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 468, 4)
    
    summary = property(__summary.value, __summary.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link,
        __summary.name() : __summary
    })
_module_typeBindings.documentFacet_type = documentFacet_type
Namespace.addCategoryObject('typeBinding', 'documentFacet_type', documentFacet_type)


# Complex type {urn:ebu:tt:metadata}documentTransitionStyle_type with content type SIMPLE
class documentTransitionStyle_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}documentTransitionStyle_type with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentTransitionStyle_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 541, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute inUnit uses Python identifier inUnit
    __inUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inUnit'), 'inUnit', '__urnebuttmetadata_documentTransitionStyle_type_inUnit', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.transitionStyleAttributeType, required=True)
    __inUnit._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 544, 4)
    __inUnit._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 544, 4)
    
    inUnit = property(__inUnit.value, __inUnit.set, None, None)

    
    # Attribute outUnit uses Python identifier outUnit
    __outUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outUnit'), 'outUnit', '__urnebuttmetadata_documentTransitionStyle_type_outUnit', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.transitionStyleAttributeType, required=True)
    __outUnit._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 545, 4)
    __outUnit._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 545, 4)
    
    outUnit = property(__outUnit.value, __outUnit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __inUnit.name() : __inUnit,
        __outUnit.name() : __outUnit
    })
_module_typeBindings.documentTransitionStyle_type = documentTransitionStyle_type
Namespace.addCategoryObject('typeBinding', 'documentTransitionStyle_type', documentTransitionStyle_type)


# Complex type {urn:ebu:tt:metadata}headMetadata_type with content type ELEMENT_ONLY
class headMetadata_type (metadataBase_type):
    """Complex type {urn:ebu:tt:metadata}headMetadata_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'headMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 566, 1)
    _ElementMap = metadataBase_type._ElementMap.copy()
    _AttributeMap = metadataBase_type._AttributeMap.copy()
    # Base type is metadataBase_type
    
    # Element {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__urnebuttmetadata_headMetadata_type_httpwww_w3_orgnsttmlmetadataagent', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 15, 2), )

    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Element title ({http://www.w3.org/ns/ttml#metadata}title) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element desc ({http://www.w3.org/ns/ttml#metadata}desc) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element {urn:ebu:tt:metadata}documentMetadata uses Python identifier documentMetadata
    __documentMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentMetadata'), 'documentMetadata', '__urnebuttmetadata_headMetadata_type_urnebuttmetadatadocumentMetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 570, 5), )

    
    documentMetadata = property(__documentMetadata.value, __documentMetadata.set, None, None)

    
    # Element {urn:ebu:tt:metadata}binaryData uses Python identifier binaryData
    __binaryData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'binaryData'), 'binaryData', '__urnebuttmetadata_headMetadata_type_urnebuttmetadatabinaryData', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 577, 5), )

    
    binaryData = property(__binaryData.value, __binaryData.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __agent.name() : __agent,
        __documentMetadata.name() : __documentMetadata,
        __binaryData.name() : __binaryData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.headMetadata_type = headMetadata_type
Namespace.addCategoryObject('typeBinding', 'headMetadata_type', headMetadata_type)


# Complex type {urn:ebu:tt:metadata}bodyMetadata_type with content type ELEMENT_ONLY
class bodyMetadata_type (metadataBase_type):
    """Complex type {urn:ebu:tt:metadata}bodyMetadata_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bodyMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 584, 1)
    _ElementMap = metadataBase_type._ElementMap.copy()
    _AttributeMap = metadataBase_type._AttributeMap.copy()
    # Base type is metadataBase_type
    
    # Element title ({http://www.w3.org/ns/ttml#metadata}title) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element desc ({http://www.w3.org/ns/ttml#metadata}desc) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element {urn:ebu:tt:metadata}authoringTechnique uses Python identifier authoringTechnique
    __authoringTechnique = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), 'authoringTechnique', '__urnebuttmetadata_bodyMetadata_type_urnebuttmetadataauthoringTechnique', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 588, 8), )

    
    authoringTechnique = property(__authoringTechnique.value, __authoringTechnique.set, None, None)

    
    # Element {urn:ebu:tt:metadata}transitionStyle uses Python identifier transitionStyle
    __transitionStyle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle'), 'transitionStyle', '__urnebuttmetadata_bodyMetadata_type_urnebuttmetadatatransitionStyle', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 589, 5), )

    
    transitionStyle = property(__transitionStyle.value, __transitionStyle.set, None, None)

    
    # Element {urn:ebu:tt:metadata}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnebuttmetadata_bodyMetadata_type_urnebuttmetadatafacet', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 590, 8), )

    
    facet = property(__facet.value, __facet.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __authoringTechnique.name() : __authoringTechnique,
        __transitionStyle.name() : __transitionStyle,
        __facet.name() : __facet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.bodyMetadata_type = bodyMetadata_type
Namespace.addCategoryObject('typeBinding', 'bodyMetadata_type', bodyMetadata_type)


# Complex type {urn:ebu:tt:metadata}divMetadata_type with content type ELEMENT_ONLY
class divMetadata_type (metadataBase_type):
    """Complex type {urn:ebu:tt:metadata}divMetadata_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'divMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 597, 1)
    _ElementMap = metadataBase_type._ElementMap.copy()
    _AttributeMap = metadataBase_type._AttributeMap.copy()
    # Base type is metadataBase_type
    
    # Element title ({http://www.w3.org/ns/ttml#metadata}title) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element desc ({http://www.w3.org/ns/ttml#metadata}desc) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element {urn:ebu:tt:metadata}authoringTechnique uses Python identifier authoringTechnique
    __authoringTechnique = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), 'authoringTechnique', '__urnebuttmetadata_divMetadata_type_urnebuttmetadataauthoringTechnique', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 601, 8), )

    
    authoringTechnique = property(__authoringTechnique.value, __authoringTechnique.set, None, None)

    
    # Element {urn:ebu:tt:metadata}binaryData uses Python identifier binaryData
    __binaryData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'binaryData'), 'binaryData', '__urnebuttmetadata_divMetadata_type_urnebuttmetadatabinaryData', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 602, 5), )

    
    binaryData = property(__binaryData.value, __binaryData.set, None, None)

    
    # Element {urn:ebu:tt:metadata}transitionStyle uses Python identifier transitionStyle
    __transitionStyle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle'), 'transitionStyle', '__urnebuttmetadata_divMetadata_type_urnebuttmetadatatransitionStyle', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 603, 5), )

    
    transitionStyle = property(__transitionStyle.value, __transitionStyle.set, None, None)

    
    # Element {urn:ebu:tt:metadata}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnebuttmetadata_divMetadata_type_urnebuttmetadatafacet', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 604, 8), )

    
    facet = property(__facet.value, __facet.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __authoringTechnique.name() : __authoringTechnique,
        __binaryData.name() : __binaryData,
        __transitionStyle.name() : __transitionStyle,
        __facet.name() : __facet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.divMetadata_type = divMetadata_type
Namespace.addCategoryObject('typeBinding', 'divMetadata_type', divMetadata_type)


# Complex type {urn:ebu:tt:metadata}pMetadata_type with content type ELEMENT_ONLY
class pMetadata_type (metadataBase_type):
    """Complex type {urn:ebu:tt:metadata}pMetadata_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 611, 1)
    _ElementMap = metadataBase_type._ElementMap.copy()
    _AttributeMap = metadataBase_type._AttributeMap.copy()
    # Base type is metadataBase_type
    
    # Element title ({http://www.w3.org/ns/ttml#metadata}title) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element desc ({http://www.w3.org/ns/ttml#metadata}desc) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element {urn:ebu:tt:metadata}authoringTechnique uses Python identifier authoringTechnique
    __authoringTechnique = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), 'authoringTechnique', '__urnebuttmetadata_pMetadata_type_urnebuttmetadataauthoringTechnique', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 615, 8), )

    
    authoringTechnique = property(__authoringTechnique.value, __authoringTechnique.set, None, None)

    
    # Element {urn:ebu:tt:metadata}transitionStyle uses Python identifier transitionStyle
    __transitionStyle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle'), 'transitionStyle', '__urnebuttmetadata_pMetadata_type_urnebuttmetadatatransitionStyle', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 616, 5), )

    
    transitionStyle = property(__transitionStyle.value, __transitionStyle.set, None, None)

    
    # Element {urn:ebu:tt:metadata}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnebuttmetadata_pMetadata_type_urnebuttmetadatafacet', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 617, 8), )

    
    facet = property(__facet.value, __facet.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __authoringTechnique.name() : __authoringTechnique,
        __transitionStyle.name() : __transitionStyle,
        __facet.name() : __facet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.pMetadata_type = pMetadata_type
Namespace.addCategoryObject('typeBinding', 'pMetadata_type', pMetadata_type)


# Complex type {urn:ebu:tt:metadata}spanMetadata_type with content type ELEMENT_ONLY
class spanMetadata_type (metadataBase_type):
    """Complex type {urn:ebu:tt:metadata}spanMetadata_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spanMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 624, 1)
    _ElementMap = metadataBase_type._ElementMap.copy()
    _AttributeMap = metadataBase_type._AttributeMap.copy()
    # Base type is metadataBase_type
    
    # Element title ({http://www.w3.org/ns/ttml#metadata}title) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element desc ({http://www.w3.org/ns/ttml#metadata}desc) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element {urn:ebu:tt:metadata}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnebuttmetadata_spanMetadata_type_urnebuttmetadatafacet', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 628, 8), )

    
    facet = property(__facet.value, __facet.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __facet.name() : __facet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.spanMetadata_type = spanMetadata_type
Namespace.addCategoryObject('typeBinding', 'spanMetadata_type', spanMetadata_type)


# Complex type {urn:ebu:tt:metadata}stylingMetadata_type with content type ELEMENT_ONLY
class stylingMetadata_type (metadataBase_type):
    """Complex type {urn:ebu:tt:metadata}stylingMetadata_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stylingMetadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 635, 1)
    _ElementMap = metadataBase_type._ElementMap.copy()
    _AttributeMap = metadataBase_type._AttributeMap.copy()
    # Base type is metadataBase_type
    
    # Element title ({http://www.w3.org/ns/ttml#metadata}title) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element desc ({http://www.w3.org/ns/ttml#metadata}desc) inherited from {urn:ebu:tt:metadata}metadataBase_type
    
    # Element {urn:ebu:tt:metadata}font uses Python identifier font
    __font = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'font'), 'font', '__urnebuttmetadata_stylingMetadata_type_urnebuttmetadatafont', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 639, 8), )

    
    font = property(__font.value, __font.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __font.name() : __font
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.stylingMetadata_type = stylingMetadata_type
Namespace.addCategoryObject('typeBinding', 'stylingMetadata_type', stylingMetadata_type)


# Complex type {urn:ebu:tt:metadata}font_type with content type SIMPLE
class font_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ebu:tt:metadata}font_type with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'font_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 485, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute fontFamilyName uses Python identifier fontFamilyName
    __fontFamilyName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fontFamilyName'), 'fontFamilyName', '__urnebuttmetadata_font_type_fontFamilyName', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontFamilyType, required=True)
    __fontFamilyName._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 488, 4)
    __fontFamilyName._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 488, 4)
    
    fontFamilyName = property(__fontFamilyName.value, __fontFamilyName.set, None, None)

    
    # Attribute src uses Python identifier src
    __src = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'src'), 'src', '__urnebuttmetadata_font_type_src', pyxb.binding.datatypes.anyURI, required=True)
    __src._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 489, 4)
    __src._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 489, 4)
    
    src = property(__src.value, __src.set, None, None)

    
    # Attribute fontStyle uses Python identifier fontStyle
    __fontStyle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fontStyle'), 'fontStyle', '__urnebuttmetadata_font_type_fontStyle', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontStyleType)
    __fontStyle._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 490, 4)
    __fontStyle._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 490, 4)
    
    fontStyle = property(__fontStyle.value, __fontStyle.set, None, None)

    
    # Attribute fontWeight uses Python identifier fontWeight
    __fontWeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fontWeight'), 'fontWeight', '__urnebuttmetadata_font_type_fontWeight', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontWeightType)
    __fontWeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 491, 4)
    __fontWeight._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 491, 4)
    
    fontWeight = property(__fontWeight.value, __fontWeight.set, None, None)

    
    # Attribute fontSize uses Python identifier fontSize
    __fontSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fontSize'), 'fontSize', '__urnebuttmetadata_font_type_fontSize', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontSizeType)
    __fontSize._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 492, 4)
    __fontSize._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 492, 4)
    
    fontSize = property(__fontSize.value, __fontSize.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fontFamilyName.name() : __fontFamilyName,
        __src.name() : __src,
        __fontStyle.name() : __fontStyle,
        __fontWeight.name() : __fontWeight,
        __fontSize.name() : __fontSize
    })
_module_typeBindings.font_type = font_type
Namespace.addCategoryObject('typeBinding', 'font_type', font_type)




documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conformsToStandard'), pyxb.binding.datatypes.anyURI, scope=documentMetadata, documentation='Indicates the conformance with a specific standard that is\n\t\t\t\t\t\t\tderived from TTML.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 71, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentEbuttVersion'), STD_ANON_, scope=documentMetadata, documentation='The version of the EBU-TT standard used by the document\n\t\t\t\t\t\t\tinstance.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 78, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentIdentifier'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='Identifier for an EBU-TT document that may be used as\n\t\t\t\t\t\t\texternal reference to an EBU-TT document.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 89, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentOriginatingSystem'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='Software and version used to create the EBU-TT\n\t\t\t\t\t\t\tdocument.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 95, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCopyright'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The copyright of the document.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentReadingSpeed'), pyxb.binding.datatypes.positiveInteger, scope=documentMetadata, documentation='The intended reading speed for the subtitles in words per\n\t\t\t\t\t\t\tminute.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 106, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTargetAspectRatio'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The aspect ratio of the video the EBU-TT document was\n\t\t\t\t\t\t\tauthored for, in width by height.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 112, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTargetActiveFormatDescriptor'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The code for the Active Format Descriptor (AFD) that\n\t\t\t\t\t\t\tspecifies the active image in the active video (see “Definitions of\n\t\t\t\t\t\t\tterms”). The code shall be one of the AFD codes specified in SMPTE ST\n\t\t\t\t\t\t\t2016 1:2009 “Format for Active Format Description and Bar Data” Table\n\t\t\t\t\t\t\t1.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 118, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetBarData'), CTD_ANON_4, scope=documentMetadata, documentation='When an ebuttm:documentTargetActiveFormatDescriptor\n\t\t\t\t\t\t\telement is used in an EBU-TT document, an\n\t\t\t\t\t\t\tebuttm:documentIntendedTargetBarData element may be used whenever the\n\t\t\t\t\t\t\tAFD alone is insufficient to describe the extent of the image (i.e. AFD\n\t\t\t\t\t\t\tvalues 0000 and 0100). The Bar Data shall be specified in accordance\n\t\t\t\t\t\t\twith SMPTE ST 2016 1:2009 “Format for Active Format Description and Bar\n\t\t\t\t\t\t\tData” Table 3.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 127, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetFormat'), CTD_ANON, scope=documentMetadata, documentation='Indicates the subtitle format an author had in mind when\n\t\t\t\t\t\t\tauthoring an EBU-TT document or transforming another format to an EBU-TT\n\t\t\t\t\t\t\tdocument.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 204, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCreationMode'), STD_ANON_3, scope=documentMetadata, documentation='Identifies the overall workflow used to create the content\n\t\t\t\t\t\t\tin the document.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 223, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentContentType'), CTD_ANON_, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 235, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceMediaIdentifier'), sourceMediaIdentifier_type, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 249, 7)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaIdentifier'), pyxb.binding.datatypes.string, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 250, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedObjectIdentifier'), CTD_ANON_2, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaDuration'), _ImportedBinding_ebu_tt_live_bindings__ebuttdt.mediaTimingType, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 256, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentBeginDate'), pyxb.binding.datatypes.date, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 257, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'localTimeOffset'), pyxb.binding.datatypes.anyType, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 258, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referenceClockIdentifier'), pyxb.binding.datatypes.anyType, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 259, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcastServiceIdentifier'), CTD_ANON_3, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTransitionStyle'), documentTransitionStyle_type, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 266, 7)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalProgrammeTitle'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The programme title in the original language. STL mapping:\n\t\t\t\t\t\t\tOriginal Programme Title (OPT).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 267, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalEpisodeTitle'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The title of the episode of the programme in the original\n\t\t\t\t\t\t\tlanguage. STL mapping: Original Episode Title (OET).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 273, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedProgrammeTitle'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The programme title in the local language. STL mapping:\n\t\t\t\t\t\t\tTranslated Programme Title (TPT).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 279, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedEpisodeTitle'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The title of the episode of the programme in the local\n\t\t\t\t\t\t\tlanguage. STL mapping: Translated Episode Title\n\t\t\t\t\t\t\t(TET).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 285, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsName'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation="Name of the translator. STL mapping: Translator's Name\n\t\t\t\t\t\t\t(TN). ", location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 292, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsContactDetails'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation="The translator's contact details. STL mapping:\n\t\t\t\t\t\t\tTranslator's Contact Details (TCD).", location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 298, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentSubtitleListReferenceCode'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='Free-format character string which may be used to provide\n\t\t\t\t\t\t\tan additional reference for the subtitle list. Note: This attribute is\n\t\t\t\t\t\t\tprovided to support conversion of STL subtitle files and to retain the\n\t\t\t\t\t\t\tmetadata from the GSI block. STL mapping: Subtitle List Reference Code\n\t\t\t\t\t\t\t(SLR)', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 304, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCreationDate'), pyxb.binding.datatypes.date, scope=documentMetadata, documentation='The date of creation of the EBU-TT document.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 313, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionDate'), pyxb.binding.datatypes.date, scope=documentMetadata, documentation='The date of the most-recent modifications to the EBU-TT\n\t\t\t\t\t\t\tdocument. ', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 319, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionNumber'), pyxb.binding.datatypes.nonNegativeInteger, scope=documentMetadata, documentation='The revision number of the EBU-TT document may be used to\n\t\t\t\t\t\t\tspecify a particular version of the subtitle list. ', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 325, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTotalNumberOfSubtitles'), pyxb.binding.datatypes.nonNegativeInteger, scope=documentMetadata, documentation='The number of subtitles. STL mapping: Total Number of\n\t\t\t\t\t\t\tSubtitles (TNS).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 331, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentMaximumNumberOfDisplayableCharacterInAnyRow'), pyxb.binding.datatypes.nonNegativeInteger, scope=documentMetadata, documentation='Maximum number of displayable rows per television frame\n\t\t\t\t\t\t\twhich could be occupied at any one time by the subtitles defined in the\n\t\t\t\t\t\t\tTTI blocks. STL mapping: Maximum Number of Displayable Characters in any\n\t\t\t\t\t\t\ttext row (MNC). ', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 337, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentStartOfProgramme'), _ImportedBinding_ebu_tt_live_bindings__ebuttdt.startOfProgrammeTimingType, scope=documentMetadata, documentation='The time code of the first frame of the recorded video\n\t\t\t\t\t\t\tsignal which is intended for transmission. Note: When the referenced\n\t\t\t\t\t\t\tstart timecode of the video material the subtitles were authored for is\n\t\t\t\t\t\t\tgreater than 00:00:00:00 (e.g. 10:00:00:00) it is recommended to specify\n\t\t\t\t\t\t\tthe attribute ebuttm:documentStartOfPrograme. STL mapping: Timecode:\n\t\t\t\t\t\t\tStart-of-Programme (TCP).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 345, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCountryOfOrigin'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='The country of origin of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tCountry of Origin (CO). ', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 355, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentPublisher'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='Name of the publisher of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tPublisher (PUB).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsName'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation="Name of the editor of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tEditor's Name (EN).", location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsContactDetails'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation="Information about the editor named in the metadata element\n\t\t\t\t\t\t\tdocumentEditorsName. STL mapping: Editor's Contact Details (ECD).\n\t\t\t\t\t\t", location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentUserDefinedArea'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='This field may be used to carry information about the\n\t\t\t\t\t\t\tprogramme or subtitle list, or other relevant details. STL mapping:\n\t\t\t\t\t\t\tUser-Defined Area (UDA).', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 380, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stlCreationDate'), pyxb.binding.datatypes.date, scope=documentMetadata, documentation='', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 387, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionDate'), pyxb.binding.datatypes.date, scope=documentMetadata, documentation='', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 392, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionNumber'), pyxb.binding.datatypes.nonNegativeInteger, scope=documentMetadata, documentation='', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 397, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitleZero'), pyxb.binding.datatypes.string, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 402, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalSourceServiceIdentifier'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='\n\t\t\t\t\t\t\tThe ebuttm:originalSourceServiceIdentifier may be used to identify the stream of\n\t\t\t\t\t\t\taudio-visual content that was used as the source for authoring the document.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intendedDestinationServiceIdentifier'), pyxb.binding.datatypes.string, scope=documentMetadata, documentation='\n\t\t\t\t\t\t\tThe ebuttm:intendedDestinationServiceIdentifier may be used to identify the streams of destination audio-visual\n\t\t\t\t\t\t\tcontent for which the document is intended to apply.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 411, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentFacet'), documentFacet_type, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 419, 4)))

documentMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing'), appliedProcessing_type, scope=documentMetadata, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 420, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 71, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 78, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 89, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 95, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 106, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 112, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 118, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 127, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 204, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 223, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 235, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 249, 7))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 250, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 256, 4))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 257, 4))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 258, 4))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 259, 4))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 266, 7))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 267, 4))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 273, 4))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 279, 4))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 285, 4))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 292, 4))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 298, 4))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 304, 4))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 313, 4))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 319, 4))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 325, 4))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 331, 4))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 337, 4))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 345, 4))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 355, 4))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 380, 4))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 387, 4))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 392, 4))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 397, 4))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 402, 4))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 411, 4))
    counters.add(cc_44)
    cc_45 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 419, 4))
    counters.add(cc_45)
    cc_46 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 420, 4))
    counters.add(cc_46)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conformsToStandard')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 71, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentEbuttVersion')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 78, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 89, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentOriginatingSystem')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 95, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCopyright')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentReadingSpeed')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 106, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTargetAspectRatio')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 112, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTargetActiveFormatDescriptor')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 118, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetBarData')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 127, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetFormat')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 204, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCreationMode')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 223, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentContentType')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 235, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceMediaIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 249, 7))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 250, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObjectIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaDuration')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 256, 4))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentBeginDate')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 257, 4))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'localTimeOffset')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 258, 4))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referenceClockIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 259, 4))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcastServiceIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTransitionStyle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 266, 7))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalProgrammeTitle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 267, 4))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalEpisodeTitle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 273, 4))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedProgrammeTitle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 279, 4))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedEpisodeTitle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 285, 4))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsName')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 292, 4))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsContactDetails')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 298, 4))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentSubtitleListReferenceCode')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 304, 4))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCreationDate')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 313, 4))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionDate')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 319, 4))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionNumber')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 325, 4))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTotalNumberOfSubtitles')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 331, 4))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentMaximumNumberOfDisplayableCharacterInAnyRow')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 337, 4))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentStartOfProgramme')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 345, 4))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCountryOfOrigin')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 355, 4))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentPublisher')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsName')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsContactDetails')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentUserDefinedArea')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 380, 4))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stlCreationDate')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 387, 4))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionDate')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 392, 4))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionNumber')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 397, 4))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subtitleZero')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 402, 4))
    st_42 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalSourceServiceIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4))
    st_43 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intendedDestinationServiceIdentifier')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 411, 4))
    st_44 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_45, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentFacet')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 419, 4))
    st_45 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_46, False))
    symbol = pyxb.binding.content.ElementUse(documentMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 420, 4))
    st_46 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_44, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_44, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_45, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_45, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_46, True) ]))
    st_46._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
documentMetadata._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 428, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:ebu:tt:metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 428, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
appliedProcessing_type._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 555, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=set(['not','urn:ebu:tt','http://www.w3.org/ns/ttml'])), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 555, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
anyMetadata_type._Automaton = _BuildAutomaton_2()




metadataBase_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title'), pyxb.binding.datatypes.string, scope=metadataBase_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 66, 2)))

metadataBase_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc'), pyxb.binding.datatypes.string, scope=metadataBase_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 67, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(metadataBase_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(metadataBase_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
metadataBase_type._Automaton = _BuildAutomaton_3()




headMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), _ImportedBinding_ebu_tt_live_bindings__ttm.CTD_ANON_, scope=headMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 15, 2)))

headMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentMetadata'), documentMetadata, scope=headMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 570, 5)))

headMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'binaryData'), binaryData_type, scope=headMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 577, 5)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 576, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 577, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 578, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(headMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(headMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(headMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentMetadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 570, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(headMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 576, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(headMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'binaryData')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 577, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 578, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
headMetadata_type._Automaton = _BuildAutomaton_4()




bodyMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), authoringTechnique_type, scope=bodyMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 588, 8)))

bodyMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle'), pyxb.binding.datatypes.string, scope=bodyMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 589, 5)))

bodyMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), facet_type, scope=bodyMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 590, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 588, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 589, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 590, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 591, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bodyMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(bodyMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(bodyMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 588, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(bodyMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 589, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(bodyMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 590, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 591, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
bodyMetadata_type._Automaton = _BuildAutomaton_5()




divMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), authoringTechnique_type, scope=divMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 601, 8)))

divMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'binaryData'), binaryData_type, scope=divMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 602, 5)))

divMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle'), pyxb.binding.datatypes.string, scope=divMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 603, 5)))

divMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), facet_type, scope=divMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 604, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 601, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 602, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 603, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 604, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 605, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(divMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(divMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(divMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 601, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(divMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'binaryData')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 602, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(divMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 603, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(divMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 604, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 605, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
divMetadata_type._Automaton = _BuildAutomaton_6()




pMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), authoringTechnique_type, scope=pMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 615, 8)))

pMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle'), pyxb.binding.datatypes.string, scope=pMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 616, 5)))

pMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), facet_type, scope=pMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 617, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 615, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 616, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 617, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 618, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 615, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transitionStyle')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 616, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 617, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 618, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pMetadata_type._Automaton = _BuildAutomaton_7()




spanMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), facet_type, scope=spanMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 628, 8)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 628, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 629, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(spanMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(spanMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(spanMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 628, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 629, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
spanMetadata_type._Automaton = _BuildAutomaton_8()




stylingMetadata_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'font'), font_type, scope=stylingMetadata_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 639, 8)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 639, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 640, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(stylingMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'title')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(stylingMetadata_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'desc')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(stylingMetadata_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'font')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 639, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 640, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
stylingMetadata_type._Automaton = _BuildAutomaton_9()

